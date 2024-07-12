start=int(input("enter the no:"))
end=int(input("enter the no:"))
for i in range(start,end+1):
    if i%4==0:
        print("leap year")
    else:
        print("its not a leap year")