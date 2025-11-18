
# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.


label call_mapUI:
    call screen MapUI
    return

## Tela de interação com o mapa
screen MapUI:

    add "images/map/mapa.png" xysize (config.screen_width, config.screen_height)


    if fase_1_liberada:
        # FASE 1
        imagebutton:
            xpos 180    
            ypos 680   
            idle im.Scale("images/map/fase-1-idle.png", 250, 350)  
            hover im.Scale("images/map/fase-1-hover.png", 250, 350)  
            focus_mask True
            # action Jump("digital")
            action [Hide("MapUI"), Jump("digital")]
    

    if fase_2_liberada:
        # FASE 2    
        imagebutton:
            xpos 550   
            ypos 550    
            idle im.Scale("images/map/fase-2-idle.png", 250, 300)   
            hover im.Scale("images/map/fase-2-hover.png", 250, 300)  
            focus_mask True
            action Jump("cyberpunk")
            # action [Hide("MapUI"), Jump("cyberpunk")]
            


    if fase_3_liberada:
        # FASE 3    
        imagebutton:
            xpos 1050   
            ypos 350    
            idle im.Scale("images/map/fase-3-idle.png", 300, 350)     
            hover im.Scale("images/map/fase-3-hover.png", 300, 350)  
            focus_mask True
            action Jump("marinho")
            # action [Hide("MapUI"), Jump("marinho")]
            


    if fase_4_liberada:
        # FASE 4    
        imagebutton:
            xpos 800
            ypos 630
            idle im.Scale("images/map/fase-4-idle.png", 400, 400)   
            hover im.Scale("images/map/fase-4-hover.png", 400, 400)   
            focus_mask True
            action Jump("medieval")
            # action [Hide("MapUI"), Jump("medieval")]
            


    if fase_5_liberada:
        # FASE 5    
        imagebutton:
            xpos 1450
            ypos 560
            idle im.Scale("images/map/fase-5-idle.png", 280, 300)   
            hover im.Scale("images/map/fase-5-hover.png", 280, 300)  
            focus_mask True
            action Jump("alienigena")
            # action [Hide("MapUI"), Jump("alienigena")]
            


    if volta_pra_casa:
        # VAI PRA CASA
        imagebutton:
            xpos 1480
            ypos 160
            idle im.Scale("images/map/volta-pra-casa-idle.png", 200, 200)   
            hover im.Scale("images/map/volta-pra-casa-hover.png", 200, 200)   
            focus_mask True
            # action Jump("final")
            action [Hide("MapUI"), Jump("final")]
            