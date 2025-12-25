#planta (atualmente) 4 tipos de entidades, dividindo o terreno de forma igual, parecendo um sorvete Napolitano

#TODO: Tem um remendo comentado na linha 61

def napolitano(q_faixas, enable_girasol, enable_madeira, enable_feno, enable_cenoura): #q_faixas é a quantidade de faixas de cada tipo que vai ser plantada, é passada pela main

	#planta girassóis
	if enable_girasol:
		for i in range(q_faixas):
			for j in range(get_world_size()):

				#se puder colher, colha
				if can_harvest():
					harvest()
				
				#are a terra, caso nescessário
				if get_ground_type() == Grounds.Grassland:
					till()

				#plante o girassól
				plant(Entities.Sunflower)

				#vá para cima
				move(North)

			#vá pra direita
			move(East)
	
	#planta e colhe o arbusto/árvore
	if enable_madeira:
		for i in range(q_faixas):
			for j in range(get_world_size()):
					
				#se puder colher, colha
				if can_harvest():
					harvest()
			
				#verifica se vai plantar árvore ou arbusto
				if (get_pos_x() + get_pos_y()) % 2 == 0:
					plant(Entities.Tree)

					#Ague ela
					nivelDeAgua = get_water()
					if nivelDeAgua < 0.25:
						use_item(Items.Water)
				else:
					plant(Entities.Bush)
				
				#vá para cima
				move(North)

			#vá para a direita
			move(East)
			
	#colhe o feno/grama, não precisa plantar a grama
	if enable_feno:
		for i in range(q_faixas):
			for j in range(get_world_size()):
				
				#se puder colher, colha
				if can_harvest():
					harvest()

				#REMENDO
				#are o solo para nascer a grama
				#if get_ground_type() == Grounds.Soil:
					#till()

				#vá para cima
				move(North)

			#vá para a direita
			move(East)

	#planta e colhe a cenoura
	if enable_cenoura:
		for i in range(q_faixas):
			for j in range(get_world_size()):
				
				#se puder colher, colha
				if can_harvest():
					harvest()
					
				#se tiver que arar, are
				if get_ground_type()== Grounds.Grassland:
					till()
					
				#plante a cenoura
				plant(Entities.Carrot)

				#Ague ela
				nivelDeAgua = get_water()
				if nivelDeAgua < 0.25:
					use_item(Items.Water)
				
				#vá para cima
				move(North)

			#vá para a direita
			move(East)
