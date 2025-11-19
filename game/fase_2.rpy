################### FASE 2 ###############################

image bg fase2 = "images/background/bg cyberpunk.png"
image bg hub = "images/background/bg hub.png"


# --------------------------------------------------------
# CARREGANDO PERGUNTAS FASE 2
# --------------------------------------------------------
init python:
    import json
    import random
    import vanilton_ai

    try:
        with renpy.open_file("quiz_perguntas.json", encoding='utf-8') as f:
            dados_quiz = json.load(f)

        # Chave exatamente como está no JSON
        perguntas_fase_2 = dados_quiz["Lógica e estruturas condicionais (if, else, elif)"]

    except Exception as e:
        renpy.error("Falha ao carregar as perguntas da Fase 2 do 'quiz_perguntas.json': " + str(e))



# --------------------------------------------------------
# INÍCIO DA FASE 2 - CYBERPUNK
# --------------------------------------------------------

label cyberpunk:

    hide screen MapUI

    scene expression Transform("bg fase2", fit="cover") with fade

    vanilton "Olá, [jogador]! Seja bem-vindo ao Universo de Lógica e Estruturas Condicionais!"

    jogador "E quem é você?"

    vanilton "Sou Vanilton. Vou testar se sua lógica é forte o suficiente para continuar."

    jogador "Pode mandar, eu aceito o desafio!"

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

        "DEBUG: Passar direto (100% acertos).":
            jump debug_passar_quiz_cyberpunk

        "DEBUG: Falhar direto (0% acertos).":
            jump debug_falhar_quiz_cyberpunk



# --- LABELS DE DEPURAÇÃO ---
label debug_passar_quiz_cyberpunk:
    $ acertos = perguntas_totais
    jump verificar_resultado_quiz_cyberpunk

label debug_falhar_quiz_cyberpunk:
    $ acertos = 0
    jump verificar_resultado_quiz_cyberpunk



# --------------------------------------------------------
# LÓGICA DO QUIZ - FASE 2
# --------------------------------------------------------

label preparar_quiz_cyberpunk:

    $ acertos = 0

    show screen contador_quiz

    $ mapa_dificuldade = {"easy": "fácil", "normal": "médio", "hard": "difícil"}
    $ chave_dificuldade_atual = mapa_dificuldade[difficulty]

    $ lista_de_perguntas = list(perguntas_fase_2[chave_dificuldade_atual])
    $ random.shuffle(lista_de_perguntas)

    $ perguntas_da_sessao = lista_de_perguntas[:perguntas_totais]

    jump proxima_pergunta_cyberpunk



label proxima_pergunta_cyberpunk:

    if not perguntas_da_sessao:
        jump verificar_resultado_quiz_cyberpunk

    # Pega a primeira pergunta da fila (sem embaralhar mais)
    $ pergunta_atual = perguntas_da_sessao[0]

    # Limpa o texto anterior
    $ resposta_digitada = ""

    # Chama a tela global de resposta aberta
    call screen quiz_escrita_screen(pergunta_atual['pergunta'])

    # Coleta o que foi digitado
    $ resposta_do_jogador = resposta_digitada.strip()

    if not resposta_do_jogador:
        vanilton "Você precisa digitar alguma coisa para eu avaliar a sua lógica."
        jump proxima_pergunta_cyberpunk

    # IA DO VANILTON
    $ status_resposta, feedback_vanilton = vanilton_ai.avaliar_resposta(
        pergunta_atual['pergunta'],
        pergunta_atual['resposta_correta'],
        resposta_do_jogador
    )

    vanilton "[feedback_vanilton]"

    if status_resposta == "correta":
        $ acertos += 1
        $ perguntas_da_sessao.pop(0)
        jogador "Minha lógica está afiada! Próxima."
        jump proxima_pergunta_cyberpunk

    elif status_resposta == "quase":
        jogador "Acho que estou quase entendendo..."
        vanilton "Você está perto, ajuste um pouco sua condição."
        jump proxima_pergunta_cyberpunk

    else:  # errada
        jogador "Hmm... essa não foi."
        vanilton "Sua condição não está certa ainda. Leia a pergunta com atenção e tente de novo."
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

    vanilton "Parabéns, [jogador]! Sua lógica passou nos meus testes."

    jogador "Ótimo, mais um passo pra casa!"

    jump hub_controle_3_feliz



## Se não passar

label cyberpunk_triste:

    vanilton "Você ainda não domina bem as estruturas condicionais. Mas pode tentar de novo."

    jogador "Não vou desistir. Vou ajustar minha lógica!"

    jump hub_controle_3_triste



## Fase 1, 2 e 3 liberada

label hub_controle_3_feliz:

    scene expression Transform("bg hub", fit="cover") with pixellate

    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"

    jogador "Pode vir a próxima. Estou pronto!"

    jump hub_mapa



## Fase 1 e 2 liberadas

label hub_controle_3_triste:

    scene expression Transform("bg hub", fit="cover") with pixellate

    android "Que pena [jogador], mas você pode tentar novamente."

    jogador "Eu volto mais forte!"

    jump hub_mapa
