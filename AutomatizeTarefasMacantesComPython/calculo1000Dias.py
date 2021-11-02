import datetime
print("""
Programa que calcular a data correspondente a 1.000 dias a partir de agora.
Isso é útil porque, ao calcular 1.000 dias a partir de uma data
especificada, você deveria se lembrar de quantos dias há em cada mês e
considerar anos bissextos e outros detalhes intrincados. O módulo datetime
cuida de tudo isso para você.
""".upper()
      )

dt = datetime.datetime.now()
print("Data tual: ".upper(), dt)
mildias = datetime.timedelta(days=1000)
print("1000 dias apartir desta data se dará no dia:".upper(), dt+mildias)
