ps=0
ns=0
n=int(input("enter no:"))
for i in range(n):
    a=int(input())
    if a>0:
        ps=ps+a
    else:
        ns=ns-a
print(ps)
print(ns)