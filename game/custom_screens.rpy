## Tela com os diamantes na tela ????? pensar se vou colocar

###exemplo abaixo está com o botão de começar
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png"
        action Jump ("call_mapUI")
        # You may also use the code below depending on your needs.
        # action ShowMenu("mapUI")
        # This was the same code used in the vlog.

# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.
label call_mapUI:
    call screen MapUI

## Tela de interação com o mapa
screen MapUI:

    add "map/bg map.jpg"

    if fase_1_liberada:
        # FASE 1
        imagebutton:
            xpos 618    #### mudar
            ypos 570      #### mudar
            idle "map/house1_idle.png"        #### quando está normal
            hover "map/house1_hover.png"       #### quando passa o mouse em cima
            action Jump("quiz_digital")

    if fase_2_liberada:
        # FASE 2    
        imagebutton:
            xpos 596       ## mudar       
            ypos 165        ## mudar
            idle "map/house2_idle.png"      ### quando está normal
            hover "map/house2_hover.png"      #### quando passa o mouse em cima
            action Jump("quiz_cyberpunk")


    if fase_3_liberada:
        # FASE 3    
        imagebutton:
            xpos 596       ## mudar       
            ypos 165        ## mudar
            idle "map/house3_idle.png"      ### quando está normal
            hover "map/house3_hover.png"      #### quando passa o mouse em cima
            action Jump("quiz_marinho")


    if fase_4_liberada:
        # FASE 4    
        imagebutton:
            xpos 596       ## mudar       
            ypos 165        ## mudar
            idle "map/house4_idle.png"      ### quando está normal
            hover "map/house4_hover.png"      #### quando passa o mouse em cima
            action Jump("quiz_medieval")


    if fase_5_liberada:
        # FASE 5    
        imagebutton:
            xpos 596       ## mudar       
            ypos 165        ## mudar
            idle "map/house5_idle.png"      ### quando está normal
            hover "map/house5_hover.png"      #### quando passa o mouse em cima
            action Jump("quiz_alienigena")


    if volta_pra_casa:
        # VAI PRA CASA
        imagebutton:
            xpos 596       ## mudar       
            ypos 165        ## mudar
            idle "map/house6_idle.png"      ### quando está normal
            hover "map/house6_hover.png"      #### quando passa o mouse em cima
            action Jump("final")