class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add",self.num1+self.num2)
    def sub(self):
        print("sub",self.num1-self.num2)
    def mul(self):
        print("mul",self.num1*self.num2)
    def div(self):
        print("div",self.num1/self.num2)
obj1=calculator(10,20)
obj2=calculator(2,3)
obj3=calculator(4,9)
obj4=calculator(4,2)

obj1.add()
obj2.sub()
obj3.mul()
obj4.div()
        