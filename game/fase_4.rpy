# ################### FASE 4 ###############################

# --- PERSONAGEM ---
# Define o personagem 'Merlin' para esta fase.
define merlin = Character("Merlin")

# --- IMAGEM DE FUNDO ---
# Declaração da imagem de fundo para a fase 4.
image bg fase4 = "images/background/fase4.jpg"

# --- TELA CUSTOMIZADA PARA O QUIZ (Replicada da Fase 3) ---
# Esta tela exibe uma pergunta e uma lista de opções como botões.
screen quiz_screen(question, options):
    # Usamos um frame para agrupar os elementos do quiz com um fundo semi-transparente.
    frame:
        # Alinha o frame no centro da tela
        xalign 0.5
        yalign 0.5
        # Define um preenchimento interno para não colar nas bordas
        padding (30, 30)

        # Organiza os elementos verticalmente
        vbox:
            spacing 20

            # 1. O Texto da Pergunta
            text question:
                xalign 0.5  # Centraliza o texto da pergunta

            # 2. As Alternativas como Botões
            for option in options:
                textbutton option:
                    xalign 0.5  # Centraliza os botões
                    # A ação 'Return(option)' fecha a tela e retorna o texto do botão.
                    action Return(option)

# Bloco de inicialização para carregar as perguntas do JSON.
init python:
    import json
    import random

    try:
        with renpy.open_file("quiz_perguntas.json", encoding='utf-8') as f:
            dados_quiz = json.load(f)

        # Armazena as perguntas desta fase numa variável.
        perguntas_fase_4 = dados_quiz["Funções e modularização (def, return)"]
    except Exception as e:
        renpy.error("Falha ao carregar 'quiz_perguntas.json': " + str(e))


label medieval:
    # Esconde a tela do mapa que estava visível.
    hide screen MapUI

    # Define a imagem de fundo da fase 4.
    scene bg fase4 with fade

    # Diálogo inicial
    merlin "Olá, [jogador]! Seja bem-vindo ao Universo de Funções e Modularização!"
    jogador "E quem é você?"
    merlin "Serei o seu desafiante. Se passar pelos meus desafios, lhe darei a joia necessária para voltar pra casa."
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


# --- LÓGICA DO QUIZ ---
label preparar_quiz_medieval:
    $ acertos = 0
    $ mapa_dificuldade = {"easy": "fácil", "normal": "médio", "hard": "difícil"}
    $ chave_dificuldade_atual = mapa_dificuldade[difficulty]
    $ lista_de_perguntas = list(perguntas_fase_4[chave_dificuldade_atual])
    $ random.shuffle(lista_de_perguntas)
    $ perguntas_da_sessao = lista_de_perguntas[:perguntas_totais]
    jump proxima_pergunta_medieval


label proxima_pergunta_medieval:
    if not perguntas_da_sessao:
        jump verificar_resultado_quiz_medieval

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
        merlin "Correto! Próxima pergunta."
    else:
        jogador "Minha escolha é essa..."
        merlin "Incorreto. A resposta certa era: [pergunta_atual['resposta_correta']]"

    jump proxima_pergunta_medieval


label verificar_resultado_quiz_medieval:
    if acertos >= acertos_para_passar:
        jump medieval_feliz
    else:
        jump medieval_triste


# Se passar
label medieval_feliz:
    $ fase_5_liberada = True
    merlin "Parabéns, [jogador]! Você concluiu sua quarta missão no universo e merece seu prêmio."
    # mostra a joia la
    jogador "Finalmente! Só mais uma e posso ir pra casa!"
    jump hub_controle_5_feliz


# Se não passar
label medieval_triste:
    merlin "Infelizmente você não está pronto, mas pode tentar novamente!"
    # corta pro hub
    jump hub_controle_5_triste


# Rota para o hub se o jogador passar
label hub_controle_5_feliz:
    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"
    jogador "Pode vir!!"
    jump hub_mapa


# Rota para o hub se o jogador falhar
label hub_controle_5_triste:
    android "Que pena [jogador], não foi dessa vez. Mas você pode tentar novamente."
    jogador "Não vou desistir! Estou muito perto de conseguir!"
    jump hub_mapa