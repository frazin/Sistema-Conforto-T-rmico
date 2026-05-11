def classificar_conforto(temperatura, umidade):

    if temperatura <= 5:
        return "Muito Frio"

    elif temperatura >= 35:
        return "Muito Quente"

    elif umidade <= 30:
        return "Muito Seco"

    elif umidade >= 80:
        return "Muito Úmido"

    elif 10 <= temperatura < 20 and 30 < umidade < 80:
        return "Precisa de Sol para Conforto"

    elif 20 <= temperatura <= 25 and 30 < umidade < 80:
        return "Confortável"

    elif 25 < temperatura < 35 and 30 < umidade < 80:
        return "Precisa de Vento para Conforto"

    elif 10 <= temperatura <= 32 and 30 < umidade < 80:
        return "Confortável (Zona Adaptativa)"

    else:
        return "Indefinido"