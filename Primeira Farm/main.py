#Importa os arquivos de código
import Madeira
import one_Type
import Napolitano
import Abobora

#reseta a fazenda
clear()

#muda a cor do chapéu para cinza (porquê é legal)
change_hat(Hats.Gray_Hat)

#minera pra sempre
while True:
					#girasóis, madeira, feno e cenoura, o parâmetro é 11 para dividir a fazenda no meio
	Napolitano.napolitano(11, False, True, True, False) #precisa da quantidade de faixas de plantação de cada tipo
	
	#one_Type.one_type()
	#Madeira.madeira()
	#Abobora.abobora()
