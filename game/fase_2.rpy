################### FASE 2 ###############################


label cyberpunk:

    vanilton "Olá, [jogador]! Seja bem-vindo ao Universo de Lógica e Estrutura Condicionais!"

    jogador "E quem é você?"

    vanilton "Serei o seu desafiante, caso passe pelos meus desafios e lhe darei a jóia necessária para voltar pra casa"

    jogador "Aceito seu desafio!"    

    if difficulty == "easy":
        $ perguntas_totais = 10
        $ acertos_para_passar = 7

        jump quiz_digital  #### quiz facil, depois vê como coloca
    
    elif difficulty == "normal":
        $ perguntas_totais = 10
        $ acertos_para_passar = 7
        
        jump quiz_digital    #### quiz normal, depois vê como coloca

    else:
        $ perguntas_totais = 10
        $ acertos_para_passar = 7
        
        jump quiz_digital     #### quiz dificil, depois vê como coloca

label quiz_cyberpunk:

    #####ver como resolver esse negocio de passar ou não dependendo do acerto e erro


## Se passar

label cyberpunk_feliz:

    $ fase_3_liberada = True

    vanilton "Parabéns, [jogador]! Você concluiu sua segunda missão no universo e merece seu prêmio"

    #mostra a joia la

    jogador "Finalmente! Falta pouco!"

    jump hub_controle_3_feliz


## Se não passar

label cyberpunk_triste:

    vanilton "Infelizmente você não está pronto, mas você pode tentar novamente!"

    #corta pro hub

    jump hub_controle_3_triste


## Fase 1 e 2 e 3 liberada

label hub_controle_3_feliz:
    
    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"

    jogador "Pode vir! Estou pronto"

    show screen MapUI


## Fase 1 e 2 liberada

label hub_controle_3_triste:
    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente"

    jogador "Não vou desistir!"

    show screen MapUI