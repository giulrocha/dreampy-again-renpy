# ################### FASE 2 ###############################

# Declaramos a imagem de fundo para a fase 2.
# Adapte o caminho se a sua imagem tiver outro nome.
image bg fase2 = "images/background/fase2.jpg"

# --- TELA CUSTOMIZADA PARA O QUIZ (Reutilizada da Fase 1) ---
# Esta tela exibe uma pergunta e uma lista de opções como botões.
screen quiz_screen(question, options):
    # Usamos um frame para agrupar os elementos do quiz com um fundo semi-transparente.
    frame:
        # Alinha o frame no centro da tela
        xalign 0.5
        yalign 0.5
        # Define um preenchimento interno para não colar nas bordas
        padding (30, 30)

        # Organiza os elementos verticalmente
        vbox:
            spacing 20  # Espaço entre a pergunta e as alternativas

            # 1. O Texto da Pergunta
            text question:
                xalign 0.5  # Centraliza o texto da pergunta

            # 2. As Alternativas como Botões
            for option in options:
                textbutton option:
                    xalign 0.5  # Centraliza os botões
                    # A ação 'Return(option)' fecha a tela e retorna o texto do botão.
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
    # Esconde a tela do mapa que estava visível.
    hide screen MapUI
    
    # Define o fundo da cena.
    scene bg fase2 with fade

    # Diálogo inicial da Fase 2
    vanilton "Olá, [jogador]! Seja bem-vindo ao Universo de Lógica e Estrutura Condicionais!"
    jogador "E quem é você?"
    vanilton "Serei o seu desafiante, caso passe pelos meus desafios e lhe darei a jóia necessária para voltar pra casa"
    jogador "Aceito seu desafio!"

    # Definição das regras
    if difficulty == "easy":
        $ perguntas_totais = 10
        $ acertos_para_passar = 7
    elif difficulty == "normal":
        $ perguntas_totais = 10
        $ acertos_para_passar = 7
    else: # difficulty == "hard"
        $ perguntas_totais = 10
        $ acertos_para_passar = 7

    # --- MENU DE DEPURAÇÃO (Replicado da Fase 1) ---
    menu:
        "Iniciar o questionário normalmente.":
            jump preparar_quiz_cyberpunk
            
        "DEBUG: Passar direto (100% acertos).":
            jump debug_passar_quiz_cyberpunk
            
        "DEBUG: Falhar direto (0% acertos).":
            jump debug_falhar_quiz_cyberpunk


# --- LABELS DE DEPURAÇÃO para a Fase 2 ---
label debug_passar_quiz_cyberpunk:
    $ acertos = perguntas_totais
    jump verificar_resultado_quiz_cyberpunk

label debug_falhar_quiz_cyberpunk:
    $ acertos = 0
    jump verificar_resultado_quiz_cyberpunk


# --- LÓGICA DO QUIZ (Adaptada para a Fase 2) ---
label preparar_quiz_cyberpunk:
    $ acertos = 0
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
    if acertos >= acertos_para_passar:
        jump cyberpunk_feliz
    else:
        jump cyberpunk_triste


## Se passar
label cyberpunk_feliz:
    $ fase_3_liberada = True
    vanilton "Parabéns, [jogador]! Você concluiu sua segunda missão no universo e merece seu prêmio"
    #mostra a joia la
    jogador "Finalmente! Falta pouco!"
    jump hub_controle_3_feliz


## Se não passar
label cyberpunk_triste:
    vanilton "Infelizmente você não está pronto, mas você pode tentar novamente!"
    #corta pro hub
    jump hub_controle_3_triste


## Fase 1, 2 e 3 liberada
label hub_controle_3_feliz:
    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"
    jogador "Pode vir! Estou pronto"
    # MUDANÇA IMPORTANTE: Salta de volta para o hub do mapa
    jump hub_mapa


## Fase 1 e 2 liberada (mas não passou a 2)
label hub_controle_3_triste:
    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente"
    jogador "Não vou desistir!"
    # MUDANÇA IMPORTANTE: Salta de volta para o hub do mapa
    jump hub_mapa