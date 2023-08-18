arr=[]
n=int(input("Enter size"))
for i in range(n):
    a=int(input("Enter elements"))
    arr.append(a)
for i in range(n):
    if((i==0 or arr[i-1]<arr[i])) and ((i==n or arr[i]>arr[i+1])):
        print(i, end=" ")