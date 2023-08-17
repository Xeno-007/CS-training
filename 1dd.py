n=int(input("Enter the size of the array"))
m=[]
c=0
print("Enter the elemnts")
for i in range(n):
    m.append(int(input()))
i=0
while (i<n):
    if(m[i]==0):
        m.pop(i)
        m.append(0)
        i=i+1
print(m)