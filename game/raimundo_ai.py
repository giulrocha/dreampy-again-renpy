# ----------------------------------------
# IA DO RAIMUNDO - FASE 1 (VERSÃO INTELIGENTE)
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

    # ========== 1) EQUIVALÊNCIAS COMUNS ==========
    equivalencias = {
        "string": "str",
        "texto": "str",
        "palavra": "str",
        "numero": "int",
        "inteiro": "int"
    }

    if jogador_norm in equivalencias:
        jogador_norm = equivalencias[jogador_norm]

    # ========== 2) SE A RESPOSTA CERTA APARECE NA RESPOSTA ==========
    if correta_norm in jogador_norm:
        return "correta", "Muito bem! A resposta está certa."

    # ========== 3) SIMILARIDADE ==========
    similar = SequenceMatcher(None, jogador_norm, correta_norm).ratio()

    if similar >= 0.78:
        return "quase", "Quase lá! Você entendeu o conceito, só precisa ajustar um detalhe."

    # ========== 4) IA COMO CAMADA EXTRA (NÃO DECIDE SOZINHA) ==========
    prompt = f"""
    Você é o Robô Raimundo, mestre de Variáveis e Tipos em Python.
    Avalie se a resposta está correta com base na lógica e equivalência de significados.

    Pergunta: {pergunta}
    Resposta correta: {resposta_correta}
    Resposta do aluno: {resposta_jogador}

    Considere:
    - Respostas dentro de frases são corretas se contiverem o essencial.
    - Equivalentes como "string" = "str" devem ser aceitas como corretas.
    - Só marque errado se realmente estiver incorreta.
    - Se estiver quase certa, retorne "quase".

    Responda SOMENTE em JSON:
    {{
      "status": "correta" | "quase" | "errada",
      "feedback": "mensagem curta"
    }}
    """

    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        req = urllib.request.Request(
            API_URL,
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        data = urllib.request.urlopen(req, context=ssl_context).read()
        raw = json.loads(data)["candidates"][0]["content"]["parts"][0]["text"]

        result = json.loads(raw)

        # IA não pode marcar errado se a resposta contém o correto
        if result["status"] == "errada" and correta_norm in jogador_norm:
            return "correta", "Correto! Você respondeu dentro de uma frase."

        return result["status"], result["feedback"]

    except:
        # FALLBACK SEGURO — nunca devolve errado por falha da API
        if correta_norm in jogador_norm:
            return "correta", "Acertou! (fallback seguro)"
        elif similar >= 0.60:
            return "quase", "Quase! Ajuste um pouco sua resposta."
        else:
            return "errada", "Não é bem isso. Vamos tentar outra."
