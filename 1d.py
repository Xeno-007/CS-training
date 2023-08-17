n=int(input("Enter the size of the array"))
m=[]
a=[]
c=0
print("Enter the elemnts")
for i in range(n):
    m.append(int(input()))
for i in range(n):
    if m[i]!=0:
        a.append(m[i])
    else:
        c=c+1
for i in range(c):
    a.append(0)

print(a)