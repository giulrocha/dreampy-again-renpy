################### FASE 1 ###############################

image bg fase1 = "images/background/bg digital.png"
image bg hub = "images/background/bg hub.png"

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


# Bloco de inicialização para carregar as perguntas da Fase 1
init python:
    import json
    import random
    import requests
    import raimundo_ai

    def enviar_quiz_por_enter():
        renpy.return_statement("enviar")

    config.keymap['enviar_quiz'] = ['K_RETURN', 'K_KP_ENTER']  # ENTER e ENTER do teclado numérico

    try:
        url_json = "https://senselessly-patronal-jorge.ngrok-free.dev/api/core/quiz/?format=json"

        resposta = requests.get(url_json)
        renpy.log("STATUS: " + str(resposta.status_code))
        renpy.log("CONTENT RAW: " + resposta.text[:500])  # exibe conteúdo bruto

        resposta.raise_for_status()
        dados_quiz = resposta.json()

        renpy.log("JSON CARREGADO: " + str(dados_quiz)[:500])

        perguntas_fase_1 = dados_quiz["Valores, Tipos de Dados, Variáveis, Nomes de Variáveis, Palavras-chave"]

    except Exception as e:
        renpy.error("Erro ao carregar o JSON externo: " + str(e))




################### FASE 1 ###############################

image bg fase1 = "images/background/bg digital.png"
image bg hub = "images/background/bg hub.png"


# === NOVA TELA DE RESPOSTA ABERTA ===
screen quiz_escrita_screen(question):

    key "enviar_quiz" action Return("enviar")


    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)

        vbox:
            spacing 20

            text question:
                xalign 0.5
                size 30

            text "Digite sua resposta abaixo:":
                xalign 0.5
                size 22

            input:
                value VariableInputValue("resposta_digitada")
                length 200
                xalign 0.5

            textbutton "Enviar":
                xalign 0.5
                action Return("enviar")



label digital:

    hide screen MapUI

    scene expression Transform("bg fase1", fit="cover") with fade

    raimundo "Olá, [jogador]! Seja bem-vindo ao Universo de Variáveis!"
    jogador "Quem é você??"
    raimundo "Serei o seu desafiante, caso passe pelos meus desafios, ficará mais perto de voltar pra casa"
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

    menu:
        "Iniciar o questionário normalmente.":
            jump preparar_quiz_digital



label debug_passar_quiz:
    $ acertos = perguntas_totais
    jump verificar_resultado_quiz

label debug_falhar_quiz:
    $ acertos = 0
    jump verificar_resultado_quiz



label preparar_quiz_digital:

    $ acertos = 0
    show screen contador_quiz

    $ mapa_dificuldade = {"easy": "fácil", "normal": "médio", "hard": "difícil"}
    $ chave_dificuldade_atual = mapa_dificuldade[difficulty]

    # Lista bruta (vinda do JSON)
    $ lista_de_perguntas = list(perguntas_fase_1[chave_dificuldade_atual])

    # --- REMOVER DUPLICADAS: bloco Python (uso de for requires python: ) ---
    python:
        perguntas_unicas = []
        vistas = set()
        for p in lista_de_perguntas:
            # usa o texto da pergunta como chave de unicidade
            key = p.get("answer", "")
            if key not in vistas:
                vistas.add(key)
                perguntas_unicas.append(p)

    # logs para depuração (opcional)
    $ renpy.log("TOTAL BRUTO: " + str(len(lista_de_perguntas)))
    $ renpy.log("TOTAL UNICO: " + str(len(perguntas_unicas)))

    # embaralha e seleciona somente as que vai usar
    $ random.shuffle(perguntas_unicas)
    $ perguntas_da_sessao = perguntas_unicas[:perguntas_totais]

    jump proxima_pergunta



# ===============================
#      LÓGICA CORRIGIDA AQUI
# ===============================

label proxima_pergunta:

    if not perguntas_da_sessao:
        jump verificar_resultado_quiz

    $ pergunta_atual = perguntas_da_sessao[0]
    $ resposta_digitada = ""

    call screen quiz_escrita_screen(pergunta_atual['answer'])
    $ resposta_do_jogador = resposta_digitada.strip()

    if not resposta_do_jogador:
        raimundo "Você precisa escrever alguma resposta!"
        jump proxima_pergunta

    # Número da pergunta atual
    $ numero_da_pergunta = (perguntas_totais - len(perguntas_da_sessao)) + 1

    # IA avalia
    $ resultado = raimundo_ai.avaliar_resposta(
        pergunta_atual['answer'],
        pergunta_atual['answer_correct'],
        resposta_do_jogador,
        numero_da_pergunta
    )
    $ status_resposta = resultado.get("status")
    $ feedback_raimundo = resultado.get("feedback")

    raimundo "[feedback_raimundo]"

    if status_resposta == "correta":
        $ acertos += 1

    $ perguntas_da_sessao.pop(0)

    jump proxima_pergunta



label verificar_resultado_quiz:

    hide screen contador_quiz

    if acertos >= acertos_para_passar:
        jump digital_feliz
    else:
        jump digital_triste



label digital_feliz:

    $ fase_2_liberada = True

    raimundo "Parabéns, [jogador]! Você concluiu sua primeira missão no universo"
    jogador "Finalmente!"

    jump hub_controle_2_feliz



label digital_triste:

    raimundo "Infelizmente você não está pronto, mas você pode tentar novamente!"
    jump hub_controle_2_triste



label hub_controle_2_feliz:

    scene expression Transform("bg hub", fit="cover") with pixellate

    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"
    jogador "Pode vir! Estou pronto"

    jump hub_mapa



label hub_controle_2_triste:

    scene expression Transform("bg hub", fit="cover") with pixellate

    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente"
    jogador "Não vou desistir!"

    jump hub_mapa
