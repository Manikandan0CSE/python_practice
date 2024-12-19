def check_and_duplicate_vowels(strings):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    result = []

    for string in strings:
        if any(char in vowels for char in string):
            result.append(string)
    for item in result:
        print(item)
string_list = ["my","friend","is","death"]
print(string_list)
check_and_duplicate_vowels(string_list)

# a=[]
# count=0
# temp=str(input())
# a.append(temp)
# print(a)
