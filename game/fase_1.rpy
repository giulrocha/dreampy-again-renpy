################### FASE 1 ###############################

label digital:

    #mostra universo digital e desafiador

    raimundo "Olá, [jogador]! Seja bem-vindo ao Universo de Variáveis!"

    jogador "Quem é você??"

    raimundo "Serei o seu desafiante, caso passe pelos meus desafios e lhe darei a jóia necessária para voltar pra casa"

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

label quiz_digital:

    $ acertos = 0  ## acho que começa com zero e ai vai incrementando

    #####ver como resolver esse negocio de passar ou não dependendo do acerto e erro

    if acertos >= acertos_para_passar:

        jump digital_feliz

    else:

        jump digital_triste



### Se passar    

label digital_feliz:

    $ fase_2_liberada = True

    raimundo "Parabéns, [jogador]! Você concluiu sua primeira missão no universo e merece seu prêmio"

    #mostra a joia la

    jogador "Finalmente!"

    jump hub_controle_2_feliz


## Se não passar

label digital_triste:

    raimundo "Infelizmente você não está pronto, mas você pode tentar novamente!"

    #corta pro hub

    jump hub_controle_2_triste


## Fase 1 e 2 liberada

label hub_controle_2_feliz:

    android "Parabéns [jogador]! Você conseguiu! Pode seguir para a próxima fase!"

    jogador "Pode vir! Estou pronto"

    show screen MapUI    ### pode tentar com call tbem se não rolar


## Fase 1 liberada

label hub_controle_2_triste:

    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente"

    jogador "Não vou desistir!"

    show screen MapUI