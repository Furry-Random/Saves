#ela foi construída pra plantar
#bush, se for plantar cenoura por
#exemplo, então tem que modificar
#a função

def one_type():

	tamanhoFazenda = get_world_size()
	planta = Entities.Bush
	
	for i in range(tamanhoFazenda):
		if can_harvest():
			harvest()
		
		#comente a linha abaixo
		#para colher grama
		#plant(planta)
		move(North)
			
	move(East)