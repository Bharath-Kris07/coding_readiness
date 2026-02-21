def check(ransomNote,magazine):
    dict={}
    for i in magazine:
           dict[i]=dict.get(i,0)+1
    for j in ransomNote:
        if(dict.get(j,0)==0):
            return False
        dict[j]-=1
    return True
ransomNote=input("Enter the ransomNote:")
magazine=input("Enter the magazine:")
if(check(ransomNote,magazine)):
    print("True")
else:
    print("False")