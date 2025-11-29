import unicodedata
import json
import urllib.request
import urllib.error
import ssl
from difflib import SequenceMatcher
import os
import requests


ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


def log_debug(text):
    try:
        with open("willon_log.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n\n")
    except:
        pass

def normalize(text):
    if not text:
        return ""

    text = text.lower()
    text = "".join(
        c for c in unicodedata.normalize("NFD", text)
        if unicodedata.category(c) != "Mn"
    )
    text = text.replace(" ", "").replace("_", "").replace("-", "")
    return text


def avaliar_resposta(answer, answer_correct, resposta_do_jogador, numero_da_pergunta):
    try:
        r = requests.post(
            "http://ec2-107-20-38-175.compute-1.amazonaws.com:30001/avaliar_resposta_api/",
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