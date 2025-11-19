import json
import urllib.request
import urllib.error
import ssl

API_KEY = "AIzaSyAZSKswUirIOfEE7-A01azX5betVuWwiD0"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

# Ignora verificação SSL
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def limitar_linhas(texto, max_linhas=10):
    linhas = texto.strip().splitlines()
    return "\n".join(linhas[:max_linhas])

def perguntar_ao_bit(pergunta):
    if not pergunta or not pergunta.strip():
        return "Por favor, escreva uma pergunta."

    headers = {
        "Content-Type": "application/json",
    }

    # Contexto do jogo: só responde sobre esses assuntos
    contexto = (
        "Você se chama bit e é um assistente em um jogo educativo de programação em Python, seja educado e muito simpatico ao responder. "
        "Responda APENAS perguntas relacionadas aos seguintes tópicos: "
        "1) variáveis, tipos de dados e valores; "
        "2) nomes de variáveis válidos; "
        "3) lógica e estruturas condicionais (if, else, elif); "
        "4) estruturas de repetição (for, while); "
        "5) funções (def, return); "
        "6) listas e dicionários (criação, acesso, métodos básicos). "
        "Se a pergunta estiver fora desse escopo, diga que não pode responder. "
        "Se estiver no escopo, responda de forma resumida (máximo 10 linhas)."
    )

    pergunta_formatada = f"{contexto}\n\nPergunta: {pergunta.strip()}"

    payload = {
        "contents": [
            {
                "parts": [{"text": pergunta_formatada}]
            }
        ]
    }

    try:
        req = urllib.request.Request(
            API_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST"
        )

        with urllib.request.urlopen(req, context=ssl_context) as response:
            result = json.loads(response.read().decode("utf-8"))
            candidates = result.get("candidates", [])
            if candidates:
                texto_bruto = candidates[0]["content"]["parts"][0]["text"]
                return limitar_linhas(texto_bruto, max_linhas=10)
            else:
                return "⚠️ Nenhuma resposta recebida do Bit."

    except urllib.error.HTTPError as e:
        return f"Erro HTTP {e.code}: {e.reason}"

    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"
