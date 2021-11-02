import os
for nomePasta, subpastas, arquivos in os.walk("/home/jario/"):
	for arquivo in arquivos:
		if arquivo.endswith(".pdf"):
			print(arquivo)


