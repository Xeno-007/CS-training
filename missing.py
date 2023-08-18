def find(arr,n):
    for i in range(1,n+1):
        flag=False

        for j in range(n-1):
            if arr[j]==i:
                flag=True
                break
            if flag== False:
                return i
arr=[-2,2,1,-3,2,10,0]
res=find(arr,len(arr))
print    (res)