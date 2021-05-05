from .Temel import Temel
class Series:

    def __init__(self):
        self.fibb = [0,1]

    def fibonacci(self,n):
        if len(self.fibb)<n:
            for i in range(len(self.fibb),n+1):
                self.fibb.append(self.fibb[i-2]+self.fibb[i-1])
        return self.fibb[0:n]

    def goldenRatio(self,n):
        if len(self.fibb)<n:
            self.fibonacci(n)
        return self.fibb[n]/self.fibb[n-1]



