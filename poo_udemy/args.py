def multiiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


def par_impar(valor):
    multipl0_de_2 = valor % 2 == 0

    if multipl0_de_2:
        return f'{valor} é par'
    return f'{valor} é ímpar'

# resultado = multiiplicar(1, 2, 3, 4, 5)
resultado = multiiplicar(1, 3)
par_impar(resultado)