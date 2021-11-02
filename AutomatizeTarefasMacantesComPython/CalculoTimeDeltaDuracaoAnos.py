import datetime
print("Programa que calcula uma duração de aproximadamente 30 anos no tempo ".upper())

DataAtual = datetime.datetime.now()
print("Data atual é: ", DataAtual)
# Definimos  o numero de anos no caso aqui é 30 anos.
anos = datetime.timedelta(days=365 * 30)
# estamos supondo que há 365 dias em cada um desses anos.
print("30 anos atrás foi em:", DataAtual - anos)  # subtrai 30 anos atrás
# subtrai 30 anos * 2  = 60 anos atŕas.
print("60 anos atrás foi em: ", DataAtual - (2 * anos))
