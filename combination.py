from itertools import combinations
def sub_list(lists):
    subs=[]
    for i in range(0,len(lists)+1):
        temp =[list(x) for x in combinations(lists,i)]
        if len(temp)>0:
            subs.extend(temp)
    return subs
a=[10,1,2]
print("Original List:")
print(a)
print("Sublist:")
print(sub_list(a))