# ----------------------------------------
# IA DO FRANK - FASE 4 (INTELIGENTE)
# ----------------------------------------
import unicodedata
import json
import urllib.request
import urllib.error
import ssl
from difflib import SequenceMatcher

API_KEY = "AIzaSyAZSKswUirIOfEE7-A01azX5betVuWwiD0"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


def normalize(text):
    if not text:
        return ""
    text = text.lower()
    text = ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')
    text = text.replace(" ", "").replace("_", "").replace("-", "")
    return text


def avaliar_resposta(pergunta, resposta_correta, resposta_jogador):

    correta_norm = normalize(resposta_correta)
    jogador_norm = normalize(resposta_jogador)

    equivalencias = {
        "funcao": "def",
        "function": "def",
        "declarar": "def",
        "retorno": "return",
        "resultado": "return"
    }

    if jogador_norm in equivalencias:
        jogador_norm = equivalencias[jogador_norm]

    if correta_norm in jogador_norm:
        return "correta", "Perfeito! Sua magia de funções está impecável!"

    similar = SequenceMatcher(None, jogador_norm, correta_norm).ratio()
    if similar >= 0.78:
        return "quase", "Quase lá! Só falta um toque arcano na função."

    prompt = f"""
Você é Frank, mago supremo das Funções.

Avalie equivalências:
- “uma função começa com def” = CORRETO
- “retorna o valor usando return” = CORRETO
- resposta dentro de frases = CORRETO

Pergunta: {pergunta}
Correta: {resposta_correta}
Aluno: {resposta_jogador}

JSON:
{{"status":"...","feedback":"..."}}
"""

    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        req = urllib.request.Request(API_URL,
                                     data=json.dumps(payload).encode(),
                                     headers={"Content-Type": "application/json"},
                                     method="POST")
        data = urllib.request.urlopen(req, context=ssl_context).read()
        raw = json.loads(data)["candidates"][0]["content"]["parts"][0]["text"]
        result = json.loads(raw)

        if result["status"] == "errada" and correta_norm in jogador_norm:
            return "correta", "Correto! Você expressou a função de maneira válida."

        return result["status"], result["feedback"]

    except:
        if correta_norm in jogador_norm:
            return "correta", "Correto! (fallback seguro)"
        elif similar >= 0.60:
            return "quase", "Quase! Falta pouco para conjurar a função certa."
        else:
            return "errada", "Ainda não é essa estrutura de função."
