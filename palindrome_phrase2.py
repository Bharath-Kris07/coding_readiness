def checkPalin(s):
    L=0
    R=len(s)-1
    while L<R:
        if not s[L].isalnum():
            L+=1
        elif not s[R].isalnum():
            R-=1
        else:
            if s[L].lower() != s[R].lower():
                    return False
            L += 1
            R -= 1
        return True
s=input("Enter the string: ")
if checkPalin(s):
    print("They are palindrome")
else:
    print("They are not palindrome")