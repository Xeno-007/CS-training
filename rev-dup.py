c=input("Enter string")
s=c[::-1]

p=""
for i in s:
    if i not in p:
        p=p+i
print(p)







