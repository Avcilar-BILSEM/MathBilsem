from .rootfunctions import *
from .Temel import Temel
"""a2+b2=c2
b2=c2-a2
a2=c2-b2
"""
Temel=Temel()

class Triangle:
    def __init__(self):
        pass

    def pisagor(self,a=False,b=False,c=False):
        if a!=False and b!=False:
            return [a,b,kok(ust(a)+ust(b))]
        elif a!=False and c!=False:
            return [a, kok(ust(c)-ust(a)), c]
        elif b!=False and c!=False:
            return [kok(ust(c)-ust(b)), b, c]

    def pisagorKoklu(self,a=False,b=False):
        c=ust(a)+ust(b)
        carpan_c=Temel.carpan(c)
        for key in carpan_c:
            carpan_c[key]=carpan_c[key]/2
        return carpan_c
