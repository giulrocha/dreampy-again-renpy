# ################### FASE 1 ###############################

# Bloco de inicialização para carregar as perguntas do JSON uma vez, no início do jogo.
init python:
    import json
    import random

    # Usamos renpy.open_file() por ser a forma mais segura de abrir ficheiros no Ren'Py
    try:
        with renpy.open_file("quiz_perguntas.json", encoding='utf-8') as f:
            dados_quiz = json.load(f)

        # Armazenamos apenas as perguntas desta fase numa variável para facilitar o acesso.
        perguntas_fase_1 = dados_quiz["Valores, Tipos de Dados, Variáveis, Nomes de Variáveis, Palavras-chave"]
    except Exception as e:
        # Se o ficheiro não for encontrado ou tiver um erro, o Ren'Py mostrará uma mensagem clara.
        renpy.error("Falha ao carregar o ficheiro 'quiz_perguntas.json': " + str(e))


label digital:
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

    # Pula para a preparação do quiz
    jump preparar_quiz_digital


label preparar_quiz_digital:
    # Inicia o contador de acertos para esta tentativa
    $ acertos = 0

    # Mapeia a dificuldade do jogo ("normal") para as chaves do JSON ("médio")
    $ mapa_dificuldade = {"easy": "fácil", "normal": "médio", "hard": "difícil"}
    $ chave_dificuldade_atual = mapa_dificuldade[difficulty]

    # Pega a lista de perguntas da dificuldade correta
    $ lista_de_perguntas = list(perguntas_fase_1[chave_dificuldade_atual])

    # Embaralha as perguntas para que a ordem seja aleatória a cada jogo
    $ random.shuffle(lista_de_perguntas)

    # Seleciona apenas o número de perguntas que vamos usar na rodada
    $ perguntas_da_sessao = lista_de_perguntas[:perguntas_totais]

    # Inicia o loop do quiz
    jump proxima_pergunta


label proxima_pergunta:
    # Primeiro, verificamos se a lista de perguntas da sessão já esvaziou
    if not perguntas_da_sessao:
        # Se sim, o quiz terminou. Vamos verificar o resultado.
        jump verificar_resultado_quiz

    # Pega a próxima pergunta da lista e, ao mesmo tempo, a remove
    $ pergunta_atual = perguntas_da_sessao.pop(0)

    # Mostra a pergunta na tela
    raimundo "[pergunta_atual['pergunta']]"

    # Embaralha as opções de resposta para que não apareçam sempre na mesma ordem
    $ random.shuffle(pergunta_atual['opcoes'])

    # --- O Coração do Quiz: A Correção Definitiva ---
    python:
        # Criamos uma lista de opções no formato que o Ren'Py entende para menus dinâmicos
        opcoes_para_menu = []
        for opcao in pergunta_atual['opcoes']:
            opcoes_para_menu.append( (opcao, opcao) ) # Formato: (Texto da Opção, Valor de Retorno)

        # A função renpy.display_menu mostra o menu e espera o jogador escolher.
        # A escolha do jogador é então armazenada na variável.
        escolha_do_jogador = renpy.display_menu(opcoes_para_menu)

    # Agora, fora do bloco python, verificamos se a escolha foi correta
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