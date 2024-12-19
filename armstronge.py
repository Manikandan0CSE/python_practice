n=int(input("Enter the value:"))
t=n
r=0
while(n>0):
    a=n%10
    r=r+a*a*a
    n=n//10
if r==t:
    print("Arm No")
else:
    print("not arm")
