def check_strings(sender, receiver):
    return sender == receiver
sender = str(input())
print(id(sender))
receiver=str(sender)
if sender==receiver:
    print(check_strings(sender, receiver)) 
else:
    print(check_strings(sender, receiver))