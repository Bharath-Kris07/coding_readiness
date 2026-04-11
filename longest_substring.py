def lengthOfLongestSubstring(self, s):
    char_set = set()
    L = 0
    max_length = 0
    for R in range(len(s)):
        while s[R] in char_set:
            char_set.remove(s[L])
            L += 1
        char_set.add(s[R])
        max_length = max(max_length, R - L + 1)
    return max_length
s = input("Enter the string: ")
result = lengthOfLongestSubstring(s)
print(f"The length of the longest substring without repeating characters is: {result}") 