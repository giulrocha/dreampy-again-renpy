#Parte Indrodutória comum a todas as dificuldades

image bg intro = "images/background/bg classroom.png"
image gilberto_1 = "images/characters/gilberto_1.png"
image aluna = "images/characters/aluna_andando.png"
image aluno = "images/characters/aluno_normal.png"
image giulie = "images/characters/giulie_feliz.png"
image luan = "images/characters/luan_feliz.png"
image yasmim = "images/characters/yasmim_feliz.png"

label intro:

    #cena da sala de aula
    scene expression Transform("bg intro", fit="cover") with fade

    show gilberto_1 at Position(xpos=0.56, ypos=0.58, xanchor=0.5, yanchor=1.0)
    if jogador == "aluna":
        show aluna at Position(xpos=0.30, ypos=0.84, xanchor=0.5, yanchor=1.0)
    else:
        show aluno at Position(xpos=0.30, ypos=0.74, xanchor=0.5, yanchor=1.0)
    show giulie at Position(xpos=0.38, ypos=0.84, xanchor=0.5, yanchor=1.0)
    show yasmim at Position(xpos=0.54, ypos=0.84, xanchor=0.5, yanchor=1.0)
    show luan   at Position(xpos=0.46, ypos=0.84, xanchor=0.5, yanchor=1.0)


    #aparece o professor e alunos

    professor_gilberto "Alunos, informo que o simulado final para conclusão do curso é amanhã! Espero que estejam preparados para mais esse desafio, não me decepcionem!"

    #aparece so alunos, foca neles

    jogador "Nossa… tenho que revisar urgentemente tudo! Havia esquecido que a prova estava tão perto!"

    aluno_1 "Calma, esquecer faz parte da emoção da reta final! Estudar com um pouco de pressão até me ajuda a focar melhor."

    aluno_2 "Ih, lá vem ela com esse papo! Essa aí já devia estar dando aula com o professor Gilberto. Vive acertando tudo! Se eu tirar metade da sua nota, já tô comemorando com bolo e guaraná."
    
    aluno_1 "Que isso, só tento não surtar… muito."

    aluno_3 "Então tá fazendo errado, porque surtar é meu plano A! Inclusive, se alguém achar minha calma por aí, favor devolver antes da prova!"

    jogador "Vou logo para casa e virar a noite estudando..."

    scene bg bedroom with pixellate

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

    #cena do hub e do android

    android "Bem vindo, [jogador]! Estive esperando por você."

    jogador "Onde estou? Quem é você? como saio daqui?"

    android "Você está no (a decidir), sou GIBA - Guardião Integrado de Bases Avançadas. Você caiu aqui porque sua mente começou a colapsar sob o peso do simulado final."

    jogador "Simulado...? O curso... o diploma!"

    android "Exato. Você absorveu os dados, mas não os organizou. Sua lógica está fragmentada, dividida em cinco blocos principais."

    jogador "Preciso sair daqui!"

    #aparece o mapa e o totem sem joias

    android "Cada portal leva a um setor do seu aprendizado. Para restaurar seu código mental, você deve dominar cada conceito — não apenas lembrar, mas compreender. E ao fazê-lo, você conquistará uma jóia de conhecimento."

    jogador "Jóia?"

    android "Fragmentos do seu próprio código-fonte. Ao reunir as cinco, você reativará seu núcleo racional. E então, poderá despertar."

    #mostra as joais de fato, como elas são

    android "Conquiste as jóais e mostre aos desafiadores que você é digno, boa sorte!"

    #primeira portal fica disponível para clicar no mapa.

    jump digital