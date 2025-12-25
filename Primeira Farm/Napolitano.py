#o Napolitano só funciona se o get_world_size() for divisível por 3, já que são 3 tipos de plantas

#TODO: a minha fazenda atualmente é divisível por 4, então plante 4 tipos em 4 faixas

def napolitano():
	tamanhoFazenda = get_world_size()
		
	#verifica o tipo do solo
	soloType = get_ground_type()
		
	#planta e colhe a cenoura
	for i in range(get_world_size() / 3):
		for j in range(tamanhoFazenda):
			if can_harvest():
				harvest()
				
			if soloType == Grounds.Grassland:
				till()
				
			plant(Entities.Carrot)
			nivelDeAgua = get_water()
			if nivelDeAgua < 0.25:
				use_item(Items.Water)
			move(East)
		move(North)
	
	#planta e colhe o arbusto/árvore
	for i in range(get_world_size() / 3):
		for j in range(tamanhoFazenda):
				
			if can_harvest():
				harvest()
		
			#verifica se vai plantar árvore ou arbusto
			if (get_pos_x() + get_pos_y()) % 2 == 0:
				plant(Entities.Tree)
				nivelDeAgua = get_water()
				if nivelDeAgua < 0.25:
					use_item(Items.Water)
			else:
				plant(Entities.Bush)
			
			move(East)
		move(North)
			
	#colhe o feno/grama, não precisa plantar a grama
	for i in range(get_world_size() / 3):
		for j in range(tamanhoFazenda):
			
			if can_harvest():
				harvest()
				
			#plant(Entities.Grass)
			move(East)
		move(North)