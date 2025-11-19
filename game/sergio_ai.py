# ----------------------------------------
# IA DO SERGIO - FASE 5 (INTELIGENTE)
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
        "lista": "[]",
        "vetor": "[]",
        "colecao": "[]",
        "dicionario": "{}",
        "tabela": "{}",
        "mapa": "{}"
    }

    if jogador_norm in equivalencias:
        jogador_norm = equivalencias[jogador_norm]

    if correta_norm in jogador_norm:
        return "correta", "Muito bem! Você manipulou listas e dicionários como um alien especialista!"

    similar = SequenceMatcher(None, jogador_norm, correta_norm).ratio()
    if similar >= 0.78:
        return "quase", "Quase! Só ajustar a estrutura do elemento."

    prompt = f"""
Você é Sérgio, alien mestre de listas e dicionários.

Considere:
- explicações dentro de frases = CORRETAS
- equivalências (“uma lista usa colchetes”) = CORRETAS
- acessos semelhantes → QUASE

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
            return "correta", "Correto! Você respondeu dentro de uma frase válida."

        return result["status"], result["feedback"]

    except:
        if correta_norm in jogador_norm:
            return "correta", "Correto! (fallback seguro)"
        elif similar >= 0.60:
            return "quase", "Quase! Estrutura quase perfeita."
        else:
            return "errada", "Não é essa estrutura de dados."
