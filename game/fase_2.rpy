################### FASE 2 ###############################

image bg fase2 = "images/background/bg cyberpunk.png"
image bg hub = "images/background/bg hub.png"
image vanilton = "images/characters/vanilton.png"
image gilberto_android = "images/characters/gilberto_android.png"

transform grande: 
    zoom 2.3

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

            for option in options:
                textbutton option["text"]:
                    action Return(option)



# Bloco de inicialização para carregar as perguntas da Fase 2 do JSON.
# init python:
#     import json
#     import random

#     try:
#         if 'dados_quiz' not in globals():
#             with renpy.open_file("quiz_perguntas.json", encoding='utf-8') as f:
#                 dados_quiz = json.load(f)

#         # Chave exatamente como está no JSON
#         perguntas_fase_2 = dados_quiz["Lógica e estruturas condicionais (if, else, elif)"]

#     except Exception as e:
#         renpy.error("Falha ao carregar as perguntas da Fase 2 do 'quiz_perguntas.json': " + str(e))

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
        perguntas_fase_2 = dados_quiz["Lógica e estruturas condicionais (if, else, elif)"]
    except Exception as e:
        # Se o ficheiro não for encontrado ou tiver um erro, o Ren'Py mostrará uma mensagem clara.
        renpy.error("Falha ao carregar o ficheiro 'quiz_perguntas.json': " + str(e))



label cyberpunk:

    hide screen MapUI

    scene expression Transform("bg fase2", fit="cover") with fade
    
    show vanilton at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    vanilton "Olá, [jogador]! Seja bem-vindo ao Universo de Lógica e Estruturas Condicionais!"

    jogador "E quem é você?"

    vanilton "Sou Vanilton. Vou testar se sua lógica é forte o suficiente para continuar."

    jogador "Pode mandar, eu aceito o desafio!"

    hide vanilton

    if difficulty == "fácil":
        $ perguntas_totais = 10
        $ acertos_para_passar = 7

    elif difficulty == "médio":
        $ perguntas_totais = 10
        $ acertos_para_passar = 7

    else:
        $ perguntas_totais = 10
        $ acertos_para_passar = 7

    # --- MENU DE DEPURAÇÃO  ---
    menu:
        "Iniciar o questionário normalmente.":
            jump preparar_quiz_cyberpunk


# --- LABELS DE DEPURAÇÃO ---
label debug_passar_quiz_cyberpunk:
    $ acertos = perguntas_totais
    jump verificar_resultado_quiz_cyberpunk

label debug_falhar_quiz_cyberpunk:
    $ acertos = 0
    jump verificar_resultado_quiz_cyberpunk


# --- LÓGICA DO QUIZ ---
label preparar_quiz_cyberpunk:

    $ acertos = 0

    show screen contador_quiz

    $ mapa_dificuldade = {"fácil": "fácil", "médio": "médio", "difícil": "difícil"}
    $ chave_dificuldade_atual = mapa_dificuldade[difficulty]

    $ lista_de_perguntas = list(perguntas_fase_2[chave_dificuldade_atual])
    $ random.shuffle(lista_de_perguntas)
    $ perguntas_da_sessao = lista_de_perguntas[:perguntas_totais]
    jump proxima_pergunta_cyberpunk


label proxima_pergunta_cyberpunk:
    if not perguntas_da_sessao:
        jump verificar_resultado_quiz_cyberpunk

    $ pergunta_atual = perguntas_da_sessao.pop(0)
    $ random.shuffle(pergunta_atual['options'])

    call screen quiz_screen(
        question=pergunta_atual['answer'],
        options=pergunta_atual['options']
    )

    $ escolha_do_jogador = _return

    if escolha_do_jogador['text'] == pergunta_atual['answer_correct']:
        $ acertos += 1
        show vanilton at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)
        jogador "Essa parece a escolha lógica."
        vanilton "Exato! Seu raciocínio está correto."
        hide vanilton at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)
    else:
        show vanilton at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)
        jogador "Acho que é esta..."
        vanilton "Incorreto. A resposta certa era: [pergunta_atual['answer_correct']]"
        hide vanilton at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    jump proxima_pergunta_cyberpunk


label verificar_resultado_quiz_cyberpunk:

    hide screen contador_quiz

    if acertos >= acertos_para_passar:
        jump cyberpunk_feliz
    else:
        jump cyberpunk_triste



## Se passar

label cyberpunk_feliz:

    $ fase_3_liberada = True

    show vanilton at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    vanilton "Parabéns, [jogador]! Sua lógica passou nos meus testes."

    jogador "Ótimo, mais um passo pra casa!"

    hide vanilton at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    jump hub_controle_3_feliz



## Se não passar

label cyberpunk_triste:

    show vanilton at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    vanilton "Você ainda não domina bem as estruturas condicionais. Mas pode tentar de novo."

    jogador "Não vou desistir. Vou ajustar minha lógica!"

    hide vanilton at Position(xpos=0.49, ypos=0.92, xanchor=0.5, yanchor=1.0)

    jump hub_controle_3_triste



## Fase 1, 2 e 3 liberada

label hub_controle_3_feliz:

    scene expression Transform("bg hub", fit="cover") with pixellate
    show gilberto_android at Position(xpos=0.35, ypos=0.86, xanchor=0.8, yanchor=1.0)

    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"

    jogador "Pode vir a próxima. Estou pronto!"

    jump hub_mapa



## Fase 1 e 2 liberadas

label hub_controle_3_triste:

    scene expression Transform("bg hub", fit="cover") with pixellate
    show gilberto_android at Position(xpos=0.35, ypos=0.86, xanchor=0.8, yanchor=1.0)

    android "Que pena [jogador], mas você pode tentar novamente."

    jogador "Eu volto mais forte!"

    jump hub_mapa