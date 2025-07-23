
#juego del ahorcado
from random import choice

palabras = ['panadero','dinosaurio','helipuerto','tiburon']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False


def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida,letras_unicas


def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No escogiste bien la letra")
    return letra_elegida


def mostrar_nuevo_tablero(palabra_elegida):

    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')
    print(''.join(lista_oculta))


def chequear_letra(letras_elegida, palabra_oculta, vidas,coincidencias):

    fin= False

    if letras_elegida in palabra_oculta:
        letras_correctas.append(letras_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letras_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letra_unicas:
        fin = ganar(palabra_oculta)

    return vidas,fin,coincidencias


def perder():
    print('te quedaste sin vida')
    print('la palabra oculta es ' + palabra)

    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print('felicitaciones ganaste encontraste la palabra!!')

    return True


palabra, letra_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 +'\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('letras incorrectas' + '-'.join(letras_incorrectas))
    print(f'vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letras= pedir_letra()

    intentos,terminado,aciertos = chequear_letra(letras,palabra,intentos,aciertos)

    juego_terminado = terminado
    
    
