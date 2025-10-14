# Transform para redimensionar as imagens dos botões do mapa.
# Você pode ajustar os valores (150, 120) para a largura e altura que desejar.
transform map_icon_size:
    size (150, 120)


# Tela da UI principal com o botão para abrir o mapa
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png"
        # Esta ação chama a tela do mapa
        action Show("MapUI")


# Tela de interação com o mapa
screen MapUI:

    # Imagem de fundo do mapa
    add "images/map/bg map.jpg"

    # --- FASE 1 ---
    if fase_1_liberada:
        imagebutton:
            xpos 618
            ypos 570
            # Aplica a transform de redimensionamento às imagens
            idle At("images/map/house1_idle.png", map_icon_size)
            #hover At("images/map/house1_hover.png", map_icon_size)
            action Jump("digital")

    # --- FASE 2 ---
    if fase_2_liberada:
        imagebutton:
            xpos 596
            ypos 165
            # Aplica a transform de redimensionamento às imagens
            idle At("images/map/house2_idle.png", map_icon_size)
            #hover At("images/map/house2_hover.png", map_icon_size)
            action Jump("cyberpunk")

    # --- FASE 3 ---
    if fase_3_liberada:
        imagebutton:
            xpos 950  # Lembre-se de ajustar a posição!
            ypos 350  # Lembre-se de ajustar a posição!
            # Aplica a transform de redimensionamento às imagens
            idle At("images/map/house3_idle.png", map_icon_size)
            #hover At("images/map/house3_hover.png", map_icon_size)
            action Jump("marinho")

    # --- FASE 4 ---
    if fase_4_liberada:
        imagebutton:
            xpos 300  # Lembre-se de ajustar a posição!
            ypos 400  # Lembre-se de ajustar a posição!
            # Aplica a transform de redimensionamento às imagens
            idle At("images/map/house4_idle.png", map_icon_size)
            #hover At("images/map/house4_hover.png", map_icon_size)
            action Jump("medieval")

    # --- FASE 5 ---
    if fase_5_liberada:
        imagebutton:
            xpos 800  # Lembre-se de ajustar a posição!
            ypos 600  # Lembre-se de ajustar a posição!
            # Aplica a transform de redimensionamento às imagens
            idle At("images/map/house5_idle.png", map_icon_size)
            #hover At("images/map/house5_hover.png", map_icon_size)
            action Jump("alienigena")

    # --- VOLTA PRA CASA ---
    if volta_pra_casa:
        imagebutton:
            xpos 120  # Lembre-se de ajustar a posição!
            ypos 150  # Lembre-se de ajustar a posição!
            # Aplica a transform de redimensionamento às imagens
            idle At("images/map/house6_idle.png", map_icon_size)
            #hover At("images/map/house6_hover.png", map_icon_size)
            action Jump("final")