################### FASE 4 ###############################

image bg fase4 = "images/background/bg medieval.png"
image bg hub = "images/background/bg hub.png"
image frank = "images/characters/frank.png"
image frank_erro = "images/characters/frank_erro.png"
image frank_falando = "images/characters/frank_falando.png"
image frank_feliz = "images/characters/frank_feliz.png"



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

# Bloco de inicialização para carregar as perguntas da Fase 4 do JSON.
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

    hide screen MapUI

    scene expression Transform("bg fase4", fit="cover") with fade
    show frank_falando at grande, center

    frank "Olá, [jogador]! Seja bem-vindo ao Universo de Funções e Modularização!"

    hide frank_falando at grande, center
    show frank at grande, center

    jogador "E quem é você?"

    hide frank at grande, center
    show frank_falando at grande, center

    frank "Serei o seu desafiante, caso passe pelos meus desafios, ficará mais próximo de voltar pra casa"
   
    hide frank_falando at grande, center
    show frank_feliz at grande, center

    jogador "Aceito seu desafio!"   
    hide frank_feliz at grande, center
    hide frank at grande, center

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

        # "DEBUG: Passar direto (100% acertos).":
        #     jump debug_passar_quiz_medieval

        # "DEBUG: Falhar direto (0% acertos).":
        #     jump debug_falhar_quiz_medieval



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

    $ pergunta_atual = perguntas_da_sessao.pop(0)
    $ random.shuffle(pergunta_atual['opcoes'])

    call screen quiz_screen(
        question=pergunta_atual['pergunta'],
        options=pergunta_atual['opcoes']
    )

    $ escolha_do_jogador = _return

    if escolha_do_jogador == pergunta_atual['resposta_correta']:
        $ acertos += 1
        show frank at grande, center
        jogador "Essa é a resposta. Acertei!"
        hide frank at grande, center
        show frank_feliz at grande, center
        frank "Correto! Próxima pergunta."
        hide frank_feliz at grande, center
    else:
        show frank at grande, center
        jogador "Minha escolha é essa..."
        hide frank at grande, center
        show frank_erro at grande, center
        frank "Incorreto. A resposta certa era: [pergunta_atual['resposta_correta']]"
        hide frank_erro at grande, center

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
    
    show frank_feliz at grande, center

    frank "Parabéns, [jogador]! Você concluiu sua quarta missão no universo"

    jogador "Finalmente! Só mais uma e posso ir pra casa!"

    hide frank_feliz at grande, center

    jump hub_controle_5_feliz


## Se não passar

label medieval_triste:

    show frank_erro at grande, center
    
    frank "Infelizmente você não está pronto, mas você pode tentar novamente!"

    hide frank_erro at grande, center

    jump hub_controle_5_triste


## Fase 1 e 2 e 3 e 4 e 5 liberada

label hub_controle_5_feliz:

    scene expression Transform("bg hub", fit="cover") with pixellate

    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"

    jogador "Pode vir!!"

    jump hub_mapa


## Fase 1 e 2 e 3 e 4 liberada

label hub_controle_5_triste:

    scene expression Transform("bg hub", fit="cover") with pixellate

    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente"

    jogador "Não vou desistir! Estou muito perto de conseguir!"

    jump hub_mapa
