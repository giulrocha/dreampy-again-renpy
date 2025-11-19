################### FINAL ###########################

image bg ending = "images/background/bg classroom.png"
image gilberto_1 = "images/characters/gilberto_1.png"
image gilberto_2 = "images/characters/gilberto_2.png"
image renata_andando = "images/characters/renata_andando.png"
image renata_desmotivada = "images/characters/renata_desmotivada.png"
image renata = "images/characters/renata_feliz.png"
image renata_comemorando = "images/characters/renata_comemorando.png"
image renata_raiva = "images/characters/renata_raiva.png"
image renata_triste = "images/characters/renata_triste.png"
image renata_sono = "images/characters/renata_sono.png"
image renata_vou_conseguir = "images/characters/renata_vou_conseguir.png"
image thiago = "images/characters/thiago.png"
image thiago_comemorando = "images/characters/thiago_comemorando.png"
image thiago_duvida = "images/characters/thiago_duvida.png"
image thiago_raiva = "images/characters/thiago_raiva.png"
image thiago_triste = "images/characters/thiago_triste.png"
image thiago_sono = "images/characters/thiago_sono.png"
image thiago_vou_conseguir = "images/characters/thiago_vou_conseguir.png"
image giulie_feliz = "images/characters/giulie_feliz.png"
image giulie_triste = "images/characters/giulie_triste.png"
image giulie = "images/characters/giulie.png"
image giulie_apreensiva = "images/characters/giulie_apreensiva.png"
image luan = "images/characters/luan.png"
image luan_feliz = "images/characters/luan_feliz.png"
image luan_surtando = "images/characters/luan_surtando.png"
image yasmim = "images/characters/yasmim.png"
image yasmim_falando = "images/characters/yasmim_falando.png"
image yasmim_feliz = "images/characters/yasmim_feliz.png"
image yasmim_apreensiva = "images/characters/yasmim_apreensiva.png"
image gilberto_android = "images/characters/gilberto_android.png"

