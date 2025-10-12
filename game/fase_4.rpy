################### FASE 4 ###############################


label medieval:    

    personagem "Olá, [jogador]! Seja bem-vindo ao Universo de Funções e Modularização!"

    jogador "E quem é você?"

    personagem "Serei o seu desafiante, caso passe pelos meus desafios e lhe darei a jóia necessária para voltar pra casa"

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

label medieval_quiz:

    #####ver como resolver esse negocio de passar ou não dependendo do acerto e erro


## Se passar

label medieval_feliz:

    $ fase_5_liberada = True

    personagem "Parabéns, [jogador]! Você concluiu sua quarta missão no universo e merece seu prêmio"

    #mostra a joia la

    jogador "Finalmente! Só mais uma e posso ir pra casa!"

    jump hub_controle_5_feliz


## Se não passar

label medieval_triste:

    personagem "Infelizmente você não está pronto, mas você pode tentar novamente!"

    #corta pro hub
    jump hub_controle_5_triste


## Fase 1 e 2 e 3 e 4 e 5 liberada

label hub_controle_5_feliz:

    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"

    jogador "Pode vir!!"

    show screen MapUI


## Fase 1 e 2 e 3 e 4 liberada

label hub_controle_5_triste:

    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente"

    jogador "Não vou desistir! Estou muito perto de conseguir!"

    show screen MapUI
