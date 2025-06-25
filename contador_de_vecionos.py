def cero_vecinos(*arg):

    contador = 0 

    for  num in args:
        if args [contador] == 0 and args [contador +1] == 0:
          return true

        else:
          contador += 1

    return False
print(cero_vecinos(1,2,1,5,5,5,4,6,4,))           