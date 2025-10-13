## Tela com os diamantes na tela ????? pensar se vou colocar

### exemplo abaixo está com o botão de começar
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png"
        # AÇÃO CORRIGIDA: Usando "Call" para chamar a tela do mapa diretamente.
        action Call("MapUI")

# O label "call_mapUI" que estava aqui foi removido, pois estava incorreto.

## Tela de interação com o mapa
screen MapUI:

    # Caminho já estava correto
    add "images/map/bg map.jpg"

    if fase_1_liberada:
        # FASE 1
        imagebutton:
            xpos 618
            ypos 570
            # Caminho já estava correto
            idle "images/map/house1_idle.png"
            #hover "images/map/house1_hover.png"
            # AÇÃO CORRIGIDA: A ação deve pular para o label "digital", não "quiz_digital"
            action Jump("digital")

    if fase_2_liberada:
        # FASE 2
        imagebutton:
            xpos 596
            ypos 165
            # CAMINHOS CORRIGIDOS
            idle "images/map/house2_idle.png"
            #hover "images/map/house2_hover.png"
            action Jump("cyberpunk") # Presumindo que o label seja "cyberpunk"


    if fase_3_liberada:
        # FASE 3
        imagebutton:
            xpos 596
            ypos 165
            # CAMINHOS CORRIGIDOS
            idle "images/map/house3_idle.png"
            #hover "images/map/house3_hover.png"
            action Jump("marinho") # Presumindo que o label seja "marinho"


    if fase_4_liberada:
        # FASE 4
        imagebutton:
            xpos 596
            ypos 165
            # CAMINHOS CORRIGIDOS
            idle "images/map/house4_idle.png"
            #hover "images/map/house4_hover.png"
            action Jump("medieval") # Presumindo que o label seja "medieval"


    if fase_5_liberada:
        # FASE 5
        imagebutton:
            xpos 596
            ypos 165
            # CAMINHOS CORRIGIDOS
            idle "images/map/house5_idle.png"
            #hover "images/map/house5_hover.png"
            action Jump("alienigena") # Presumindo que o label seja "alienigena"


    if volta_pra_casa:
         # VAI PRA CASA
        imagebutton:
            xpos 596
            ypos 165
            # CAMINHOS CORRIGIDOS
            idle "images/map/house6_idle.png"
            #hover "images/map/house6_hover.png"
            action Jump("final")