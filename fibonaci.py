n=10
a=0
b=1
next=None
for i in range(n):
    print(a,end=" ")
    next=a+b
    a=b
    b=next
print("\n")