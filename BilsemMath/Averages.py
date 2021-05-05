class Averages:
    """Ertuğrul bu sınıfı yaz"""
    def __init__(self):
        pass

    def Standart(self,*args):
        if isinstance(args[0],(int,float)):
            return sum(args)/len(args)
        else:
            return sum(args[0])/len(args[0])