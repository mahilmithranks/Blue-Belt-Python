# Write a program to check if two given strings are anagrams of
# each other. Anagrams are strings formed by rearranging the
# letters of another string while using all the original letters
# exactly once.
# Input:
# Two strings, each containing only lowercase letters and no
# spaces.
# Output:
# Print •Anagrams" if the strings are anagrams of each other;
# otherwise, print "Not Anagrams".


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