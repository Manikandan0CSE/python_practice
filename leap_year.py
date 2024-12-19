year=int(input("Enter:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("leap year")
else:
    print("isn't leap year")