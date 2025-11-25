# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.
# The game starts here.
#Definindo personagens, título e cor dos nomes na tela
define professor_gilberto = Character("Professor Gilberto", color="#3477eb")
define jogador = Character("Jogador",  color="#34d8eb")    #nome de user que cadastrou la no tela inicial
define aluno_1 = Character("Giulie", color="#f2b3ed")
define aluno_2 = Character("Yasmim", color="#b3dff2")
define aluno_3 = Character("Luan", color="#e34f61")
define android = Character("Android Giba", color="#3477eb")
define raimundo = Character("Cientista Raimundo", color="#78c4cc")      ## FASE 1
define vanilton = Character("Vanilton", color="#6935db")           ## FASE 2
define willon = Character("Tritão Willon", color="#c8cecf")          ## FASE 3
define frank = Character("Mago Frank", color="#c8cecf")            ## FASE 4
define sergio = Character("Alien Sergio", color="#c8cecf")         ## FASE 5


# Declaração de fases


default fase_1_liberada = True      
default fase_2_liberada = False
default fase_3_liberada = False
default fase_4_liberada = False
default fase_5_liberada = False
default volta_pra_casa = False


###############################

# Variáveis do sistema de resposta escrita da Fase 1
default resposta_digitada = ""
default feedback_raimundo = ""


############# START JOGO
label start:

    call choice_character from _call_choice_character



############# ESCOLHA DE PERSONAGENS

default personagem_preview = None

image aluna = "images/characters/renata_andando.png"
image aluno = "images/characters/thiago.png"

screen escolha_personagem():

    modal True
    tag menu

    # Fundo da tela
    add "black"

    # Título
    text "Escolha seu personagem Jogador:":
        xalign 0.5
        yalign 0.1
        size 40

    # Botões de escolha
    vbox:
        xalign 0.5
        yalign 0.35
        spacing 20

        textbutton "Renata":
            xalign 0.5
            action Return("renata")
            hovered SetVariable("personagem_preview", "renata")
            unhovered SetVariable("personagem_preview", None)

        textbutton "Thiago":
            xalign 0.5
            action Return("thiago")
            hovered SetVariable("personagem_preview", "thiago")
            unhovered SetVariable("personagem_preview", None)

    # --- Área de preview ---
    if personagem_preview == "renata":
        add "images/characters/renata_andando.png":
            xalign 0.5
            yalign 0.75

    if personagem_preview == "thiago":
        add "images/characters/thiago.png":
            xalign 0.5
            yalign 0.75

label choice_character:

    # Chama a tela
    $ escolha = renpy.call_screen("escolha_personagem")

    # Processa a escolha
    if escolha == "renata":
        $ jogador = "Renata"
    elif escolha == "thiago":
        $ jogador = "Thiago"

    jump dificuldade


#########Escolhe dificuldade do jogo
label dificuldade:
    scene black with fade
    show text "Escolha o nível de dificuldade:" at Position(xalign=0.5, yalign=0.2)
    menu:
        "Fácil":
            $ difficulty = "easy"
            call intro from _call_intro
            jump hub_mapa
        "Normal":
            $ difficulty = "normal"
            call intro from _call_intro_1
            jump hub_mapa
        "Difícil":
            $ difficulty = "hard"
            call intro from _call_intro_2
            jump hub_mapa


screen contador_quiz:
    frame:
        xalign 0.02
        yalign 0.02
        padding (10, 5)
        background "#0008"  

        text "Acertos: [acertos] / [perguntas_totais]" size 28 color "#e650cf"


# ####################################################################
# HUB CENTRAL DO MAPA
# O jogo sempre voltará para este ponto após uma fase.
# ####################################################################
label hub_mapa:
    # Esconde a caixa de diálogo para uma visão limpa do mapa
    window hide

    # Usando "call screen" para mostrar o mapa e esperar por uma
    # interação válida (um clique num botão). Cliques no fundo serão ignorados.
    call screen MapUI

    # Só será executado se a tela MapUI usar a ação "Return",
    # o que não deve acontecer no fluxo normal do jogo.
    "Algo correu mal com o mapa."
    return