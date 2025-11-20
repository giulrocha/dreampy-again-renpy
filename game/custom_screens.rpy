
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
            ypos 580   
            idle im.Scale("images/map/fase-1-idle.png", 450, 400)  
            hover im.Scale("images/map/fase-1-hover.png", 450, 400)  
            focus_mask True
            # action Jump("digital")
            action [Hide("MapUI"), Jump("digital")]
    

    if fase_2_liberada:
        # FASE 2    
        imagebutton:
            xpos 500   
            ypos 150    
            idle im.Scale("images/map/fase-2-idle.png", 450, 400)   
            hover im.Scale("images/map/fase-2-hover.png", 450, 400)  
            focus_mask True
            action Jump("cyberpunk")
            # action [Hide("MapUI"), Jump("cyberpunk")]
            


    if fase_3_liberada:
        # FASE 3    
        imagebutton:
            xpos 1050   
            ypos 250    
            idle im.Scale("images/map/fase-3-idle.png", 400, 400)     
            hover im.Scale("images/map/fase-3-hover.png", 400, 400)  
            focus_mask True
            action Jump("marinho")
            # action [Hide("MapUI"), Jump("marinho")]
            


    if fase_4_liberada:
        # FASE 4    
        imagebutton:
            xpos 750
            ypos 600
            idle im.Scale("images/map/fase-4-idle.png", 450, 450)   
            hover im.Scale("images/map/fase-4-hover.png", 450, 450)   
            focus_mask True
            action Jump("medieval")
            # action [Hide("MapUI"), Jump("medieval")]
            


    if fase_5_liberada:
        # FASE 5    
        imagebutton:
            xpos 1450
            ypos 560
            idle im.Scale("images/map/fase-5-idle.png", 400, 400)   
            hover im.Scale("images/map/fase-5-hover.png", 400, 400)  
            focus_mask True
            action Jump("alienigena")
            # action [Hide("MapUI"), Jump("alienigena")]
            


    if volta_pra_casa:
        # VAI PRA CASA
        imagebutton:
            xpos 1480
            ypos 140
            idle im.Scale("images/map/volta-pra-casa-idle.png", 400, 400)   
            hover im.Scale("images/map/volta-pra-casa-hover.png", 400, 400)   
            focus_mask True
            # action Jump("final")
            action [Hide("MapUI"), Jump("final")]
            