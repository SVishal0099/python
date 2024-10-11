class Rect:
    def __init__(self,l2,w2):
        self.l=l2
        self.w=w2
    def RectArea(self):
        self.a=self.l * self.w
        print("Area of Rectangle:", self.a)
    def RectPer(self):
        self.p=2*(self.l + self.w)
        print("Perimeter of Rectangle:", self.p)
l1=int(input("Enter Length:"))
w1=int(input("Enter Width:"))
Obj=Rect(l1,w1)
Obj.RectArea()
Obj.RectPer()