label final:

    scene expression Transform("bg ending", fit="cover") with fade

    show gilberto_2 at Position(xpos=0.59, ypos=0.70, xanchor=0.5, yanchor=1.0)
    if jogador == "Renata":
        show renata at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        show thiago at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    show giulie at Position(xpos=0.39, ypos=0.74, xanchor=0.5, yanchor=1.0)
    show luan at Position(xpos=0.31, ypos=0.74, xanchor=0.5, yanchor=1.0)
    show yasmim at Position(xpos=0.67, ypos=0.74, xanchor=0.5, yanchor=1.0)   

    professor_gilberto "Bom dia, turma! Chegou o momento de mostrar tudo o que aprenderam. As provas estão em suas mesas. Boa sorte a todos!"

    hide gilberto_2 at Position(xpos=0.59, ypos=0.70, xanchor=0.5, yanchor=1.0)
    show gilberto_1 at Position(xpos=0.59, ypos=0.70, xanchor=0.5, yanchor=1.0)

    if jogador == "Renata":
        hide renata at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        hide thiago at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    
    if jogador == "Renata":
        show renata_desmotivada at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        show thiago_duvida at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)

    hide giulie at Position(xpos=0.39, ypos=0.74, xanchor=0.5, yanchor=0.90)
    show giulie_apreensiva at Position(xpos=0.39, ypos=0.74, xanchor=0.5, yanchor=1.0)

    aluno_1 "Ai meu Deus... agora é real!"

    hide yasmim at Position(xpos=0.67, ypos=0.74, xanchor=0.5, yanchor=1.0)  
    show yasmim_apreensiva at Position(xpos=0.67, ypos=0.74, xanchor=0.5, yanchor=1.0) 

    aluno_2 "Eu revisei tanto que até sonhei com código!"

    hide luan at Position(xpos=0.31, ypos=0.74, xanchor=0.5, yanchor=1.0)
    show luan_surtando at Position(xpos=0.31, ypos=0.74, xanchor=0.5, yanchor=1.0)

    aluno_3 "Espero que o Python tenha piedade de mim hoje."

    if jogador == "Renata":
        hide renata_desmotivada at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        hide thiago_duvida at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)

    if jogador == "Renata":
        show renata_vou_conseguir at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        show thiago_vou_conseguir at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)

    jogador "Dessa vez, estou pronto."

    ###galerinha fazendo prova

    ### dá uma transição ai

    scene expression Transform("bg ending", fit="cover") with pixellate

    show gilberto_2 at Position(xpos=0.59, ypos=0.70, xanchor=0.5, yanchor=1.0)
    if jogador == "Renata":
        show renata at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        show thiago at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    show giulie at Position(xpos=0.39, ypos=0.74, xanchor=0.5, yanchor=1.0)
    show luan at Position(xpos=0.31, ypos=0.74, xanchor=0.5, yanchor=1.0)
    show yasmim at Position(xpos=0.67, ypos=0.74, xanchor=0.5, yanchor=1.0)   

    professor_gilberto "Terminou, [jogador]? Espero que tenha se saído bem."

    if jogador == "Renata":
        hide renata at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        hide thiago at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    
    if jogador == "Renata":
        show renata_vou_conseguir at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        show thiago_vou_conseguir at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)

    jogador "Acho que, pela primeira vez, eu realmente entendi o que estava fazendo."

    professor_gilberto "Isso é o que mais importa. A nota é apenas uma consequência do aprendizado verdadeiro."

    # Transição para o resultado

    scene expression Transform("bg ending", fit="cover") with pixellate

    show gilberto_2 at Position(xpos=0.59, ypos=0.70, xanchor=0.5, yanchor=1.0)
    if jogador == "Renata":
        show renata at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        show thiago at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    show giulie at Position(xpos=0.39, ypos=0.74, xanchor=0.5, yanchor=1.0)
    show luan at Position(xpos=0.31, ypos=0.74, xanchor=0.5, yanchor=1.0)
    show yasmim at Position(xpos=0.67, ypos=0.74, xanchor=0.5, yanchor=1.0)  

    professor_gilberto "Turma! Os resultados da prova saíram. Parabéns — a maioria de vocês foi muito bem!"

    aluno_1 "Ai, fala logo, professor! Como eu fui?"

    hide giulie at Position(xpos=0.39, ypos=0.74, xanchor=0.5, yanchor=0.90)
    show giulie_feliz at Position(xpos=0.39, ypos=0.74, xanchor=0.5, yanchor=1.0)

    professor_gilberto "Giulie, excelente como sempre."

    hide yasmim at Position(xpos=0.67, ypos=0.74, xanchor=0.5, yanchor=1.0)
    show yasmim_feliz at Position(xpos=0.67, ypos=0.74, xanchor=0.5, yanchor=1.0)
    
    professor_gilberto "Yasmim, ótimo progresso." 

    hide luan at Position(xpos=0.31, ypos=0.74, xanchor=0.5, yanchor=1.0)
    show luan_feliz at Position(xpos=0.31, ypos=0.74, xanchor=0.5, yanchor=1.0)
    
    professor_gilberto "Luan, melhorou bastante!"

    jogador "E eu, professor?"

    if jogador == "Renata":
        hide renata at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        hide thiago at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    
    if jogador == "Renata":
        show renata_comemorando at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        show thiago_comemorando at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)

    professor_gilberto "Você, [jogador]... superou todas as expectativas. Conquistou a nota máxima."

    if jogador == "Renata":
        hide renata_comemorando at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        hide thiago_comemorando at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    
    if jogador == "Renata":
        show renata_feliz at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        show thiago at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)

    jogador "Acho que finalmente despertei meu verdadeiro potencial."

    hide giulie_feliz at Position(xpos=0.39, ypos=0.74, xanchor=0.5, yanchor=0.90)
    show giulie at Position(xpos=0.39, ypos=0.74, xanchor=0.5, yanchor=1.0)

    hide yasmim_feliz at Position(xpos=0.67, ypos=0.74, xanchor=0.5, yanchor=1.0)
    show yasmim at Position(xpos=0.67, ypos=0.74, xanchor=0.5, yanchor=1.0)

    hide luan_feliz at Position(xpos=0.31, ypos=0.74, xanchor=0.5, yanchor=1.0)
    show luan at Position(xpos=0.31, ypos=0.74, xanchor=0.5, yanchor=1.0)

    professor_gilberto "Nunca se esqueça, [jogador]: programar é como sonhar acordado — basta transformar suas ideias em lógica."

    show text "FIM — Seu código foi reescrito com sucesso." at Position(xalign=0.5, yalign=0.5)

    scene bg fim    
    with fade
    pause
    $ renpy.full_restart()