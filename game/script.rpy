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
define raimundo = Character("Raimundo", color="#78c4cc")      ## FASE 1
define vanilton = Character("Vanilton", color="#6935db")      ## FASE 2
define pedro = Character("Pedro", color="#c8cecf")            ## FASE 3

# Declaração de fases

default fase_1_liberada = True      
default fase_2_liberada = False
default fase_3_liberada = False
default fase_4_liberada = False
default fase_5_liberada = False
default volta_pra_casa = False

############### FALTA COLOCAR O START, PENSAR NISSO DEPOIS

label start:

    call choice_character


#Escolhe personagem
label choice_character:
    scene black with fade
    show text "Escolha seu personagem [jogador]:" at Position(xalign=0.5, yalign=0.2)
    menu:
        "Aluna":
            jump dificuldade
        "Aluno":
            jump dificuldade

#Escolhe dificuldade do jogo
label dificuldade:
    scene black with fade
    show text "Escolha o nível de dificuldade:" at Position(xalign=0.5, yalign=0.2)
    menu:
        "Fácil":
            $ difficulty = "easy"
            jump start_game_easy
        "Normal":
            $ difficulty = "normal"
            jump start_game_normal
        "Difícil":
            $ difficulty = "hard"
            jump start_game_hard


label start_game_easy:

    call intro

    call screen MapUI

label start_game_normal:

    call intro

    call screen MapUI

label start_game_hard:

    call intro

    call screen MapUI