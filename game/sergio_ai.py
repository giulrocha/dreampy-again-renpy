# ----------------------------------------
# IA DO SERGIO - FASE 5 (INTELIGENTE)
# ----------------------------------------
import unicodedata
import json
import urllib.request
import urllib.error
import ssl
import requests
from difflib import SequenceMatcher


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


def avaliar_resposta(answer, answer_correct, resposta_do_jogador, numero_da_pergunta):
    try:
        r = requests.post(
            "https://senselessly-patronal-jorge.ngrok-free.dev/avaliar_resposta_api/",
            json={
                "answer": answer,
                "answer_correct": answer_correct,
                "resposta_do_jogador": resposta_do_jogador
            },
            # timeout=10
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"status": "errada", "feedback": f"Erro: {e}", "equivalencia": ""}