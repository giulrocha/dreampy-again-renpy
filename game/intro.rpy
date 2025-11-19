#Parte Indrodutória comum a todas as dificuldades

image bg intro = "images/background/bg classroom.png"
image bg bedroom = "images/background/bg bedroom.png"
image bg hub = "images/background/bg hub.png"
image gilberto_1 = "images/characters/gilberto_1.png"
image gilberto_2 = "images/characters/gilberto_2.png"
image renata_andando = "images/characters/renata_andando.png"
image renata_desmotivada = "images/characters/renata_desmotivada.png"
image renata = "images/characters/renata_feliz.png"
image renata_comemorando = "images/characters/renata_comemorando.png"
image renata_raiva = "images/characters/renata_raiva.png"
image renata_triste = "images/characters/renata_triste.png"
image thiago = "images/characters/thiago.png"
image thiago_comemorando = "images/characters/thiago_comemorando.png"
image thiago_duvida = "images/characters/thiago_duvida.png"
image thiago_raiva = "images/characters/thiago_raiva.png"
image thiago_triste = "images/characters/thiago_triste.png"
image giulie_feliz = "images/characters/giulie_feliz.png"
image giulie_triste = "images/characters/giulie_triste.png"
image giulie = "images/characters/giulie.png"
image luan = "images/characters/luan.png"
image luan_feliz = "images/characters/luan_feliz.png"
image luan_surtando = "images/characters/luan_surtando.png"
image yasmim = "images/characters/yasmim.png"
image yasmim_falando = "images/characters/yasmim_falando.png"
image yasmim_feliz = "images/characters/yasmim_feliz.png"

label intro:

    #cena da sala de aula
    scene expression Transform("bg intro", fit="cover") with fade

    show gilberto_2 at Position(xpos=0.59, ypos=0.70, xanchor=0.5, yanchor=1.0)
    if jogador == "Renata":
        show renata at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        show thiago at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    show giulie at Position(xpos=0.39, ypos=0.74, xanchor=0.5, yanchor=1.0)
    show luan at Position(xpos=0.31, ypos=0.74, xanchor=0.5, yanchor=1.0)
    show yasmim at Position(xpos=0.67, ypos=0.74, xanchor=0.5, yanchor=1.0)    


    #aparece o professor e alunos

    professor_gilberto "Alunos, informo que o simulado final para conclusão do curso é amanhã! Espero que estejam preparados para mais esse desafio, não me decepcionem!"

    hide gilberto_2 at Position(xpos=0.59, ypos=0.70, xanchor=0.5, yanchor=1.0)
    show gilberto_1 at Position(xpos=0.59, ypos=0.70, xanchor=0.5, yanchor=1.0)

    if jogador == "Renata":
        hide renata at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        hide thiago at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)

    if jogador == "Renata":
        show renata_desmotivada at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        show thiago_triste at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)

    jogador "Nossa… tenho que revisar urgentemente tudo! Havia esquecido que a prova estava tão perto!"

    hide giulie at Position(xpos=0.39, ypos=0.74, xanchor=0.5, yanchor=1.0)
    show giulie_triste at Position(xpos=0.39, ypos=0.74, xanchor=0.5, yanchor=1.0)

    aluno_1 "Calma, esquecer faz parte da emoção da reta final! Estudar com um pouco de pressão até me ajuda a focar melhor."

    hide yasmim at Position(xpos=0.67, ypos=0.74, xanchor=0.5, yanchor=1.0)  
    show yasmim_falando at Position(xpos=0.67, ypos=0.74, xanchor=0.5, yanchor=1.0)  

    aluno_2 "Ih, lá vem ela com esse papo! Essa aí já devia estar dando aula com o professor Gilberto. Vive acertando tudo! Se eu tirar metade da sua nota, já tô comemorando com bolo e guaraná."
    
    aluno_1 "Que isso, só tento não surtar… muito."

    hide luan at Position(xpos=0.31, ypos=0.74, xanchor=0.5, yanchor=1.0)
    show luan_surtando at Position(xpos=0.31, ypos=0.74, xanchor=0.5, yanchor=1.0)

    aluno_3 "Então tá fazendo errado, porque surtar é meu plano A! Inclusive, se alguém achar minha calma por aí, favor devolver antes da prova!"

    if jogador == "Renata":
        hide renata_desmotivada at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        hide thiago_triste at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)

    if jogador == "Renata":
        show renata_andando at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)
    else:
        show thiago at Position(xpos=0.49, ypos=0.72, xanchor=0.5, yanchor=1.0)

    jogador "Vou logo para casa e virar a noite estudando..."

    scene expression Transform("bg bedroom", fit="cover") with pixellate

    "Você já está estudando a um tempo e o sono começa a vir"

    #cara de cansado, tipo gatinho sem bateria

    jogador "Nossa...estou com muito sono..."

    #meio determinado

    jogador "Mas tenho que continuar"

    #portal aparece e puxa ele para outra dimensão
    #(cenário 1 e 2 cutscene com opção de botão de skip para pular a história toda para a próxima cena)

    
    jump hub_controle_1


#No sonho já
label hub_controle_1:

    scene expression Transform("bg hub", fit="cover") with pixellate

    android "Bem vindo, [jogador]! Estive esperando por você."

    jogador "Onde estou? Quem é você? como saio daqui?"

    android "Você está no Hub de Controle, sou GIBA - Guardião Integrado de Bases Avançadas. Você caiu aqui porque sua mente começou a colapsar sob o peso do simulado final."

    jogador "Simulado...? O curso... o diploma!"

    android "Exato. Você absorveu os dados, mas não os organizou. Sua lógica está fragmentada, dividida em cinco blocos principais."

    jogador "Preciso sair daqui!"

    #aparece o mapa e o totem sem joias

    android "Cada portal leva a um setor do seu aprendizado. Para restaurar seu código mental, você deve dominar cada conceito — não apenas lembrar, mas compreender. E ao fazê-lo, você conquistará a chance de voltar para casa."

    jogador "Como assim?"

    android "Fragmentos do seu próprio código-fonte. Ao passar pelos 5 universos, você reativará seu núcleo racional. E então, poderá despertar."

    android "Conquiste os cinco universos e mostre aos desafiadores que você é digno, boa sorte!"

    jump digital