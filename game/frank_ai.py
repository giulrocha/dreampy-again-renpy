# ----------------------------------------
# IA DO FRANK - FASE 4
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

    if "nao" in jogador_norm or "não" in jogador_norm:
        return "errada", "Hum... parece que você está negando a função correta."

    if correta_norm in jogador_norm:
        return "correta", "Excelente! Sua magia de funções está poderosa!"

    similar = SequenceMatcher(None, jogador_norm, correta_norm).ratio()
    if similar >= 0.75:
        return "quase", "Quase lá! Só falta um toque de magia Python."

    prompt = f"""
Você é Frank, mago supremo das Funções em Python.

Considere como CORRETO:
- qualquer frase contendo a forma correta
- qualquer forma equivalente (“uma função começa com def”)
- explicações semânticas do conceito
- chamadas equivalentes

Pergunta: {pergunta}
Resposta correta: {resposta_correta}
Resposta do aluno: {resposta_jogador}

JSON apenas:

{{
  "status": "...",
  "feedback": "..."
}}
"""

    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        req = urllib.request.Request(API_URL, data=json.dumps(payload).encode(),
                                     headers={"Content-Type": "application/json"}, method="POST")
        data = urllib.request.urlopen(req, context=ssl_context).read()
        raw = json.loads(data)["candidates"][0]["content"]["parts"][0]["text"]
        result = json.loads(raw)
        return result["status"], result["feedback"]
    except:
        return "quase", "Você está muito perto de conjurar a função correta!"
