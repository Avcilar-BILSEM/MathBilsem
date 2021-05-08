from .Temel import Temel
Temel=Temel()
class Series():

    def __init__(self):
        self.asal=[2]
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

    def createArithmetic(self,bas,son, artis):
        self.dizi = []
        for i in range (bas, son + 1, artis):
           self.dizi.append (i)
        return self.dizi

    def createGeometric(self, bas, terim, kat):
        self.dizi = [bas]
        for i in range(1, terim + 1):
            self.dizi.append(self.dizi[-1] * kat)
        return self.dizi

    def asalSayilar(self,bit):
        if self.asal[-1]<bit:
            for i in range(self.asal[-1]+1,bit):
                bolundu=False
                for j in range(2,i):
                    if i%j==0:
                        bolundu=True
                        break
                if bolundu==False:
                    self.asal.append(i)
        return [item for item in self.asal if item < bit]
