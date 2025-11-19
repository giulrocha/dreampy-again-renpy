################### FASE 4 ###############################

image bg fase4 = "images/background/bg medieval.png"
image bg hub = "images/background/bg hub.png"


# --------------------------------------------------------
# CARREGANDO PERGUNTAS FASE 4
# --------------------------------------------------------
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



# --------------------------------------------------------
# INÍCIO DA FASE 4 - MEDIEVAL
# --------------------------------------------------------

label medieval:

    hide screen MapUI

    scene expression Transform("bg fase4", fit="cover") with fade

    frank "Olá, [jogador]! Seja bem-vindo ao Universo de Funções e Modularização!"

    jogador "E quem é você?"

    frank "Sou o Mago Frank. Suas funções serão colocadas à prova."

    jogador "Então vamos testar essa magia!"

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

        "DEBUG: Passar direto (100% acertos).":
            jump debug_passar_quiz_medieval

        "DEBUG: Falhar direto (0% acertos).":
            jump debug_falhar_quiz_medieval



# --- LABELS DE DEPURAÇÃO ---
label debug_passar_quiz_medieval:
    $ acertos = perguntas_totais
    jump verificar_resultado_quiz_medieval

label debug_falhar_quiz_medieval:
    $ acertos = 0
    jump verificar_resultado_quiz_medieval



# --------------------------------------------------------
# LÓGICA DO QUIZ - FASE 4
# --------------------------------------------------------

label preparar_quiz_medieval:

    $ acertos = 0

    show screen contador_quiz

    $ mapa_dificuldade = {"easy": "fácil", "normal": "médio", "hard": "difícil"}
    $ chave_dificuldade_atual = mapa_dificuldade[difficulty]

    $ lista_de_perguntas = list(perguntas_fase_4[chave_dificuldade_atual])
    $ random.shuffle(lista_de_perguntas)

    $ perguntas_da_sessao = lista_de_perguntas[:perguntas_totais]

    jump proxima_pergunta_medieval



label proxima_pergunta_medieval:

    if not perguntas_da_sessao:
        jump verificar_resultado_quiz_medieval

    $ pergunta_atual = perguntas_da_sessao[0]

    $ resposta_digitada = ""

    call screen quiz_escrita_screen(pergunta_atual['pergunta'])
    $ resposta_do_jogador = resposta_digitada.strip()

    if not resposta_do_jogador:
        frank "Você precisa escrever algo para eu avaliar sua magia de funções."
        jump proxima_pergunta_medieval

    $ status_resposta, feedback_frank = frank_ai.avaliar_resposta(
        pergunta_atual['pergunta'],
        pergunta_atual['resposta_correta'],
        resposta_do_jogador
    )

    frank "[feedback_frank]"

    if status_resposta == "correta":
        $ acertos += 1
        $ perguntas_da_sessao.pop(0)
        jogador "Minha função foi conjurada com sucesso!"
        jump proxima_pergunta_medieval

    elif status_resposta == "quase":
        jogador "Acho que errei algum detalhe da função..."
        frank "Sua lógica está perto. Ajuste parâmetros, retornos ou sintaxe e tente de novo."
        jump proxima_pergunta_medieval

    else:
        jogador "Ok... essa função bugou."
        frank "Sua magia falhou. Releia a pergunta e pense em como a função deveria ser escrita."
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

    frank "Parabéns, [jogador]! Você dominou as artes das funções e da modularização!"

    jogador "Só mais uma fase e eu posso voltar pra casa!"

    jump hub_controle_5_feliz


## Se não passar

label medieval_triste:

    frank "Ainda não está pronto, mas continue praticando. Funções exigem treino."

    jogador "Eu vou voltar com magia mais forte!"

    jump hub_controle_5_triste



## Fase 1, 2, 3, 4 e 5 liberadas

label hub_controle_5_feliz:

    scene expression Transform("bg hub", fit="cover") with pixellate

    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a última fase!"

    jogador "Vamos lá! Eu vou até o fim!"

    jump hub_mapa


## Fase 1, 2, 3 e 4 liberadas

label hub_controle_5_triste:

    scene expression Transform("bg hub", fit="cover") with pixellate

    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente."

    jogador "Estou quase lá, eu sinto isso. Vou tentar de novo!"

    jump hub_mapa