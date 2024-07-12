class Teacher:
    def __init__(self,name,regno):
        self.name=name
        self.registernumber=regno
    def display(self):
        print(self.name)
        print(self.registernumber)
t1=Teacher("alive","1")
t2=Teacher("heaven","2")
t1.display()
t2.display()
