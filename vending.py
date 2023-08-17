m=200
s=70
def check(x,s):
    if x <=s:
        return True

    else:
        return False
while True:
    x=int(input("How many pepsi"))

    if check(x,s):
        print("Take it \n"*x)
        print("have a good drink \n")
        s=s-x
    else:
        print("Not Enough \n" * x)
        print("have a good drink \n")