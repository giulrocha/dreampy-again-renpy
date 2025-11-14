
# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.

# transform map_icon_size:
    # zoom 2.0
    # fit "cover" 
    # size (250, 250)  # Ajuste conforme quiser
    # anchor (0.5, 0.5)  # Centraliza o ponto de clique
    # nearest True

label call_mapUI:
    call screen MapUI
    #incluido depois esse return
    return

## Tela de interação com o mapa
screen MapUI:

    # add "#000" 
    # add Transform("map/mapa(1).png", fit="cover") 
    add Transform("map/mapa(1).png", size=(config.screen_width, config.screen_height), fit="cover")

    if fase_1_liberada:
        # FASE 1
        imagebutton:
            xpos 130    #antes 32
            ypos 350     #antes 50
            idle At("images/map/fase-1-idle.png")  #, map_icon_size
            hover At("images/map/fase-1-hover.png")  #, map_icon_size
            focus_mask True
            # action Jump("digital")
            action [Hide("MapUI"), Jump("digital")]

    if fase_2_liberada:
        # FASE 2    
        imagebutton:
            xpos 330    #antes 480
            ypos 360     #antes 450
            idle At("images/map/fase-2-idle.png")   #, map_icon_size
            hover At("images/map/fase-2-hover.png")  #, map_icon_size
            focus_mask True
            # action Jump("cyberpunk")
            action [Hide("MapUI"), Jump("cyberpunk")]


    if fase_3_liberada:
        # FASE 3    
        imagebutton:
            xpos 520   #antes 650
            ypos 350    #antes 440
            idle At("images/map/fase-3-idle.png")  #, map_icon_size
            hover At("images/map/fase-3-hover.png")  #, map_icon_size
            focus_mask True
            # action Jump("marinho")
            action [Hide("MapUI"), Jump("marinho")]


    if fase_4_liberada:
        # FASE 4    
        imagebutton:
            xpos 820
            ypos 420
            idle At("images/map/fase-4-idle.png")   #, map_icon_size
            hover At("images/map/fase-4-hover.png")   #, map_icon_size
            focus_mask True
            # action Jump("medieval")
            action [Hide("MapUI"), Jump("medieval")]


    if fase_5_liberada:
        # FASE 5    
        imagebutton:
            xpos 950
            ypos 380
            idle At("images/map/fase-5-idle.png")   #, map_icon_size
            hover At("images/map/fase-5-hover.png")  #, map_icon_size
            focus_mask True
            # action Jump("alienigena")
            action [Hide("MapUI"), Jump("alienigena")]


    if volta_pra_casa:
        # VAI PRA CASA
        imagebutton:
            xpos 1150
            ypos 200
            idle At("images/map/volta-pra-casa-idle.png")   #, map_icon_size
            hover At("images/map/volta-pra-casa-hover.png")   #, map_icon_size
            focus_mask True
            # action Jump("final")
            action [Hide("MapUI"), Jump("final")]