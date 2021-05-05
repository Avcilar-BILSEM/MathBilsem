import random

class Temel:

    def __init__(self):
        pass

    def __del__(self):
        pass

    def topla(self,*args):
        if isinstance (args[0], (int, float)):
            numbers = args
        else:
            numbers = args[0]
        return sum(numbers)

    def carp(self,*args):
        if isinstance (args[0], (int, float)):
            numbers = args
        else:
            numbers = args[0]
        carpim=1
        for number in numbers:
            carpim*=number
        return carpim

    def bol(self,*args):
        return args[0]/args[1]

    def cikar(self,*args):
        return args[0] - args[1]

    def kok(self,sayi,ust):
        return sayi**(1/ust)

    def ust(self,sayi,ust):
        return sayi**ust

    def rasgeleListe(self,elemansayisi,basla=0,bit=100):
        liste=[]
        for i in range(0,elemansayisi):
            liste.append(random.randrange(basla,bit))
        return liste