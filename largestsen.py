a=[]
count=0
for temp in range(1,5):
    temp=str(input())
    a.append(temp)
h= max(a,key=len)
print(h)
