#função feita apenas para farmar madeira, lá ele

def madeira():
	tamanhoFazenda = get_world_size()
	
	for i in range(tamanhoFazenda):
		if can_harvest():
			harvest()
		
		if (get_pos_x() + get_pos_y()) % 2 == 0:
			plant(Entities.Tree)
			nivelDeAgua = get_water()
			if nivelDeAgua == 0:
				use_item(Items.Water)
		else:
			plant(Entities.Bush)
			
		move(East)
	move(North)
	