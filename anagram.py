def checkAnagram(s,t):
    if len(s)!=len(t):
        return False
    dict={}
    for a in s:
        dict[a]=dict.get(a,0)+1
    for b in t:
        dict[b]=dict.get(b,0)-1
    return all(count==0 for count in dict.values())
s=input("Enter the first string: ")
t=input("Enter the second string: ")
if checkAnagram(s,t): # return sorted(t)==s
    print(f"They are anagram")
else:
    print(f"They are not anagram") 