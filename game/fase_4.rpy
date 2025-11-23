################### FASE 4 ###############################

image bg fase4 = "images/background/bg medieval.png"
image bg hub = "images/background/bg hub.png"
image frank = "images/characters/frank.png"
image frank_erro = "images/characters/frank_erro.png"
image frank_falando = "images/characters/frank_falando.png"
image frank_feliz = "images/characters/frank_feliz.png"

transform frankfit:
    zoom 2

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

# Bloco de inicialização para carregar as perguntas da Fase 4 do JSON.
# init python:
#     import json
#     import random

#     try:
#         with renpy.open_file("quiz_perguntas.json", encoding='utf-8') as f:
#             dados_quiz = json.load(f)

#         perguntas_fase_4 = dados_quiz["Funções e modularização (def, return)"]
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
        perguntas_fase_4 = dados_quiz["Funções e modularização (def, return)"]
    except Exception as e:
        # Se o ficheiro não for encontrado ou tiver um erro, o Ren'Py mostrará uma mensagem clara.
        renpy.error("Falha ao carregar o ficheiro 'quiz_perguntas.json': " + str(e))


label medieval:

    hide screen MapUI

    scene expression Transform("bg fase4", fit="cover") with fade
    show frank_falando at frankfit, center

    frank "Olá, [jogador]! Seja bem-vindo ao Universo de Funções e Modularização!"

    hide frank_falando at frankfit, center
    show frank at frankfit, center

    jogador "E quem é você?"

    hide frank at frankfit, center
    show frank_falando at frankfit, center

    frank "Serei o seu desafiante, caso passe pelos meus desafios, ficará mais próximo de voltar pra casa"

    hide frank_falando at frankfit, center
    show frank_feliz at frankfit, center

    jogador "Aceito seu desafio!"   
    hide frank_feliz at frankfit, center
    hide frank at frankfit, center

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
            jump preparar_quiz_medieval



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

    $ mapa_dificuldade = {"fácil": "fácil", "médio": "médio", "difícil": "difícil"}
    $ chave_dificuldade_atual = mapa_dificuldade[difficulty]
    $ lista_de_perguntas = list(perguntas_fase_4[chave_dificuldade_atual])
    $ random.shuffle(lista_de_perguntas)
    $ perguntas_da_sessao = lista_de_perguntas[:perguntas_totais]
    jump proxima_pergunta_medieval


label proxima_pergunta_medieval:
    if not perguntas_da_sessao:
        jump verificar_resultado_quiz_medieval

    $ pergunta_atual = perguntas_da_sessao.pop(0)
    $ random.shuffle(pergunta_atual['options'])

    call screen quiz_screen(
        question=pergunta_atual['answer'],
        options=pergunta_atual['options']
    )

    $ escolha_do_jogador = _return

    if escolha_do_jogador['text'] == pergunta_atual['answer_correct']:
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
        frank "Incorreto. A resposta certa era: [pergunta_atual['answer_correct']]"
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

    frank "Parabéns, [jogador]! Você dominou as artes das funções e da modularização!"

    jogador "Só mais uma fase e eu posso voltar pra casa!"

    hide frank_feliz at grande, center

    jump hub_controle_5_feliz


## Se não passar

label medieval_triste:

    show frank_erro at grande, center

    frank "Infelizmente você não está pronto, mas você pode tentar novamente!"

    hide frank_erro at grande, center

    jump hub_controle_5_triste



## Fase 1, 2, 3, 4 e 5 liberadas

label hub_controle_5_feliz:

    scene expression Transform("bg hub", fit="cover") with pixellate
    show gilberto_android at Position(xpos=0.35, ypos=0.86, xanchor=0.8, yanchor=1.0)

    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a última fase!"

    jogador "Vamos lá! Eu vou até o fim!"

    jump hub_mapa


## Fase 1, 2, 3 e 4 liberadas

label hub_controle_5_triste:

    scene expression Transform("bg hub", fit="cover") with pixellate
    show gilberto_android at Position(xpos=0.35, ypos=0.86, xanchor=0.8, yanchor=1.0)

    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente."

    jogador "Estou quase lá, eu sinto isso. Vou tentar de novo!"

    jump hub_mapa