# ################### FASE 1 ###############################

# --- CORREÇÃO (PARTE 1) ---
# Declaramos a imagem de fundo com um nome simples ("bg fase1").
# Esta linha deve ficar fora de qualquer label.
image bg fase1 = "images/background/fase1.jpg"

# --- TELA CUSTOMIZADA PARA O QUIZ ---
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
            spacing 20  # Espaço entre a pergunta e as alternativas

            # 1. O Texto da Pergunta
            # Exibe a pergunta recebida pela tela.
            text question:
                xalign 0.5  # Centraliza o texto da pergunta

            # 2. As Alternativas como Botões
            # Cria um botão para cada opção na lista de 'options'.
            for option in options:
                textbutton option:
                    xalign 0.5  # Centraliza os botões
                    # A ação 'Return(option)' faz com que a tela seja fechada
                    # e o texto do botão seja retornado como resultado.
                    action Return(option)


# Bloco de inicialização para carregar as perguntas do JSON uma vez, no início do jogo.
init python:
    import json
    import random

    # Usamos renpy.open_file() por ser a forma mais segura de abrir ficheiros no Ren'Py.
    try:
        with renpy.open_file("quiz_perguntas.json", encoding='utf-8') as f:
            dados_quiz = json.load(f)

        # Armazenamos apenas as perguntas desta fase numa variável para facilitar o acesso.
        perguntas_fase_1 = dados_quiz["Valores, Tipos de Dados, Variáveis, Nomes de Variáveis, Palavras-chave"]
    except Exception as e:
        # Se o ficheiro não for encontrado ou tiver um erro, o Ren'Py mostrará uma mensagem clara.
        renpy.error("Falha ao carregar o ficheiro 'quiz_perguntas.json': " + str(e))


label digital:
    # Esconde a tela do mapa que estava visível.
    hide screen MapUI

    # Agora usamos o nome simples que definimos acima.
    scene bg fase1 with fade

    # Diálogo inicial (mantido do seu script original)
    raimundo "Olá, [jogador]! Seja bem-vindo ao Universo de Variáveis!"
    jogador "Quem é você??"
    raimundo "Serei o seu desafiante, caso passe pelos meus desafios e lhe darei a jóia necessária para voltar pra casa"
    jogador "Aceito seu desafio!"
    
    # Definição das regras (mantido do seu script original)
    if difficulty == "easy":
        $ perguntas_totais = 10
        $ acertos_para_passar = 7
    elif difficulty == "normal":
        $ perguntas_totais = 10
        $ acertos_para_passar = 7
    else: # difficulty == "hard"
        $ perguntas_totais = 10
        $ acertos_para_passar = 7


    # --- NOVO: MENU DE DEPURAÇÃO ---
    # Este menu permite pular o quiz para fins de teste.
    menu:
        "Iniciar o questionário normalmente.":
            # [cite_start]Pula para a preparação normal do quiz. [cite: 10]
            jump preparar_quiz_digital
            
        "DEBUG: Passar direto (100% acertos).":
            # Pula para uma rotina que força a vitória.
            jump debug_passar_quiz
            
        "DEBUG: Falhar direto (0% acertos).":
            # Pula para uma rotina que força a derrota.
            jump debug_falhar_quiz


# --- NOVOS LABELS DE DEPURAÇÃO ---
label debug_passar_quiz:
    # Define os acertos como o máximo possível para garantir a vitória.
    $ acertos = perguntas_totais
    # Pula diretamente para a verificação de resultados.
    jump verificar_resultado_quiz

label debug_falhar_quiz:
    # Define os acertos como zero para garantir a derrota.
    $ acertos = 0
    # Pula diretamente para a verificação de resultados.
    jump verificar_resultado_quiz


label preparar_quiz_digital:
    # Inicia o contador de acertos para esta tentativa
    $ acertos = 0

    # Mapeia a dificuldade do jogo para as chaves do JSON
    $ mapa_dificuldade = {"easy": "fácil", "normal": "médio", "hard": "difícil"}
    $ chave_dificuldade_atual = mapa_dificuldade[difficulty]

    # Pega a lista de perguntas da dificuldade correta
    $ lista_de_perguntas = list(perguntas_fase_1[chave_dificuldade_atual])

    # Embaralha as perguntas para que a ordem seja aleatória
    $ random.shuffle(lista_de_perguntas)

    # Seleciona apenas o número de perguntas que vamos usar na rodada
    $ perguntas_da_sessao = lista_de_perguntas[:perguntas_totais]

    # Inicia o loop do quiz
    jump proxima_pergunta


label proxima_pergunta:
    # Primeiro, verificamos se a lista de perguntas da sessão já esvaziou
    if not perguntas_da_sessao:
        # Se sim, o quiz terminou. [cite_start]Vamos verificar o resultado. [cite: 12]
        jump verificar_resultado_quiz

    # Pega a próxima pergunta da lista e, ao mesmo tempo, a remove
    $ pergunta_atual = perguntas_da_sessao.pop(0)

    # Embaralha as opções de resposta para que não apareçam sempre na mesma ordem
    $ random.shuffle(pergunta_atual['opcoes'])

    # Chamamos a nossa nova tela, passando a pergunta e as opções atuais.
    call screen quiz_screen(
        question=pergunta_atual['pergunta'],
        options=pergunta_atual['opcoes']
    )

    # O valor da escolha do jogador é guardado na variável especial '_return'.
    $ escolha_do_jogador = _return

    # Agora, verificamos se a escolha foi correta
    if escolha_do_jogador == pergunta_atual['resposta_correta']:
        $ acertos += 1
        jogador "A resposta é essa. Acho que acertei!"
        raimundo "Correto! Vamos para a próxima."
    else:
        jogador "Vou escolher esta..."
        raimundo "Incorreto. A resposta certa era: [pergunta_atual['resposta_correta']]"

    # Após responder, voltamos ao início do loop para pegar a próxima pergunta
    jump proxima_pergunta


label verificar_resultado_quiz:
    # Esta verificação SÓ acontece DEPOIS de todas as perguntas terem sido respondidas
    if acertos >= acertos_para_passar:
        jump digital_feliz
    else:
        jump digital_triste


### Se passar
label digital_feliz:
    $ fase_2_liberada = True
    raimundo "Parabéns, [jogador]! Você concluiu sua primeira missão no universo e merece seu prêmio"
    #mostra a joia la
    jogador "Finalmente!"
    jump hub_controle_2_feliz


## Se não passar
label digital_triste:
    raimundo "Infelizmente você não está pronto, mas você pode tentar novamente!"
    #corta pro hub
    jump hub_controle_2_triste


## Fase 1 e 2 liberada
label hub_controle_2_feliz:
    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"
    jogador "Pode vir! Estou pronto"
    # MUDANÇA IMPORTANTE: Salta de volta para o hub do mapa
    jump hub_mapa


## Fase 1 liberada (mas não passou)
label hub_controle_2_triste:
    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente"
    jogador "Não vou desistir!"
    # MUDANÇA IMPORTANTE: Salta de volta para o hub do mapa
    jump hub_mapa