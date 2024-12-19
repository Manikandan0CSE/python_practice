array=[55,43,23,45,54,10]
n=len(array)
for i in range(n):
    for j in range(0,n-i-1):
        if array[j] > array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
print(array)