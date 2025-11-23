################### FASE 5 ###############################

image bg fase5 = "images/background/bg alienigena.png"
image bg hub = "images/background/bg hub.png"
image sergio = "images/characters/sergio.png"
image sergio_erro = "images/characters/sergio_erro.png"
image sergio_falando = "images/characters/sergio_falando.png"
image sergio_feliz = "images/characters/sergio_feliz.png"
image gilberto_android = "images/characters/gilberto_android.png"

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
                textbutton option["text"]:
                    action Return(option)

# Bloco de inicialização para carregar as perguntas da Fase 5 do JSON.
# init python:
#     import json
#     import random

#     try:
#         with renpy.open_file("quiz_perguntas.json", encoding='utf-8') as f:
#             dados_quiz = json.load(f)

#         perguntas_fase_5 = dados_quiz["Listas e Dicionários (criação, acesso, métodos básicos)"]
#     except Exception as e:
#         renpy.error("Falha ao carregar 'quiz_perguntas.json': " + str(e))


init python:
    import json
    import random
    import requests

    API_URL = 'http://10.177.250.32:8000/api/core/quiz/'

    r = requests.get(API_URL)
    print(r.json())

    def pegar_texto():
        try:
            r = requests.get(API_URL)
            return r.json()
        except Exception as e:
            return f"Erro ao buscar dados.{e}"

    try:
        dados_quiz = pegar_texto()

        # Armazenamos apenas as perguntas desta fase numa variável para facilitar o acesso.
        perguntas_fase_5 = dados_quiz["Listas e Dicionários (criação, acesso, métodos básicos)"]
    except Exception as e:
        # Se o ficheiro não for encontrado ou tiver um erro, o Ren'Py mostrará uma mensagem clara.
        renpy.error("Falha ao carregar o ficheiro 'quiz_perguntas.json': " + str(e))

label alienigena:

    scene expression Transform("bg fase5", fit="cover") with fade
    show sergio_falando at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    sergio "Olá, [jogador]! Seja bem-vindo ao Universo de Listas e Dicionários!"

    hide sergio_falando at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)
    show sergio at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    jogador "E quem é você?"

    hide sergio at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)
    show sergio_falando at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    sergio "Sou Sérgio, o Alien das Estruturas de Dados. Se passar pelos meus desafios, poderá voltar pra casa."

    hide sergio_falando at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)
    show sergio_feliz at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    jogador "Então vamos terminar isso!"

    hide sergio_feliz at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    if difficulty == "fácil":
        $ perguntas_totais = 10
        $ acertos_para_passar = 7

    elif difficulty == "médio":
        $ perguntas_totais = 10
        $ acertos_para_passar = 7

    else:
        $ perguntas_totais = 10
        $ acertos_para_passar = 7

    # --- MENU DE DEPURAÇÃO ---
    menu:
        "Iniciar o questionário normalmente.":
            jump preparar_quiz_alienigena



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

    show screen contador_quiz

    $ mapa_dificuldade = {"fácil": "fácil", "médio": "médio", "difícil": "difícil"}
    $ chave_dificuldade_atual = mapa_dificuldade[difficulty]
    $ lista_de_perguntas = list(perguntas_fase_5[chave_dificuldade_atual])
    $ random.shuffle(lista_de_perguntas)
    $ perguntas_da_sessao = lista_de_perguntas[:perguntas_totais]
    jump proxima_pergunta_alienigena


label proxima_pergunta_alienigena:
    if not perguntas_da_sessao:
        jump verificar_resultado_quiz_alienigena

    $ pergunta_atual = perguntas_da_sessao.pop(0)
    $ random.shuffle(pergunta_atual['options'])

    call screen quiz_screen(
        question=pergunta_atual['answer'],
        options=pergunta_atual['options']
    )

    $ escolha_do_jogador = _return

    if escolha_do_jogador['text'] == pergunta_atual['answer_correct']:
        $ acertos += 1
        show sergio at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)
        jogador "Essa é a resposta. Acertei!"
        hide sergio at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)
        show sergio_feliz at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)
        sergio "Correto! Próxima pergunta."
        hide sergio_feliz at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)
    else:
        show sergio at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)
        jogador "Minha escolha é essa..."
        hide sergio at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)
        show sergio_erro at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)
        sergio "Incorreto. A resposta certa era: [pergunta_atual['answer_correct']]"
        hide sergio_erro at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    jump proxima_pergunta_alienigena


label verificar_resultado_quiz_alienigena:

    hide screen contador_quiz

    if acertos >= acertos_para_passar:
        jump alienigena_feliz
    else:
        jump alienigena_triste



## Se passar

label alienigena_feliz:

    $ volta_pra_casa = True

    show sergio_feliz at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    sergio "INCRÍVEL, [jogador]! Você dominou as estruturas de dados do universo!"

    jogador "Finalmente… eu consegui! Posso voltar pra casa!"

    hide sergio_feliz at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    jump hub_controle_6_feliz


## Se não passar

label alienigena_triste:

    show sergio_erro at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    sergio "Ainda não. Mas não desista, você está perto de dominar tudo."

    jogador "Nãããããããooo! Mas eu volto melhor."

    hide sergio_erro at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    jump hub_controle_6_triste


## Todas as fases liberadas, pode ir pra casa.

label hub_controle_6_feliz:

    scene expression Transform("bg hub", fit="cover") with pixellate
    show gilberto_android at Position(xpos=0.35, ypos=0.86, xanchor=0.8, yanchor=1.0)

    android "Parabéns, [jogador]! Você completou todos os desafios dos cinco universos."
    android "Sua mente foi restaurada. Você domina variáveis, lógica, laços, funções e estruturas de dados."
    android "Está pronto para acordar… e enfrentar o verdadeiro desafio."

    jogador "Obrigado! Agora eu sei programar de verdade."

    jump hub_mapa


## Todas as fases liberadas, não pode ir pra casa

label hub_controle_6_triste:

    scene expression Transform("bg hub", fit="cover") with pixellate
    show gilberto_android at Position(xpos=0.35, ypos=0.86, xanchor=0.8, yanchor=1.0)

    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente."

    jogador "Eu estava tão perto!! Mas vou voltar ainda mais forte."

    jump hub_mapa