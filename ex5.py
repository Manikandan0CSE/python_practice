user_list=int(input("Enter the VALUE:"))
a=[]
for i in range(user_list):
    temp=int(input())
    a.append(temp)
value=int(input("repeated value:"))
count=a.count(value)
print(count)
# seen = set()
# for item in a:
#     if item in seen:
#         print(item) 
#     else:
#         seen.add(item)
