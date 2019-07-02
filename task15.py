class Bool:
    def __init__(self,b):
        self.b=b
    def __str__(self):
        return  str(self.b)
    def res(self):
        return eval('(self.b)')


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
    def redex(self):
        c1=eval('(self.op1)')
        c2=eval('(self.op2)')
        c3=eval('(self.op3)')
        return(self.op1,self.op2,self.op3)
class prim:
    def __init__(self,sym,o1,o2):
        self.sym=sym
        self.o1=o1
        self.o2=o2
    def __str__(self):
        return  str( '(' + str(self.o1) + str(self.sym) + str(self.o2) + ')')
       

    
    def val(self):
        if(self.sym =='+'):
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
            return eval('(self.o1 >= self.o2)')
        if(self.sym   =='True:'):
            
            a= eval('(self.o1)')
            return(a)
        if(self.sym   =='False'):
            return eval('(self.o2)')


sexprobj = ifs(False,9>3,10)
print(sexprobj.redex())
print(sexprobj.res())


