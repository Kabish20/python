class goa:
    name=""
    drink=""
    def party(self):
        print("lets party")
    def beach(self):
        print("enjoying in beach")
ramesh=goa()
suresh=goa()
ramesh.name="Ramesh"
suresh.name="Suresh"
ramesh.drink="YES"
suresh.drink="NO"
print("party enjoying person:",ramesh.name)
print("beach enjoying person:",suresh.name)
print(ramesh.drink)
print(suresh.drink)
ramesh.party()
suresh.beach() 