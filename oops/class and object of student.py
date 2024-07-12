class student:
    def __init__(self):
        self.name=""
        self.register=""
    def display(self):
        print(self.name)
        print(self.register)
a=student()
b=student()
a.name="kabish"
b.name="bobby"
a.register=232028
b.register=6539
a.display()
b.display()