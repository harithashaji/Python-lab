class rectangle:
    def __init__(self,l1,b1):
        self.l=l1
        self.b=b1
    def area(self):
        return(self.l*self.b)
    def peri(self):
        print("perimeter",(2*(self.l+self.b)))
    def compare(self,obj):
        if(self.area()==obj.area()):
            print("equal")
        else:
            print("not equal")
x1 = rectangle(3, 2)
a=x1.area()
print("area",a)
x1.peri()
x2 = rectangle(2, 2)
b=x2.area()
print("area",b)
x1.compare(x2)
