user_list=int(input("Enter the VALUE:"))
a=[]
count=0
for i in range(user_list):
    temp=int(input())
    a.append(temp)
print(a)
dub={x for x in a if a.count(x)>1}
print(len(dub))