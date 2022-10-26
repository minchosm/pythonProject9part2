from functools import reduce
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def impar(numero):
    if numero % 2 != 0:
        return True


listaImpar = list(filter(impar, lista))
print(reduce(lambda x, y: x+y, listaImpar))