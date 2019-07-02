ls3=[]
ls4=[]
class Eif:
    def __init__(self,eop1,eop2,eop3):
        self.eop1=eop1
        self.eop2=eop2
        self.eop3=eop3
    def redex(self):
        c1=eval('(self.eop1)')
        return c1,self.eop2,self.eop3
    def res(self):
        c=eval('(self.eop1)')
        if c==True:
            return(self.eop2)
        else:
            return(self.eop3)
    
class Ehole:
    def __init__(self):
        return None
def ce(*stri):
    for i in stri:
        if(i=='E'):
            ls1=i
            return ls3
        else:
            return ls4
sexprobj = Eif(4>2,9,10)

print(sexprobj.redex())
print(sexprobj.res())
