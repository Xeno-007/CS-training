def peak(arr,n):
    l=0
    r=n-1
    while l<=r:
        mid=(l+r)>>1
        if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid+1]<+arr[mid]):
            break
        if mid>0 and arr[mid-1]>arr[mid]:
            r=mid-1
        else:
            l=mid+1
    return(mid)

arr=[]
n=int(input("Enter size"))
for i in range(n):
    a=int(input("Enter elements"))
    arr.append(a)
print(peak(arr,n))
