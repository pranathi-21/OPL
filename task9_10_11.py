x=prim('GTE',2,2)

print(x.val())
y=ifs(7>4,4,5)
ty=prim('>',7,4)
print(ty.val())
print(y.res())



Task 10,9



ls=list()
ls=['+','*','-','/','LT','LTE','=','GTE','GT']

def desugar(sexpr):
    if isinstance(sexpr,Cons):
        if isinstance(sexpr.left,atom):
            if(sexpr.left.val=='if'):
                return ifs(desugar(sexpr.right.left),desugar(sexpr.right.right.left),desugar(sexpr.right.right.right.left))
            if(sexpr.left.val in ls):
                return
                #if sexpr.left.val=='+':
                    #return prim(Var(sexpr.left),desugar(sexpr.right.left),desugar(sexpr.right.right,left))
            if(sexpr.left.val=='true'):
                return (sexpr.left.val)
            if(sexpr.left.val=='false'):
                return(sexpr.left.val)
            if(sexpr.left.val in range(2147483647)):
                return(sexpr.left.val)
            
    else:
        return(Var(sexpr.val))
        
           

#Extending Desugar to J1 programs
sexprobj=Cons(atom('if'),(Cons(Cons(atom('if'),(Cons(atom('<'),Cons(atom(3),Cons(atom(3),mt))))),Cons(atom(5),Cons(atom(6),mt)))))
um1=desugar(sexprobj)
print(um1)       

