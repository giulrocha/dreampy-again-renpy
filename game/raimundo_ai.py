# ----------------------------------------
# IA DO RAIMUNDO - FASE 1
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

    # ========= NEGATIVO AUTOMÁTICO ==========
    if "nao" in jogador_norm or "não" in jogador_norm:
        return "errada", "Cuidado! Parece que você negou a resposta correta."

    # ========= CONTIDO DIRETO ==========
    if correta_norm in jogador_norm:
        return "correta", "Muito bem! Você acertou direitinho!"

    # ========= APROXIMAÇÃO ==========
    similar = SequenceMatcher(None, jogador_norm, correta_norm).ratio()
    if similar >= 0.78:
        return "quase", "Você está muito perto! Falta só um ajuste."

    # ========= IA COMO SEGUNDA CAMADA ==========
    prompt = f"""
Você é o Robô Raimundo, mestre de Variáveis e Tipos em Python.

Avalie se a resposta do aluno está correta considerando:
- respostas dentro de frases são corretas se contiverem o essencial
- formas equivalentes são corretas ("string" = str)
- pequenos erros ⇒ QUASE
- negações ⇒ ERRADO

Pergunta: {pergunta}
Resposta correta: {resposta_correta}
Resposta do aluno: {resposta_jogador}

Responda em JSON puro:

{{
  "status": "correta" ou "quase" ou "errada",
  "feedback": "mensagem curta"
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
        return "quase", "Você está perto! Ajuste e tente novamente."
