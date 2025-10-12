################### FASE 3 ###############################


label marinho:

    pedro "Olá, [jogador]! Seja bem-vindo ao Universo de Estruturas de Repetição!"

    jogador "E quem é você?"

    pedro "Serei o seu desafiante, caso passe pelos meus desafios e lhe darei a jóia necessária para voltar pra casa"

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

label marinho_quiz:

    #####ver como resolver esse negocio de passar ou não dependendo do acerto e erro


## Se passar

label marinho_feliz:

    $ fase_4_liberada = True

    pedro "Parabéns, [jogador]! Você concluiu sua terceira missão no universo e merece seu prêmio"

    #mostra a joia la

    jogador "Finalmente! Falta pouco!"

    jump hub_controle_4_feliz


## Se não passar

label marinho_triste:

    pedro "Infelizmente você não está pronto, mas você pode tentar novamente!"

    #corta pro hub

    jump hub_controle_4_triste


## Fase 1 e 2 e 3 e 4 liberada

label hub_controle_4_feliz:

    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"

    jogador "Pode vir! Estou muito perto do meu objetivo!"

    show screen MapUI


## Fase 1 e 2 e 3 liberada
 
label hub_controle_4_triste:

    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente"

    jogador "Não vou desistir! Estou muito perto de conseguir!"

    show screen MapUI