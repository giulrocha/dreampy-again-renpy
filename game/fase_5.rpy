################### FASE 5 ###############################


label alienigena:    

    personagem "Olá, [jogador]! Seja bem-vindo ao Universo de Listas e Dicionários!"

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

label alienigena_quiz:

    #####ver como resolver esse negocio de passar ou não dependendo do acerto e erro


## Se passar

label alienigena_feliz:

    $ volta_pra_casa = True

    personagem "Parabéns, [jogador]! Você concluiu sua última missão no universo e merece seu prêmio"

    #mostra a joia la

    jogador "Finalmente! Agora posso ir pra casa!"

    jump hub_controle_6_feliz


## Se não passar

label alienigena_triste:

    personagem "Infelizmente você não está pronto, mas você pode tentar novamente!"

    jogador "Nããããããããããoooooo"

    #corta pro hub
    jump hub_controle_6_triste


## Todas as fases liberadas, pode ir pra casa.

label hub_controle_6_feliz:

    android "Parabéns, [jogador]! Você reuniu todas as cinco Jóias de Conhecimento."
    android "Sua mente está restaurada. Você dominou variáveis, lógica, laços, funções e estruturas de dados."
    android "Está pronto para acordar… e enfrentar o verdadeiro desafio."

    jogador "Finalmente!! Estou livreeee!!"
    jogador "Obrigado, android. Eu aprendi que programar é mais do que decorar comandos — é entender como pensar de forma lógica."

    android "Exatamente. Vá, e mostre do que é capaz."

    show screen MapUI


## Todas as fases liberadas, não pode ir pra casa

label hub_controle_6_triste:
    android "Que pena [jogador], infelizmente não foi dessa vez. Mas você pode tentar novamente"

    jogador "Nããããããããããoooooo!"

    jogador "Eu estava tão perto!!"

    show screen MapUI