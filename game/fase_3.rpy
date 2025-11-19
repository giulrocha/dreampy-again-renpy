################### FASE 3 ###############################

image bg fase3 = "images/background/bg marinho.png"
image bg hub = "images/background/bg hub.png"


# --------------------------------------------------------
# CARREGANDO PERGUNTAS FASE 3
# --------------------------------------------------------
init python:
    import json
    import random
    import willon_ai

    try:
        with renpy.open_file("quiz_perguntas.json", encoding='utf-8') as f:
            dados_quiz = json.load(f)

        perguntas_fase_3 = dados_quiz["Estrutura de repetição (loops for e while)"]

    except Exception as e:
        renpy.error("Falha ao carregar o ficheiro 'quiz_perguntas.json' (Fase 3): " + str(e))



# --------------------------------------------------------
# INÍCIO DA FASE 3 - MARINHO
# --------------------------------------------------------

label marinho:

    hide screen MapUI

    scene expression Transform("bg fase3", fit="cover") with fade

    willon "Olá, [jogador]! Seja bem-vindo ao Universo de Estruturas de Repetição!"

    jogador "E quem é você?"

    willon "Eu sou o Tritão Willon! Vou testar seus laços e ciclos."

    jogador "Então vamos nessa, aceito seu desafio!"

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

        "DEBUG: Passar direto (100% acertos).":
            jump debug_passar_quiz_marinho

        "DEBUG: Falhar direto (0% acertos).":
            jump debug_falhar_quiz_marinho



# --- LABELS DE DEPURAÇÃO ---
label debug_passar_quiz_marinho:
    $ acertos = perguntas_totais
    jump verificar_resultado_quiz_marinho

label debug_falhar_quiz_marinho:
    $ acertos = 0
    jump verificar_resultado_quiz_marinho



# --------------------------------------------------------
# LÓGICA DO QUIZ - FASE 3
# --------------------------------------------------------

label preparar_quiz_marinho:

    $ acertos = 0

    show screen contador_quiz

    $ mapa_dificuldade = {"easy": "fácil", "normal": "médio", "hard": "difícil"}
    $ chave_dificuldade_atual = mapa_dificuldade[difficulty]

    $ lista_de_perguntas = list(perguntas_fase_3[chave_dificuldade_atual])
    $ random.shuffle(lista_de_perguntas)

    $ perguntas_da_sessao = lista_de_perguntas[:perguntas_totais]

    jump proxima_pergunta_marinho



label proxima_pergunta_marinho:

    if not perguntas_da_sessao:
        jump verificar_resultado_quiz_marinho

    $ pergunta_atual = perguntas_da_sessao[0]

    $ resposta_digitada = ""

    call screen quiz_escrita_screen(pergunta_atual['pergunta'])
    $ resposta_do_jogador = resposta_digitada.strip()

    if not resposta_do_jogador:
        willon "Você precisa digitar uma resposta para continuar o fluxo."
        jump proxima_pergunta_marinho

    $ status_resposta, feedback_willon = willon_ai.avaliar_resposta(
        pergunta_atual['pergunta'],
        pergunta_atual['resposta_correta'],
        resposta_do_jogador
    )

    willon "[feedback_willon]"

    if status_resposta == "correta":
        $ acertos += 1
        $ perguntas_da_sessao.pop(0)
        jogador "Meu loop está rodando certinho!"
        jump proxima_pergunta_marinho

    elif status_resposta == "quase":
        jogador "Quase acertei o fluxo..."
        willon "Você quase acertou o laço. Ajuste um detalhe e tente novamente."
        jump proxima_pergunta_marinho

    else:
        jogador "Acho que meu loop travou..."
        willon "Sua lógica de repetição ainda não está certa. Pense em como o laço deve se comportar."
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

    willon "Excelente, [jogador]! Você dominou os ciclos das profundezas."

    jogador "Falta cada vez menos pra voltar pra casa!"

    jump hub_controle_4_feliz


## Se não passar

label marinho_triste:

    willon "Ainda não. Seus laços precisam de ajustes."

    jogador "Eu vou praticar mais!"

    jump hub_controle_4_triste



## Fase 1, 2, 3 e 4 liberadas

label hub_controle_4_feliz:

    scene expression Transform("bg hub", fit="cover") with pixellate

    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"

    jogador "Vamos lá, próxima missão!"

    jump hub_mapa


## Fase 1, 2 e 3 liberadas

label hub_controle_4_triste:

    scene expression Transform("bg hub", fit="cover") with pixellate

    android "Que pena [jogador], mas você pode tentar novamente."

    jogador "Vou voltar mais forte!"

    jump hub_mapa
