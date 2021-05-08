import random



class Temel:

    def __init__(self):
        self.asal=[2]

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

    def carpan(self,sayi):
        asallar=self.asalSayilar(sayi)
        asallar.append(sayi)

        durum=sayi
        carpanlar={}
        i=0
        while durum>1 and len(asallar)>0:
            carpan = asallar[i]
            if durum%carpan==0:
                durum=durum/carpan
                if carpan in carpanlar:
                    carpanlar[carpan]+=1
                else:
                    carpanlar[carpan]=1
            else:
                i+=1

        return carpanlar