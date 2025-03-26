arr = input().split()
t = arr[0]
s = arr[1]

dict1 = {}
dict2 = {}

for i in range(len(t)):
    if t[i] in dict1:
        dict1[t[i]] = dict1[t[i]] + 1
    else:
        dict1[t[i]] = 1

for i in range(len(s)):
    if s[i] in dict2:
        dict2[s[i]] = dict2[s[i]] + 1
    else:
        dict2[s[i]] = 1

if len(s) == len(t):
    if dict1 == dict2:
        print("Anagrams")
    else:
        print("Not Anagrams")
else:
    print("Not Anagrams")