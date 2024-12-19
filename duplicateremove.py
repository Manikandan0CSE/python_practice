a=[]
b=[]
for temp in range(1,5):
    temp=str(input())
    a.append(temp)
print(a)
for list in a:
    if list not in b:
        b.append(list)
print(b)
