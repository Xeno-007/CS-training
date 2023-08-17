m = []
r = int(input("Enter number of rows:"))
c = int(input("Enter number of colomns:"))
i = 0
j = 0
print("Enter the elements")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    m.append(a)
for i in range(r):
    for j in range(c):
        print(m[i][j], end=" ")
    print()

print("Diagonal")
for i in range(r):
    for j in range(c):
        if(i!=j and i<j):

            print(m[i][j], end=" ")
