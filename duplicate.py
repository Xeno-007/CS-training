n = int(input("Enter the size of the array: "))
m = []
print("Enter the elements:")
for i in range(n):
    m.append(int(input()))

i = 0
while i < n:
    j = i + 1
    while j < n:
        if m[i] == m[j]:
            for k in range(j, n - 1):
                m[k] = m[k + 1]
            n -= 1
        else:
            j += 1
    i += 1

print(m)