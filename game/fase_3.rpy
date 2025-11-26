################### FASE 3 ###############################

image bg fase3 = "images/background/bg marinho.png"
image bg hub = "images/background/bg hub.png"
image willon = "images/characters/willon_serio.png"
image willon_falando = "images/characters/willon_falando.png"
image willon_feliz = "images/characters/willon_feliz.png"
image willon_desapontado = "images/characters/willon_desapontado.png"
image gilberto_android = "images/characters/gilberto_android.png"

# CARREGANDO PERGUNTAS FASE 3

init python:
    import json
    import random
    import willon_ai
    import requests

    try:
        url_json = "https://senselessly-patronal-jorge.ngrok-free.dev/api/core/quiz/?format=json"

        resposta = requests.get(url_json)
        renpy.log("STATUS: " + str(resposta.status_code))
        renpy.log("CONTENT RAW: " + resposta.text[:500])  # exibe conteúdo bruto

        resposta.raise_for_status()
        dados_quiz = resposta.json()

        renpy.log("JSON CARREGADO: " + str(dados_quiz)[:500])

        perguntas_fase_3 = dados_quiz["Estrutura de repetição (loops for e while)"]

    except Exception as e:
        renpy.error("Falha ao carregar o ficheiro 'quiz_perguntas.json' (Fase 3): " + str(e))


label marinho:

    hide screen MapUI

    scene expression Transform("bg fase3", fit="cover") with fade
    show willon_falando at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)

    willon "Olá, [jogador]! Seja bem-vindo ao Universo de Estruturas de Repetição!"

    hide willon_falando at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)
    show willon at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)

    jogador "E quem é você?"

    hide willon at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)
    show willon_falando at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)

    willon "Serei o seu desafiante, caso passe pelos meus desafios, ficará mais perto de voltar pra casa"

    hide willon_falando at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)
    show willon_feliz at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)

    jogador "Aceito seu desafio!"
    hide willon_feliz at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)

    if difficulty == "easy":
        $ perguntas_totais = 10
        $ acertos_para_passar = 7

    elif difficulty == "normal":
        $ perguntas_totais = 10
        $ acertos_para_passar = 7

    else:
        $ perguntas_totais = 10
        $ acertos_para_passar = 7

    # --- MENU DE DEPURAÇÃO ---
    menu:
        "Iniciar o questionário normalmente.":
            jump preparar_quiz_marinho



# --- LABELS DE DEPURAÇÃO ---
label debug_passar_quiz_marinho:
    $ acertos = perguntas_totais
    jump verificar_resultado_quiz_marinho

label debug_falhar_quiz_marinho:
    $ acertos = 0
    jump verificar_resultado_quiz_marinho



# LÓGICA DO QUIZ - FASE 3

label preparar_quiz_marinho:

    $ acertos = 0

    show screen contador_quiz

    $ mapa_dificuldade = {"easy": "fácil", "normal": "médio", "hard": "difícil"}
    $ chave_dificuldade_atual = mapa_dificuldade[difficulty]

    $ lista_de_perguntas = list(perguntas_fase_3[chave_dificuldade_atual])
    python:
        perguntas_unicas = []
        vistas = set()
        for p in lista_de_perguntas:
            # usa o texto da pergunta como chave de unicidade
            key = p.get("answer", "")
            if key not in vistas:
                vistas.add(key)
                perguntas_unicas.append(p)
    $ random.shuffle(lista_de_perguntas)

    $ perguntas_da_sessao = lista_de_perguntas[:perguntas_totais]

    jump proxima_pergunta_marinho



label proxima_pergunta_marinho:

    if not perguntas_da_sessao:
        jump verificar_resultado_quiz_marinho

    $ pergunta_atual = perguntas_da_sessao[0]
    $ resposta_digitada = ""

    call screen quiz_escrita_screen(pergunta_atual['answer'])
    $ resposta_do_jogador = resposta_digitada.strip()

    if not resposta_do_jogador:
        willon "Você precisa digitar uma resposta para continuar o fluxo."
        jump proxima_pergunta_marinho
    $ numero_da_pergunta = (perguntas_totais - len(perguntas_da_sessao)) + 1
    $ resultado = None

    python:
        import renpy.store as store

        def chamar_ia_async():
            store.resultado = willon_ai.avaliar_resposta(
                pergunta_atual['answer'],
                pergunta_atual['answer_correct'],
                resposta_do_jogador,
                numero_da_pergunta
            )

        renpy.invoke_in_thread(chamar_ia_async)
        
    show screen thinking_screen_auto_hide

    $ renpy.pause(0.1, hard=False)

    while resultado is None:
        $ renpy.pause(0.1, hard=False)

    hide screen thinking_screen_auto_hide
    
    $ status_resposta = resultado.get("status")
    $ feedback_willon = resultado.get("feedback")

    if status_resposta == "correta":
        show willon_feliz at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)
    elif status_resposta == "errada":
        show willon_desapontado at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)
    else:
        show willon_normal at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)
    willon "[feedback_willon]"
    if status_resposta == "correta":
        hide willon_feliz at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)
    elif status_resposta == "errada":
        hide willon_desapontado at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)
    else:
        hide willon_normal at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)

    if status_resposta == "correta":
        $ acertos += 1
    $ perguntas_da_sessao.pop(0)

    jump proxima_pergunta_marinho



label verificar_resultado_quiz_marinho:

    hide screen contador_quiz

    if acertos >= acertos_para_passar:
        jump marinho_feliz
    else:
        jump marinho_triste



## Se passar

label marinho_feliz:

    $ fase_4_liberada = True

    show willon_feliz at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)

    willon "Excelente, [jogador]! Você dominou os ciclos das profundezas."

    jogador "Falta cada vez menos pra voltar pra casa!"

    hide willon_feliz at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)

    jump hub_controle_4_feliz


## Se não passar

label marinho_triste:

    show willon_desapontado at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)

    willon "Ainda não. Seus laços precisam de ajustes."

    jogador "Eu vou praticar mais!"

    hide willon_desapontado at Position(xpos=0.75, ypos=0.75, xanchor=0.5, yanchor=1.0)

    jump hub_controle_4_triste



## Fase 1, 2, 3 e 4 liberadas

label hub_controle_4_feliz:

    scene expression Transform("bg hub", fit="cover") with pixellate
    show gilberto_android at Position(xpos=0.35, ypos=0.86, xanchor=0.8, yanchor=1.0)

    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"

    jogador "Vamos lá, próxima missão!"

    jump hub_mapa


## Fase 1, 2 e 3 liberadas

label hub_controle_4_triste:

    scene expression Transform("bg hub", fit="cover") with pixellate
    show gilberto_android at Position(xpos=0.35, ypos=0.86, xanchor=0.8, yanchor=1.0)

    android "Que pena [jogador], mas você pode tentar novamente."

    jogador "Vou voltar mais forte!"

    jump hub_mapa
