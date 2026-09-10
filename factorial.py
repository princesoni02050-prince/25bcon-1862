#code 1
n=5
fact=1
for i in range(1,n+1):
  fact *=i
print(fact)
#code2
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
#code3
name=[]
roll=[]
marks=[]
student={"name":name,'roll':roll,"marks":marks}
name.append("rahul")
roll.append(101)
marks.append(87.5)
for i in student.values():
    print(i[0],"\n")