arr=[]
n=int(input("Enter size"))
for i in range(n):
    a=int(input("Enter elements"))
    arr.append(a)
max=[]
for i in range(n):
    if(i==0):
        if(arr[i]>arr[i+1]):
            max.append(arr[i])

    if(arr[i]>arr[i-1] and arr[i]>arr[i+1]):
        max.append(arr[i])

    if (i == n):
        if (arr[i] > arr[i - 1]):
            max.append(arr[i])

print(max)