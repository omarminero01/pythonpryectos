def letras_unicas(palabra):
    mi_set = set()
    
    for letra in palabra:
        mi_set.add(letra)
    mi_lista = list(mi_set)
    mi_lista.sort()
    return mi_lista

print(letras_unicas("unamalabrasmaslargaquelasdemas"))