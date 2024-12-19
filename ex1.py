list_size = int(input("Enter list: "))  
user_list = [int(input(f"{i + 1}:")) for i in range(list_size)]
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
prime_numbers = [num for num in user_list if is_prime(num)]
print("Prime numbers:", prime_numbers)
s=sum(prime_numbers)
print("last list",s)
split_digits = [int(digit) for digit in str(s)]
t=sum(split_digits)
print(t)