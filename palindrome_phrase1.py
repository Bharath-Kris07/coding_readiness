def checkPalin(s):
    p=''
    for i in s:
        if i.isalnum():
            p+=i.lower()
    return p==p[::-1]
s=input("Enter the string: ")
if checkPalin(s):
    print("They are palindrome")
else:
    print("They are not palindrome")