a=5
b=5
for i in range(1,a+1):
    for j in range(1,a+1):
        if(i!=2 and i!=3 and i!=4 or j>4):
            print("*",end="")
    print()