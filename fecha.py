from datetime import datetime


def dia():
    dia = datetime.now()
    dia_hoy = dia.strftime("%Y/%m/%d")
    return dia_hoy

print(dia())