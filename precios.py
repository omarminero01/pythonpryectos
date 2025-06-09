precios_de_cervezas =[('regia',1.50),('pilsener',1.80),('corona',1.75)]

def cerveza_mas_cara (lista_precios):
    precio_mayor = 0
    cerveza_mas_cara = ""

    for cerveza,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cerveza_mas_cara = cerveza
        else:
            pass


    return (cerveza_mas_cara,precio_mayor)


print(cerveza_mas_cara(precios_de_cervezas))

