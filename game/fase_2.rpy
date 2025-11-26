################### FASE 2 ###############################

image bg fase2 = "images/background/bg cyberpunk.png"
image bg hub = "images/background/bg hub.png"
image vanilton = "images/characters/vanilton.png"
image gilberto_android = "images/characters/gilberto_android.png"

transform grande: 
    zoom 2.3


# CARREGANDO PERGUNTAS FASE 2
init python:
    import json
    import random
    import requests
    import vanilton_ai

    try:
        url_json = "https://senselessly-patronal-jorge.ngrok-free.dev/api/core/quiz/?format=json"

        resposta = requests.get(url_json)
        renpy.log("STATUS: " + str(resposta.status_code))
        renpy.log("CONTENT RAW: " + resposta.text[:500])  # exibe conteúdo bruto

        resposta.raise_for_status()
        dados_quiz = resposta.json()

        renpy.log("JSON CARREGADO: " + str(dados_quiz)[:500])

        perguntas_fase_2 = dados_quiz["Lógica e estruturas condicionais (if, else, elif)"]

    except Exception as e:
        renpy.error("Falha ao carregar as perguntas da Fase 2 do 'quiz_perguntas.json': " + str(e))



label cyberpunk:

    hide screen MapUI

    scene expression Transform("bg fase2", fit="cover") with fade
    
    show vanilton at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    vanilton "Olá, [jogador]! Seja bem-vindo ao Universo de Lógica e Estruturas Condicionais!"

    jogador "E quem é você?"

    vanilton "Sou Vanilton. Vou testar se sua lógica é forte o suficiente para continuar."

    jogador "Pode mandar, eu aceito o desafio!"

    hide vanilton

    if difficulty == "easy":
        $ perguntas_totais = 10
        $ acertos_para_passar = 7

    elif difficulty == "normal":
        $ perguntas_totais = 10
        $ acertos_para_passar = 7

    else:
        $ perguntas_totais = 10
        $ acertos_para_passar = 7

    # --- MENU DE DEPURAÇÃO  ---
    menu:
        "Iniciar o questionário normalmente.":
            jump preparar_quiz_cyberpunk



# --- LABELS DE DEPURAÇÃO ---
label debug_passar_quiz_cyberpunk:
    $ acertos = perguntas_totais
    jump verificar_resultado_quiz_cyberpunk

label debug_falhar_quiz_cyberpunk:
    $ acertos = 0
    jump verificar_resultado_quiz_cyberpunk


# LÓGICA DO QUIZ - FASE 2

label preparar_quiz_cyberpunk:

    $ acertos = 0

    show screen contador_quiz

    $ mapa_dificuldade = {"easy": "fácil", "normal": "médio", "hard": "difícil"}
    $ chave_dificuldade_atual = mapa_dificuldade[difficulty]

    $ lista_de_perguntas = list(perguntas_fase_2[chave_dificuldade_atual])
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

    jump proxima_pergunta_cyberpunk



label proxima_pergunta_cyberpunk:

    if not perguntas_da_sessao:
        jump verificar_resultado_quiz_cyberpunk

    $ pergunta_atual = perguntas_da_sessao[0]
    $ resposta_digitada = ""

    call screen quiz_escrita_screen(pergunta_atual['answer'])
    $ resposta_do_jogador = resposta_digitada.strip()

    if not resposta_do_jogador:
        vanilton "Você precisa digitar alguma coisa para eu avaliar sua lógica."
        jump proxima_pergunta_cyberpunk

    $ numero_da_pergunta = (perguntas_totais - len(perguntas_da_sessao)) + 1

    $ resultado = None

    # IA do Vanilton (versão padronizada)
    python:
        import renpy.store as store

        def chamar_ia_async():
            store.resultado = vanilton_ai.avaliar_resposta(
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
    $ feedback_vanilton = resultado.get("feedback")

    show vanilton at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)
    vanilton "[feedback_vanilton]"
    hide vanilton at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    if status_resposta == "correta":
        $ acertos += 1

    $ perguntas_da_sessao.pop(0)

    jump proxima_pergunta_cyberpunk




label verificar_resultado_quiz_cyberpunk:

    hide screen contador_quiz

    if acertos >= acertos_para_passar:
        jump cyberpunk_feliz
    else:
        jump cyberpunk_triste



## Se passar

label cyberpunk_feliz:

    $ fase_3_liberada = True

    show vanilton at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    vanilton "Parabéns, [jogador]! Sua lógica passou nos meus testes."

    jogador "Ótimo, mais um passo pra casa!"

    hide vanilton at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    jump hub_controle_3_feliz



## Se não passar

label cyberpunk_triste:

    show vanilton at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    vanilton "Você ainda não domina bem as estruturas condicionais. Mas pode tentar de novo."

    jogador "Não vou desistir. Vou ajustar minha lógica!"

    hide vanilton at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    jump hub_controle_3_triste



## Fase 1, 2 e 3 liberada

label hub_controle_3_feliz:

    scene expression Transform("bg hub", fit="cover") with pixellate
    show gilberto_android at Position(xpos=0.35, ypos=0.86, xanchor=0.8, yanchor=1.0)

    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"

    jogador "Pode vir a próxima. Estou pronto!"

    jump hub_mapa



## Fase 1 e 2 liberadas

label hub_controle_3_triste:

    scene expression Transform("bg hub", fit="cover") with pixellate
    show gilberto_android at Position(xpos=0.35, ypos=0.86, xanchor=0.8, yanchor=1.0)

    android "Que pena [jogador], mas você pode tentar novamente."

    jogador "Eu volto mais forte!"

    jump hub_mapa
