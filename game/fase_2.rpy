################### FASE 2 ###############################

image bg fase2 = "images/background/bg cyberpunk.png"
image bg hub = "images/background/bg hub.png"
image vanilton = "images/characters/vanilton.png"

transform grande: 
    zoom 2.2

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



# Bloco de inicialização para carregar as perguntas da Fase 2 do JSON.
init python:
    import json
    import random

    # O carregamento do JSON já deve ter sido feito na Fase 1,
    # mas garantimos aqui caso o jogo comece direto da Fase 2 para testes.
    try:
        if 'dados_quiz' not in globals():
            with renpy.open_file("quiz_perguntas.json", encoding='utf-8') as f:
                dados_quiz = json.load(f)

        # ATENÇÃO: Chave corrigida para corresponder EXATAMENTE ao JSON.
        perguntas_fase_2 = dados_quiz["Lógica e estruturas condicionais (if, else, elif)"]
    except Exception as e:
        renpy.error("Falha ao carregar as perguntas da Fase 2 do 'quiz_perguntas.json': " + str(e))



label cyberpunk:

    hide screen MapUI

    scene expression Transform("bg fase2", fit="cover") with fade
    
    show vanilton at grande, center

    vanilton "Olá, [jogador]! Seja bem-vindo ao Universo de Lógica e Estrutura Condicionais!"

    jogador "E quem é você?"

    vanilton "Serei o seu desafiante, caso passe pelos meus desafios, ficará mais perto de voltar pra casa"

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


    # --- MENU DE DEPURAÇÃO  ---
    menu:
        "Iniciar o questionário normalmente.":
            jump preparar_quiz_cyberpunk
            
        # "DEBUG: Passar direto (100% acertos).":
        #     jump debug_passar_quiz_cyberpunk
            
        # "DEBUG: Falhar direto (0% acertos).":
        #     jump debug_falhar_quiz_cyberpunk


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

    $ mapa_dificuldade = {"easy": "fácil", "normal": "médio", "hard": "difícil"}
    $ chave_dificuldade_atual = mapa_dificuldade[difficulty]
    
    # Usa a variável com as perguntas da Fase 2
    $ lista_de_perguntas = list(perguntas_fase_2[chave_dificuldade_atual])
    
    $ random.shuffle(lista_de_perguntas)
    $ perguntas_da_sessao = lista_de_perguntas[:perguntas_totais]
    jump proxima_pergunta_cyberpunk


label proxima_pergunta_cyberpunk:
    if not perguntas_da_sessao:
        jump verificar_resultado_quiz_cyberpunk

    $ pergunta_atual = perguntas_da_sessao.pop(0)
    $ random.shuffle(pergunta_atual['opcoes'])

    call screen quiz_screen(
        question=pergunta_atual['pergunta'],
        options=pergunta_atual['opcoes']
    )

    $ escolha_do_jogador = _return

    if escolha_do_jogador == pergunta_atual['resposta_correta']:
        $ acertos += 1
        jogador "Essa parece a escolha lógica."
        vanilton "Exato! Seu raciocínio está correto."
    else:
        jogador "Acho que é esta..."
        vanilton "Incorreto. A resposta certa era: [pergunta_atual['resposta_correta']]"

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

    vanilton "Parabéns, [jogador]! Você concluiu sua segunda missão no universo"

    jogador "Finalmente! Falta pouco!"

    jump hub_controle_3_feliz



## Se não passar

label cyberpunk_triste:

    vanilton "Infelizmente você não está pronto, mas você pode tentar novamente!"

    jump hub_controle_3_triste


## Fase 1 e 2 e 3 liberada

label hub_controle_3_feliz:

    scene expression Transform("bg hub", fit="cover") with pixellate
    
    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"

    jogador "Pode vir! Estou pronto"

    jump hub_mapa


## Fase 1 e 2 liberada

label hub_controle_3_triste:

    scene expression Transform("bg hub", fit="cover") with pixellate

    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente"

    jogador "Não vou desistir!"

    jump hub_mapa