import unicodedata
import json
import urllib.request
import urllib.error
import ssl
from difflib import SequenceMatcher
import os

API_KEY = "AIzaSyAZSKswUirIOfEE7-A01azX5betVuWwiD0"
API_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-2.5-flash:generateContent?key=" + API_KEY
)

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


def log_debug(text):
    try:
        with open("raimundo_log.txt", "a", encoding="utf-8") as f:
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


def avaliar_resposta(pergunta, resposta_correta, resposta_jogador, numero_pergunta):
    correta_norm = normalize(resposta_correta)
    jogador_norm = normalize(resposta_jogador)

    # ========================
    # 1 - ACERTO IDÊNTICO
    # ========================
    if jogador_norm == correta_norm:
        return "correta", "Você acertou! Excelente!"

    # ========================
    # 2 - ACERTO CONTIDO (variações)
    # ========================
    if correta_norm in jogador_norm:
        return (
            "correta",
            "Você acertou! Sua resposta está certa e equivalente à resposta esperada."
        )

    # ========================
    # 3 - IA COMO SEGUNDA CAMADA
    # ========================
    prompt = f"""
Você é o Robô Raimundo, mestre em Python.

Avalie se a resposta do aluno está correta ou incorreta.

Explique rapidamente o motivo.

Retorne SOMENTE JSON:

{{
  "status": "correta" ou "quase" ou "errada",
  "feedback": "mensagem curta explicando",
  "explicacao_equivalente": "como poderia ser dito de outra forma mantendo o sentido"
}}
"""

    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    try:
        req = urllib.request.Request(
            API_URL,
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        data = urllib.request.urlopen(req, context=ssl_context).read()
        raw = json.loads(data)["candidates"][0]["content"]["parts"][0]["text"]

        log_debug("RAW RESPONSE:\n" + raw)

        json_start = raw.find("{")
        json_end = raw.rfind("}")

        if json_start == -1 or json_end == -1:
            log_debug("JSON inválido detectado.")
            status = "errada"
            exp = ""
        else:
            result = json.loads(raw[json_start:json_end+1])

            status = result.get("status", "errada")
            exp = result.get("explicacao_equivalente", "")

        # ==========================
        # RESPOSTAS DA IA
        # ==========================

        # ---- CORRETA ----
        if status == "correta":
            msg = "Você acertou!"
            if exp:
                msg += f" {exp}"
            return "correta", msg

        # ---- QUASE (mas consideramos incorreta mesmo assim) ----
        if status == "quase":
            if numero_pergunta < 10:
                return (
                    "errada",
                    f"Quase! Mas ainda assim está incorreta.\nA resposta correta é: {resposta_correta}\nVamos para a próxima!"
                )
            else:
                return (
                    "errada",
                    f"Quase! Mas ainda assim está incorreta.\nA resposta correta é: {resposta_correta}"
                )

        # ---- ERRADA ----
        if numero_pergunta < 10:
            return (
                "errada",
                f"Você errou! A resposta correta é: {resposta_correta}\nVamos para a próxima!"
            )
        else:
            return (
                "errada",
                f"Você errou! A resposta correta é: {resposta_correta}"
            )

    except Exception as e:
        log_debug("EXCEÇÃO: " + str(e))

        if numero_pergunta < 10:
            return (
                "errada",
                f"Ocorreu um erro ao analisar sua resposta.\nA resposta correta é: {resposta_correta}\nVamos para a próxima!"
            )
        else:
            return (
                "errada",
                f"Ocorreu um erro ao analisar sua resposta.\nA resposta correta é: {resposta_correta}"
            )
