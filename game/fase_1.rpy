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
    import raimundo_ai

    try:
        with renpy.open_file("quiz_perguntas.json", encoding='utf-8') as f:
            dados_quiz = json.load(f)

        # Armazenamos apenas as perguntas desta fase numa variável para facilitar o acesso.
        perguntas_fase_1 = dados_quiz["Valores, Tipos de Dados, Variáveis, Nomes de Variáveis, Palavras-chave"]
    except Exception as e:
        # Se o ficheiro não for encontrado ou tiver um erro, o Ren'Py mostrará uma mensagem clara.
        renpy.error("Falha ao carregar o ficheiro 'quiz_perguntas.json': " + str(e))



################### FASE 1 ###############################

image bg fase1 = "images/background/bg digital.png"
image bg hub = "images/background/bg hub.png"


# === NOVA TELA DE RESPOSTA ABERTA ===
screen quiz_escrita_screen(question):

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

    # scene bg fase1 with fade

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

    # Se não tiver mais perguntas, vai pro resultado
    if not perguntas_da_sessao:
        jump verificar_resultado_quiz

    # Pegamos a pergunta sem remover da lista
    $ pergunta_atual = perguntas_da_sessao[0]

    # Limpa resposta anterior
    $ resposta_digitada = ""

    # Chama a tela com input de texto
    call screen quiz_escrita_screen(pergunta_atual['pergunta'])

    # Pega o que o jogador digitou
    $ resposta_do_jogador = resposta_digitada.strip()

    if not resposta_do_jogador:
        raimundo "Você precisa escrever alguma resposta!"
        jump proxima_pergunta

    # IA avalia
    $ status_resposta, feedback_raimundo = raimundo_ai.avaliar_resposta(
        pergunta_atual['pergunta'],
        pergunta_atual['resposta_correta'],
        resposta_do_jogador
    )

    # Raimundo comenta
    raimundo "[feedback_raimundo]"

    if status_resposta == "correta":
        $ acertos += 1
        $ perguntas_da_sessao.pop(0)
        jogador "Boa! Vamos para a próxima."
        jump proxima_pergunta

    elif status_resposta == "quase":
        jogador "Acho que cheguei perto..."
        raimundo "Você está quase lá! Tente melhorar um pouco a resposta."
        jump proxima_pergunta

    else: # errada
        jogador "Hmm... ainda não."
        raimundo "Está incorreto. Leia a pergunta com calma e tente novamente."
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

    raimundo "Parabéns, [jogador]! Você concluiu sua primeira missão no universo"

    jogador "Finalmente!"

    jump hub_controle_2_feliz


## Se não passar

label digital_triste:

    raimundo "Infelizmente você não está pronto, mas você pode tentar novamente!"

    jump hub_controle_2_triste


## Fase 1 e 2 liberada

label hub_controle_2_feliz:

    scene expression Transform("bg hub", fit="cover") with pixellate

    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"

    jogador "Pode vir! Estou pronto"

    jump hub_mapa


## Fase 1 liberada

label hub_controle_2_triste:

    scene expression Transform("bg hub", fit="cover") with pixellate

    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente"

    jogador "Não vou desistir!"

    jump hub_mapa