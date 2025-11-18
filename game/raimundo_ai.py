# raimundo_ai.py

import json
import urllib.request
import urllib.error
import ssl


API_KEY = "AIzaSyAZSKswUirIOfEE7-A01azX5betVuWwiD0"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

# Ignora verificação SSL (igual ao Bit)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


def avaliar_resposta(pergunta, resposta_correta, resposta_jogador):
    """
    Compara a resposta do jogador com a resposta correta usando IA,
    mas com regras rígidas e fallback seguro.
    """

    headers = {"Content-Type": "application/json"}

    # 🔥 Normalização para facilitar a vida da IA
    resposta_correta_norm = resposta_correta.strip().lower()
    resposta_jogador_norm = resposta_jogador.strip().lower()

    # 🎯 Prompt SUPER explícito
    prompt = f"""
    Você é o Professor Raimundo, e deve avaliar a resposta do aluno.
    NUNCA forneça a resposta correta. Apenas avalie.

    Aqui estão os dados:

    PERGUNTA: '{pergunta}'
    RESPOSTA_CORRETA: '{resposta_correta_norm}'
    RESPOSTA_DO_ALUNO: '{resposta_jogador_norm}'

    Regras de avaliação:

    1. Considere letras maiúsculas/minúsculas como iguais.
    2. Considere respostas curtas como equivalentes se forem similares (ex: int == INT).
    3. Se a resposta estiver muito parecida mas não completa, retorne a categoria: quase.
    4. Se estiver totalmente correta, retorne: correta.
    5. Se estiver incorreta, retorne: errada.

    IMPORTANTE:
    Responda APENAS em JSON puro no formato:

    {{ 
      "status": "correta" ou "quase" ou "errada",
      "feedback": "mensagem curta para o aluno"
    }}

    Nada fora disso. Nenhum texto adicional.
    """

    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
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
            if not candidates:
                return "errada", "Não consegui avaliar sua resposta agora."

            texto = candidates[0]["content"]["parts"][0]["text"].strip()

            # 🛡️ Fallback: garantir que texto é JSON puro
            try:
                dados = json.loads(texto)
                status = dados.get("status", "errada")
                feedback = dados.get("feedback", "Explique sua resposta de outra forma, por favor.")

                # segurança
                if status not in ["correta", "quase", "errada"]:
                    status = "errada"

                return status, feedback

            except:
                # ❗ Se a IA NÃO retornar JSON válido → Fallback manual
                if resposta_jogador_norm == resposta_correta_norm:
                    return "correta", "Muito bem! Sua resposta está correta!"
                else:
                    return "errada", "Sua resposta ainda não está correta. Tente reformular."

    except Exception as e:
        return "errada", f"Erro ao avaliar: {e}"

