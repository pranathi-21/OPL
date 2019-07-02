#8th task
class Node:
       def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class cons:
       def __init__(self,con1,con2):
        self.con1 = con1
        self.con2=con2
        def pr(self):
            return self.con1.pr()
            return self.con2.pr()
class atom:
       def __init__(self,atom):
           self.atom=atom
       def pr(self):
             return self.atom.pr()
class empty:
       def __init__(self):
            return 

class ifs:
    def __init__(self,op1,op2,op3):
        self.op1=op1
        self.op2=op2
        self.op3=op3
    def __str__(self):
        return  'if('+str(self.op1)+' '+str(self.op2)+' '+str(self.op3)+')'
    def res(self):
        c=eval('(self.op1)')
        if c==True:
            return(self.op2)
        else:
            return(self.op3)
        
        
    
class Bool:
    def __init__(self,b):
        self.b=b
    def __str__(self):
        return  str(self.b)
    def res(self):
        return eval('(self.b)')
x=Bool(True)
print(x.res())




class prim:
    def __init__(self,sym,o1,o2):
        self.sym=sym
        self.o1=o1
        self.o2=o2
    def __str__(self):
        return  str( '(' + str(self.o1) + str(self.sym) + str(self.o2) + ')')
        

    
    def val(self):
        if(self.sym =='+'):
            z=eval('(self.o1 + self.o2)')
            print(z)
            return eval('(self.o1 + self.o2)')
        
        if(self.sym =='*'):
            return eval('(self.o1 * self.o2)')
        
        if(self.sym =='/'):
            return eval('(self.o1 / self.o2)')
        
        if(self.sym =='-'):
        
            return eval('(self.o1 - self.o2)')
        
        if(self.sym =='='):
            return eval('(self.o1 = self.o2)')
        
        if(self.sym =='LT'):
            return eval('(self.o1 < self.o2)')
        if(self.sym =='GT'):
            return eval('(self.o1 > self.o2)')
        if(self.sym =='LTE'):
            return eval('(self.o1 <= self.o2)')
        if(self.sym =='GTE'):
            qw=eval('(self.o1 >= self.o2)')
            print(qw)
            return eval('(self.o1 >= self.o2)')
        if(self.sym   =='True:'):
            return eval('(self.o1)')
        if(self.sym   =='False'):
            return eval('(self.o2)')



def e(*dox):
    for i in dox:
        ls=i
    return(ls) 

   
class Var:
    def __init__(self, x):
        self.x =x
    def __str__(self):
        return  str(self.x)
    def val(self):
        return int(self.x)
