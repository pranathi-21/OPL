class num:
        def __init__(self,var1):
                 self.var1= var1
	def __str__(self):
                 
		 return str(self.var1)
        def res(self):
             return self.var1
class add:
	def __init__(self, param1, param2):
        	self.param1= param1
       		self.param2= param2 
                
        def __str__(self):
		
                return "("+ str(self.param1) + " + " + str(self.param2) +")"
        def res(self):
           return self.param1.res() + self.param2.res()
class mul:
        def __init__(self, d,k):
                  self.d=d
                  self.k=k
	

            
        def __str__ (self):
	        return "("+str(self.d) + "* " + str(self.k)+")"
        def res(self):
           return self.d.res()+self.k.res()
v=(add(mul(num(1) ,num(2)),num(3)))
print(v.res())
print(add(mul(num(-1),num(-2)),num(4)))
print(mul(mul(add(num(-2),num(2)),num(5)),num(10)))
print(mul(mul(mul(num(5),num(2)),num(6)),num(10)))
print add(num(4) ,num(9))
print mul(num(-4),num(-6))
print add(add(num(-2) ,num(-2)),num(-2))
print (add(add(mul(num(0) ,num(-1)), num(7)),num(-10)))
print (mul(add(mul(add(mul(num(1),num(0)),num(3)),num(4)),num(7)),num(10))) 
print num(2)
print (add(mul(add(mul(add(num(1),num(0)),num(3)),num(4)),num(7)),num(10))) 
print (add(add(mul(mul(num(1),num(2)),num(2)),num(10)),num(10)))
print  add(  mul( mul (add(num(1),num(2)),add(num(4) ,num(5))),num(7)),mul(num(1),num(2)))



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


def desugar(se):
    if isinstance(se,Cons):
        if isinstance(se.l,Atom):
            if se.l.v=="+":
                return add(desugar(se.r.l),desugar(se.r.r.l))
            if se.l.v=="*":
                return mul(desugar(se.r.l),desugar(se.r.r.l))
           
    elif isinstance(se,Atom):
        return number(int(se.v))

sexpr="cons(atom('+'),cons(atom('3'),cons(atom('5'),empty())))"

print(sexpr)

sexpr1="cons(atom('*'),cons(atom('+')(cons(atom('-2'),cons(atom('2')),con(atom('5'),empty())))"
sexpr2="cons(atom('*')cons(atom('4'),cons(atom('6'),empty())))"
sexpr3="cons(atom('+'),cons(atom('*')(cons(atom('3'),cons(atom('4')),con(atom('8'),empty())))"
sexpr4="cons(atom('*'),cons(atom('*'),(cons(atom('+')(cons(atom('4'),cons(atom('5')),con(atom('2')),con(atom('1'),empty())))"
sexpr5="cons(atom('*')cons(atom('4'),cons(atom('7'),empty())))"
sexpr6="cons(atom('5'))"
print(sexpr)
print(sexpr1)
print(sexpr2)
print(sexpr3)
print(sexpr4)
print(sexpr5)





