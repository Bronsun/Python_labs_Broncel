class Zespolona:
    def __init__(self,rel=0,im=0):
        self.rel = rel
        self.im = im
    def __repr__(self):
        if self.rel == 0.0 and self.im == 0.0:
            return "0.00"
        if self.rel == 0:
            return "%.2fi" % self.im
        if self.im == 0:
            return "%.2f" % self.rel
        return "%.2f %s %.2fi" % (self.rel, "+" if self.im >= 0 else "-", abs(self.im))

    def __add__(self,other):
        return Zespolona(self.rel+other.rel,self.im+other.im)
    
    def __sub__(self,other):
        return Zespolona(self.rel-other.rel,self.im-other.im)

    def __mul__(self,other):
        return Zespolona(self.rel*other.rel-self.im*other.im,self.rel*other.rel+self.im*other.im)
    
    def __dif__(self,other):
        sr,si,op,oi = self.rel,self.im,other.rel,other.im # op is other rek
        r = float(op**2+oi**2)
        return Zespolona((sr*op+si*oi)/r, (si*op-sr*oi)/r)


        
            
        

       
       


  