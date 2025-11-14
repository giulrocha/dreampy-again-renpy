################### FASE 3 ###############################

image bg fase3 = "images/background/bg marinho.png"


# --- TELA CUSTOMIZADA PARA O QUIZ ---
screen quiz_screen(question, options):
    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)

        vbox:
            spacing 20

            text question:
                xalign 0.5  # Centraliza o texto da pergunta

            for option in options:
                textbutton option:
                    xalign 0.5  
                    action Return(option)


# Bloco de inicialização para carregar as perguntas da Fase 3 do JSON.
init python:
    import json
    import random

    # Usamos renpy.open_file() por ser a forma mais segura de abrir ficheiros no Ren'Py.
    try:
        with renpy.open_file("quiz_perguntas.json", encoding='utf-8') as f:
            dados_quiz = json.load(f)

        # Armazenamos apenas as perguntas desta fase numa variável para facilitar o acesso.
        # ** CORREÇÃO APLICADA AQUI **
        perguntas_fase_3 = dados_quiz["Estrutura de repetição (loops for e while)"]
    except Exception as e:
        # Se o ficheiro não for encontrado ou tiver um erro, o Ren'Py mostrará uma mensagem clara.
        renpy.error("Falha ao carregar o ficheiro 'quiz_perguntas.json': " + str(e))


label marinho:

    hide screen MapUI

    scene expression Transform("bg fase3", fit="cover") with fade

    pedro "Olá, [jogador]! Seja bem-vindo ao Universo de Estruturas de Repetição!"

    jogador "E quem é você?"

    pedro "Serei o seu desafiante, caso passe pelos meus desafios e lhe darei a jóia necessária para voltar pra casa"

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


# --- LÓGICA DO QUIZ ---
label preparar_quiz_marinho:
    $ acertos = 0
    $ mapa_dificuldade = {"easy": "fácil", "normal": "médio", "hard": "difícil"}
    $ chave_dificuldade_atual = mapa_dificuldade[difficulty]
    $ lista_de_perguntas = list(perguntas_fase_3[chave_dificuldade_atual])
    $ random.shuffle(lista_de_perguntas)
    $ perguntas_da_sessao = lista_de_perguntas[:perguntas_totais]
    jump proxima_pergunta_marinho


label proxima_pergunta_marinho:
    if not perguntas_da_sessao:
        jump verificar_resultado_quiz_marinho

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
        pedro "Correto! Próxima pergunta."
    else:
        jogador "Minha escolha é essa..."
        pedro "Incorreto. A resposta certa era: [pergunta_atual['resposta_correta']]"

    jump proxima_pergunta_marinho


label verificar_resultado_quiz_marinho:
    if acertos >= acertos_para_passar:
        jump marinho_feliz
    else:
        jump marinho_triste


## Se passar

label marinho_feliz:

    $ fase_4_liberada = True

    pedro "Parabéns, [jogador]! Você concluiu sua terceira missão no universo e merece seu prêmio"

    jogador "Finalmente! Falta pouco!"

    jump hub_controle_4_feliz


## Se não passar

label marinho_triste:

    pedro "Infelizmente você não está pronto, mas você pode tentar novamente!"

    jump hub_controle_4_triste


## Fase 1 e 2 e 3 e 4 liberada

label hub_controle_4_feliz:

    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"

    jogador "Pode vir! Estou muito perto do meu objetivo!"

    jump hub_mapa


## Fase 1 e 2 e 3 liberada
 
label hub_controle_4_triste:

    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente"

    jogador "Não vou desistir! Estou muito perto de conseguir!"

    jump hub_mapa