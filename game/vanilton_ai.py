# ----------------------------------------
# IA DO VANILTON - FASE 2 (PADRONIZADO)
# ----------------------------------------
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
        with open("vanilton_log.txt", "a", encoding="utf-8") as f:
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
    correta_norm = normalize(answer_correct)
    jogador_norm = normalize(resposta_do_jogador)

    # ==================================
    # 1 - ACERTO IDÊNTICO
    # ==================================
    if jogador_norm == correta_norm:
        return "correta", "Perfeito! Você dominou a lógica como um verdadeiro hacker!"

    # ==================================
    # 2 - ACERTO CONTIDO (variações)
    # ==================================
    if correta_norm in jogador_norm:
        return (
            "correta",
            "Boa! Sua lógica está afiada como uma lâmina cyberpunk!"
        )

    # ==================================
    # 3 - AJUDA DA IA (mesma estrutura do Raimundo)
    # ==================================
    prompt = f"""
Você é Vanilton, mente lógica suprema do universo cyberpunk.

Avalie se a resposta está correta, quase correta ou incorreta.

Regras:
- reconhecer equivalências lógicas (“x igual a 10” = x == 10)
- não punir explicações longas
- considerar contexto
- só marcar como INCORRETA se realmente estiver errada

Retorne SOMENTE JSON:

{{
  "status": "correta" ou "quase" ou "errada",
  "feedback": "mensagem curta explicando",
  "explicacao_equivalente": "forma alternativa correta de expressar a lógica"
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

        # Extrair JSON (mesmo método do Raimundo)
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

        # ========== RESPOSTA DA IA ==========

        # ---- CORRETA ----
        if status == "correta":
            msg = "Correto! Excelente!"
            if exp:
                msg += f" {exp}"
            return "correta", msg

        # ---- QUASE ----
        if status == "quase":
            if numero_pergunta < 10:
                return (
                    "errada",
                    f"Quase! Está perto, mas ainda não é o ideal.\nA lógica correta é: {answer_correct}\nContinue!"
                )
            else:
                return (
                    "errada",
                    f"Quase! Mas ainda assim está incorreta.\nA lógica correta é: {answer_correct}"
                )

        # ---- ERRADA ----
        if numero_da_pergunta < 10:
            return (
                "errada",
                f"Resposta incorreta.\nA lógica correta é: {answer_correct}\nVamos para a próxima!"
            )
        else:
            return (
                "errada",
                f"Você errou.\nA lógica correta é: {answer_correct}"
            )

    except Exception as e:
        log_debug("EXCEÇÃO: " + str(e))

        # fallback elegante
        if correta_norm in jogador_norm:
            return (
                "correta",
                "Boa! Sua resposta está correta (fallback seguro)."
            )

        # quase
        similar = SequenceMatcher(None, jogador_norm, correta_norm).ratio()
        if similar >= 0.70:
            if numero_da_pergunta < 10:
                return (
                    "errada",
                    f"Quase! Falta um ajuste.\nA lógica correta é: {answer_correct}"
                )
            else:
                return (
                    "errada",
                    f"Quase! Mas a lógica correta é: {answer_correct}"
                )

        # erro mesmo
        if numero_da_pergunta < 10:
            return (
                "errada",
                f"Ocorreu um erro interno. A lógica correta é: {answer_correct}\nVamos continuar!"
            )
        else:
            return (
                "errada",
                f"Ocorreu um erro. A resposta correta é: {answer_correct}"
            )
