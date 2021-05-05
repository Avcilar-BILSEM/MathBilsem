def topla (*args):
    if isinstance (args[0], (int, float)):
        numbers = args
    else:
        numbers = args[0]
    return sum (numbers)


def carp( *args):
    if isinstance (args[0], (int, float)):
        numbers = args
    else:
        numbers = args[0]
    carpim = 1
    for number in numbers:
        carpim *= number
    return carpim


def bol( *args):
    return args[0] / args[1]


def cikar(*args):
    return args[0] - args[1]


def kok(sayi, ust):
    return sayi ** (1 / ust)


def ust (sayi, ust):
    return sayi ** ust