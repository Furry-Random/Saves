#Código exclusivo para plantar e colher abóboras

#TODO: Ele não está percorrendo de forma correta
#TODO: Ele não colhe, mesmo quando cont = 36 (tamanho da minha fazenda)

#cria a função da abóbora
def abobora():

    #repete para todas as linhas
    for i in range(get_world_size()):

        #repete para todas as posições
        for j in range(get_world_size()):
            
            #verifica se é grama, se sim, colha (isso é pra farmar um pouco de grama no início da execução)
            if get_entity_type() == Entities.Grass:
                if can_harvest():
                    harvest()

            #verifica se o tipo do solo é um "grassland", se sim, então are
            if get_ground_type() == Grounds.Grassland:
                till()

            #verifica se o que está embaixo do drone é diferente de uma abóboraa, se sim, plante a abóbora
            if get_entity_type() != Entities.Pumpkin:
                plant(Entities.Pumpkin)

            #vá pra esquerda
            move(East)

        #vá pra cima
        move(North)

    #passa verificando se todas as posições tem abóboras prontas para colher
    cont = 0 #variável auxiliar para verificarmos se todas as posições tem abóboras boas

    #percorre as linhas
    for i in range(get_world_size()):

        #percorre as posições
        for j in range(get_world_size()):
            
            if get_entity_type() == Entities.Pumpkin:
                cont += 1

        #vá pra esquerda
        move(East)

    #vá pra cima
    move(North)

    #debug pra ver o valor do contador
    print(cont)

    #colha se todas as posições tiverem abóboras boas
    tamanho_fazenda = get_world_size()
    if cont == tamanho_fazenda * 2:
        harvest()