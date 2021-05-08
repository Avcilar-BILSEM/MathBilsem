from .rootfunctions import *
class Averages:
    """Ertuğrul bu sınıfı yaz"""
    def __init__(self):
        pass

    def Standart(self,*args):
        if isinstance (args[0], (int, float)):
            numbers = args
        else:
            numbers = args[0]
        return sum(numbers)/len(numbers)

    def Geometric(self,*args):
        if isinstance (args[0], (int, float)):
            numbers=args
        else:
            numbers=args[0]
        carpim=1
        for number in numbers:
            carpim=carp(carpim,number)
        return ust(carpim,1/len(numbers))

    def Harmonic(self, *args):
        if isinstance (args[0], (int, float)):
            numbers = args
        else:
            numbers = args[0]

        toplam=0
        for number in numbers:
            toplam+=1/number

        return len(numbers)/(toplam)

