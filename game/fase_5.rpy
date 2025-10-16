# ################### FASE 5 ###############################

# --- PERSONAGEM ---
# Define o personagem 'Zorg' para esta fase.
define zorg = Character("Zorg")

# --- IMAGEM DE FUNDO ---
# Declaração da imagem de fundo para a fase 5.
image bg fase5 = "images/background/fase5.jpg"

# --- TELA CUSTOMIZADA PARA O QUIZ (Replicada das fases anteriores) ---
# Esta tela exibe uma pergunta e uma lista de opções como botões.
screen quiz_screen(question, options):
    # Usamos um frame para agrupar os elementos do quiz.
    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)

        # Organiza os elementos verticalmente.
        vbox:
            spacing 20

            # 1. O Texto da Pergunta
            text question:
                xalign 0.5

            # 2. As Alternativas como Botões
            for option in options:
                textbutton option:
                    xalign 0.5
                    action Return(option)

# Bloco de inicialização para carregar as perguntas do JSON.
init python:
    import json
    import random

    try:
        with renpy.open_file("quiz_perguntas.json", encoding='utf-8') as f:
            dados_quiz = json.load(f)

        # Armazena as perguntas desta fase numa variável.
        perguntas_fase_5 = dados_quiz["Listas e Dicionários (criação, acesso, métodos básicos)."]
    except Exception as e:
        renpy.error("Falha ao carregar 'quiz_perguntas.json': " + str(e))


label alienigena:
    # Esconde a tela do mapa.
    hide screen MapUI

    # Define a imagem de fundo da fase 5.
    scene bg fase5 with fade

    # Diálogo inicial
    zorg "Olá, [jogador]! Seja bem-vindo ao Universo de Listas e Dicionários!"
    jogador "E quem é você?"
    zorg "Serei seu último desafiante. Se passar pelos meus desafios, terá a joia final para voltar pra casa."
    jogador "Aceito seu desafio!"

    # Definição das regras
    if difficulty == "easy":
        $ perguntas_totais = 10
        $ acertos_para_passar = 7
    elif difficulty == "normal":
        $ perguntas_totais = 10
        $ acertos_para_passar = 7
    else: # difficulty == "hard"
        $ perguntas_totais = 10
        $ acertos_para_passar = 7

    # --- MENU DE DEPURAÇÃO ---
    menu:
        "Iniciar o questionário normalmente.":
            jump preparar_quiz_alienigena

        "DEBUG: Passar direto (100% acertos).":
            jump debug_passar_quiz_alienigena

        "DEBUG: Falhar direto (0% acertos).":
            jump debug_falhar_quiz_alienigena


# --- LABELS DE DEPURAÇÃO ---
label debug_passar_quiz_alienigena:
    $ acertos = perguntas_totais
    jump verificar_resultado_quiz_alienigena

label debug_falhar_quiz_alienigena:
    $ acertos = 0
    jump verificar_resultado_quiz_alienigena


# --- LÓGICA DO QUIZ ---
label preparar_quiz_alienigena:
    $ acertos = 0
    $ mapa_dificuldade = {"easy": "fácil", "normal": "médio", "hard": "difícil"}
    $ chave_dificuldade_atual = mapa_dificuldade[difficulty]
    $ lista_de_perguntas = list(perguntas_fase_5[chave_dificuldade_atual])
    $ random.shuffle(lista_de_perguntas)
    $ perguntas_da_sessao = lista_de_perguntas[:perguntas_totais]
    jump proxima_pergunta_alienigena


label proxima_pergunta_alienigena:
    if not perguntas_da_sessao:
        jump verificar_resultado_quiz_alienigena

    $ pergunta_atual = perguntas_da_sessao.pop(0)
    $ random.shuffle(pergunta_atual['opcoes'])

    call screen quiz_screen(
        question=pergunta_atual['pergunta'],
        options=pergunta_atual['opcoes']
    )

    $ escolha_do_jogador = _return

    if escolha_do_jogador == pergunta_atual['resposta_correta']:
        $ acertos += 1
        jogador "Essa é a resposta. Acertei!"
        zorg "Correto! Próxima pergunta."
    else:
        jogador "Minha escolha é essa..."
        zorg "Incorreto. A resposta certa era: [pergunta_atual['resposta_correta']]"

    jump proxima_pergunta_alienigena


label verificar_resultado_quiz_alienigena:
    if acertos >= acertos_para_passar:
        jump alienigena_feliz
    else:
        jump alienigena_triste


# Se passar
label alienigena_feliz:
    $ volta_pra_casa = True
    zorg "Parabéns, [jogador]! Você concluiu sua última missão no universo e merece seu prêmio."
    # mostra a joia la
    jogador "Finalmente! Agora posso ir pra casa!"
    jump hub_controle_6_feliz


# Se não passar
label alienigena_triste:
    zorg "Infelizmente você não está pronto, mas pode tentar novamente!"
    jogador "Nããããããããããoooooo"
    # corta pro hub
    jump hub_controle_6_triste


# Rota para o final feliz
label hub_controle_6_feliz:
    android "Parabéns, [jogador]! Você reuniu todas as cinco Jóias de Conhecimento."
    android "Sua mente está restaurada. Você dominou variáveis, lógica, laços, funções e estruturas de dados."
    android "Está pronto para acordar… e enfrentar o verdadeiro desafio."
    jogador "Finalmente!! Estou livreeee!!"
    jogador "Obrigado, android. Eu aprendi que programar é mais do que decorar comandos — é entender como pensar de forma lógica."
    android "Exatamente. Vá, e mostre do que é capaz."
    # Ação final, pode ser um jump para o menu principal ou para uma tela de créditos
    # Por enquanto, retorna ao mapa.
    jump hub_mapa


# Rota para o hub se o jogador falhar na última fase
label hub_controle_6_triste:
    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente."
    jogador "Nããããããããããoooooo!"
    jogador "Eu estava tão perto!!"
    # Retorna ao mapa para o jogador tentar novamente.
    jump hub_mapa