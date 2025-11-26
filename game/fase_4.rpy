################### FASE 4 ###############################

image bg fase4 = "images/background/bg medieval.png"
image bg hub = "images/background/bg hub.png"
image frank = "images/characters/frank.png"
image frank_erro = "images/characters/frank_erro.png"
image frank_falando = "images/characters/frank_falando.png"
image frank_feliz = "images/characters/frank_feliz.png"
image gilberto_android = "images/characters/gilberto_android.png"

transform frankfit:
    zoom 2

# CARREGANDO PERGUNTAS FASE 4

init python:
    import json
    import random
    import frank_ai

    try:
        with renpy.open_file("quiz_perguntas.json", encoding='utf-8') as f:
            dados_quiz = json.load(f)

        perguntas_fase_4 = dados_quiz["Funções e modularização (def, return)"]
    except Exception as e:
        renpy.error("Falha ao carregar 'quiz_perguntas.json' (Fase 4): " + str(e))


label medieval:

    hide screen MapUI

    scene expression Transform("bg fase4", fit="cover") with fade
    show frank_falando at frankfit, center

    frank "Olá, [jogador]! Seja bem-vindo ao Universo de Funções e Modularização!"

    hide frank_falando at frankfit, center
    show frank at frankfit, center

    jogador "E quem é você?"

    hide frank at frankfit, center
    show frank_falando at frankfit, center

    frank "Serei o seu desafiante, caso passe pelos meus desafios, ficará mais próximo de voltar pra casa"
   
    hide frank_falando at frankfit, center
    show frank_feliz at frankfit, center

    jogador "Aceito seu desafio!"   
    hide frank_feliz at frankfit, center
    hide frank at frankfit, center

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
            jump preparar_quiz_medieval



# --- LABELS DE DEPURAÇÃO ---
label debug_passar_quiz_medieval:
    $ acertos = perguntas_totais
    jump verificar_resultado_quiz_medieval

label debug_falhar_quiz_medieval:
    $ acertos = 0
    jump verificar_resultado_quiz_medieval



label preparar_quiz_medieval:

    $ acertos = 0

    show screen contador_quiz

    $ mapa_dificuldade = {"easy": "fácil", "normal": "médio", "hard": "difícil"}
    $ chave_dificuldade_atual = mapa_dificuldade[difficulty]

    $ lista_de_perguntas = list(perguntas_fase_4[chave_dificuldade_atual])
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

    jump proxima_pergunta_medieval



label proxima_pergunta_medieval:

    if not perguntas_da_sessao:
        jump verificar_resultado_quiz_medieval

    $ pergunta_atual = perguntas_da_sessao[0]
    $ resposta_digitada = ""

    call screen quiz_escrita_screen(pergunta_atual['answer'])
    $ resposta_do_jogador = resposta_digitada.strip()

    if not resposta_do_jogador:
        frank "Você precisa escrever algo para eu avaliar sua magia de funções."
        jump proxima_pergunta_medieval

    $ numero_da_pergunta = (perguntas_totais - len(perguntas_da_sessao)) + 1

    $ resultado = frank_ai.avaliar_resposta(
        pergunta_atual['answer'],
        pergunta_atual['answer_correct'],
        resposta_do_jogador,
        numero_da_pergunta
    )
    $ status_resposta = resultado.get("status")
    $ feedback_frank = resultado.get("feedback")

    frank "[feedback_frank]"

    if status_resposta == "correta":
        $ acertos += 1

    jump proxima_pergunta_medieval



label verificar_resultado_quiz_medieval:

    hide screen contador_quiz

    if acertos >= acertos_para_passar:
        jump medieval_feliz
    else:
        jump medieval_triste



## Se passar

label medieval_feliz:

    $ fase_5_liberada = True
    
    show frank_feliz at grande, center

    frank "Parabéns, [jogador]! Você dominou as artes das funções e da modularização!"

    jogador "Só mais uma fase e eu posso voltar pra casa!"

    hide frank_feliz at grande, center

    jump hub_controle_5_feliz


## Se não passar

label medieval_triste:

    show frank_erro at grande, center
    
    frank "Infelizmente você não está pronto, mas você pode tentar novamente!"

    hide frank_erro at grande, center

    jump hub_controle_5_triste



## Fase 1, 2, 3, 4 e 5 liberadas

label hub_controle_5_feliz:

    scene expression Transform("bg hub", fit="cover") with pixellate
    show gilberto_android at Position(xpos=0.35, ypos=0.86, xanchor=0.8, yanchor=1.0)

    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a última fase!"

    jogador "Vamos lá! Eu vou até o fim!"

    jump hub_mapa


## Fase 1, 2, 3 e 4 liberadas

label hub_controle_5_triste:

    scene expression Transform("bg hub", fit="cover") with pixellate
    show gilberto_android at Position(xpos=0.35, ypos=0.86, xanchor=0.8, yanchor=1.0)

    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente."

    jogador "Estou quase lá, eu sinto isso. Vou tentar de novo!"

    jump hub_mapa