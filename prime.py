count=0
n=int(input("Enter the Value:"))
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print(n,"prime")
else:
    print(n,"not prime")