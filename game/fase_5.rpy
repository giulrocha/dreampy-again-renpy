################### FASE 5 ###############################

image bg fase5 = "images/background/bg alienigena.jpg"

# --- TELA CUSTOMIZADA PARA O QUIZ ---
screen quiz_screen(question, options):
    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)

        vbox:
            spacing 20

            text question:
                xalign 0.5

            for option in options:
                textbutton option:
                    xalign 0.5
                    action Return(option)

# Bloco de inicialização para carregar as perguntas da Fase 5 do JSON.
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

    sergio "Olá, [jogador]! Seja bem-vindo ao Universo de Listas e Dicionários!"

    jogador "E quem é você?"

    sergio "Serei o seu desafiante, caso passe pelos meus desafios e lhe darei a jóia necessária para voltar pra casa"

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





## Se passar

label alienigena_feliz:

    $ volta_pra_casa = True

    sergio "Parabéns, [jogador]! Você concluiu sua última missão no universo e merece seu prêmio"

    jogador "Finalmente! Agora posso ir pra casa!"

    jump hub_controle_6_feliz


## Se não passar

label alienigena_triste:

    sergio "Infelizmente você não está pronto, mas você pode tentar novamente!"

    jogador "Nããããããããããoooooo"

    jump hub_controle_6_triste


## Todas as fases liberadas, pode ir pra casa.

label hub_controle_6_feliz:

    android "Parabéns, [jogador]! Você reuniu todas as cinco Jóias de Conhecimento."
    android "Sua mente está restaurada. Você dominou variáveis, lógica, laços, funções e estruturas de dados."
    android "Está pronto para acordar… e enfrentar o verdadeiro desafio."

    jogador "Finalmente!! Estou livreeee!!"
    jogador "Obrigado, android. Eu aprendi que programar é mais do que decorar comandos — é entender como pensar de forma lógica."

    android "Exatamente. Vá, e mostre do que é capaz."

    jump hub_mapa


## Todas as fases liberadas, não pode ir pra casa

label hub_controle_6_triste:
    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente"

    jogador "Nããããããããããoooooo!"

    jogador "Eu estava tão perto!!"

    jump hub_mapa