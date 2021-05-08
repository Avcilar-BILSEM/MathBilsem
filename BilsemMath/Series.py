from .Temel import Temel
Temel=Temel()
class Series():

    def __init__(self):

        self.fibb = [0,1]
        self.teksayilar=[1]
        self.ciftsayilar = [2]

    def fibonacci(self,n):
        if len(self.fibb)<n:
            for i in range(len(self.fibb),n+1):
                self.fibb.append(Temel.topla(self.fibb[i-2],self.fibb[i-1]))
        return self.fibb[0:n]

    def goldenRatio(self,n):
        if len(self.fibb)<n:
            self.fibonacci(n)
        return self.fibb[n]/self.fibb[n-1]

    def odd(self,n):
        if n>self.teksayilar[-1]:
            for i in range(self.teksayilar[-1]+2,n+1,2):
                self.teksayilar.append(i)
        return self.teksayilar[0:n]

    def even(self,n):
        if n>self.ciftsayilar[-1]:
            for i in range(self.ciftsayilar[-1]+2,n+1,2):
                self.ciftsayilar.append(i)
        return self.ciftsayilar[0:n]

    def create(self,a,b,c,bas,son):
        if c - b == b - a:
            self.dizi = [bas]
            for i in range (bas, son + 1):
                self.dizi.append (self.dizi[-1] + (b - a))

        elif c / b == b / a:
            self.dizi = [bas]
            for i in range (bas, son + 1):
                self.dizi.append (self.dizi[-1] * (b / a))
        return self.dizi


