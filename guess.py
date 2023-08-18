import random
x=random.randint(0,10)
while True:
    c=int(input("guess:"))
    if c<x:
        print("LOW")
    elif c>x:
        print("HIGH")
    else:
        print("Correct")
        break
