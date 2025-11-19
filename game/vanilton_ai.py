# ----------------------------------------
# IA DO VANILTON - FASE 2 (VERSÃO INTELIGENTE)
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
        "igual": "==",
        "igualdade": "==",
        "comparacao": "==",
        "condicao": "if",
        "se": "if",
        "senao": "else",
        "caso contrario": "else"
    }

    if jogador_norm in equivalencias:
        jogador_norm = equivalencias[jogador_norm]

    if correta_norm in jogador_norm:
        return "correta", "Boa! Sua lógica está afiada como uma lâmina cyberpunk!"

    similar = SequenceMatcher(None, jogador_norm, correta_norm).ratio()
    if similar >= 0.78:
        return "quase", "Quase! Só falta um detalhe na condição."

    # IA EXTRA — não decide sozinha, mas reforça
    prompt = f"""
Você é Vanilton, mestre da lógica no universo Cyberpunk.

Avalie a resposta considerando:
- estruturas condicionais (if, elif, else)
- equivalências semânticas (“se x é igual a 10” = x == 10)
- respostas dentro de frases
- não penalizar explicações longas
- só marcar ERRADO se realmente estiver incorreta

Pergunta: {pergunta}
Resposta correta: {resposta_correta}
Resposta do aluno: {resposta_jogador}

Responda SOMENTE JSON:
{{"status": "...", "feedback": "..."}}
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

        # IA nunca pode marcar errado se contém a resposta
        if result["status"] == "errada" and correta_norm in jogador_norm:
            return "correta", "Correto! Você expressou a lógica dentro de um contexto."

        return result["status"], result["feedback"]

    except:
        if correta_norm in jogador_norm:
            return "correta", "Correto! (fallback seguro)"
        elif similar >= 0.60:
            return "quase", "Quase! Só ajustar um detalhe lógico."
        else:
            return "errada", "Não parece a condição correta."
