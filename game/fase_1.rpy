################### FASE 1 ###############################

image bg fase1 = "images/background/bg digital.png"

# --- TELA CUSTOMIZADA PARA O QUIZ ---
screen quiz_screen(question, options):
    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)

        vbox:
            spacing 20  # Espaço entre a pergunta e as alternativas

            # O Texto da Pergunta
            text question:
                xalign 0.5  # Centraliza o texto da pergunta

            # As Alternativas como Botões
            for option in options:
                textbutton option:
                    xalign 0.5  # Centraliza os botões
                    action Return(option)


# Bloco de inicialização para carregar as perguntas da Fase 1
init python:
    import json
    import random

    try:
        with renpy.open_file("quiz_perguntas.json", encoding='utf-8') as f:
            dados_quiz = json.load(f)

        # Armazenamos apenas as perguntas desta fase numa variável para facilitar o acesso.
        perguntas_fase_1 = dados_quiz["Valores, Tipos de Dados, Variáveis, Nomes de Variáveis, Palavras-chave"]
    except Exception as e:
        # Se o ficheiro não for encontrado ou tiver um erro, o Ren'Py mostrará uma mensagem clara.
        renpy.error("Falha ao carregar o ficheiro 'quiz_perguntas.json': " + str(e))



label digital:

    hide screen MapUI

    # scene bg fase1 with fade

    scene expression Transform("bg fase1", fit="cover") with fade

    raimundo "Olá, [jogador]! Seja bem-vindo ao Universo de Variáveis!"

    jogador "Quem é você??"

    raimundo "Serei o seu desafiante, caso passe pelos meus desafios e lhe darei a jóia necessária para voltar pra casa"

    jogador "Aceito seu desafio!"

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
    # Este menu permite pular o quiz para fins de teste.
    menu:
        "Iniciar o questionário normalmente.":
            # Pula para a preparação normal do quiz. [cite: 10]
            jump preparar_quiz_digital
            
        "DEBUG: Passar direto (100% acertos).":
            # Pula para uma rotina que força a vitória.
            jump debug_passar_quiz
            
        "DEBUG: Falhar direto (0% acertos).":
            # Pula para uma rotina que força a derrota.
            jump debug_falhar_quiz

# --- LABELS DE DEPURAÇÃO ---
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
    # Primeiro, verifica se a lista de perguntas da sessão já esvaziou
    if not perguntas_da_sessao:
        # Se sim, o quiz terminou. Verifica o resultado.
        jump verificar_resultado_quiz

    # Pega a próxima pergunta da lista e, ao mesmo tempo, a remove
    $ pergunta_atual = perguntas_da_sessao.pop(0)

    # Embaralha as opções de resposta para que não apareçam sempre na mesma ordem
    $ random.shuffle(pergunta_atual['opcoes'])

    # Chamamos a nova tela, passando a pergunta e as opções atuais.
    call screen quiz_screen(
        question=pergunta_atual['pergunta'],
        options=pergunta_atual['opcoes']
    )

    # O valor da escolha do jogador é guardado na variável especial '_return'.
    $ escolha_do_jogador = _return

    # Agora, verifica se a escolha foi correta
    if escolha_do_jogador == pergunta_atual['resposta_correta']:
        $ acertos += 1
        jogador "A resposta é essa. Acho que acertei!"
        raimundo "Correto! Vamos para a próxima."
    else:
        jogador "Vou escolher esta..."
        raimundo "Incorreto. A resposta certa era: [pergunta_atual['resposta_correta']]"

    # Após responder, volta ao início do loop para pegar a próxima pergunta
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

    jogador "Finalmente!"

    jump hub_controle_2_feliz


## Se não passar

label digital_triste:

    raimundo "Infelizmente você não está pronto, mas você pode tentar novamente!"

    jump hub_controle_2_triste


## Fase 1 e 2 liberada

label hub_controle_2_feliz:

    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"

    jogador "Pode vir! Estou pronto"

    jump hub_mapa


## Fase 1 liberada

label hub_controle_2_triste:

    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente"

    jogador "Não vou desistir!"

    jump hub_mapa