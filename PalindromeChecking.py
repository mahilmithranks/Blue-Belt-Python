# Develop a program that determines whether a given
# string can be transformed into a palindrome by rotating
# it. A palindrome is a string that reads the same forward
# and backward, such as "radar" or "level". Rotation
# involves moving characters from one end of the string
# to the other without changing their order otherwise. For
# example, rotating "abcde• once to the right gives
# "eabcd".
# Input format:
# • A single line of input containing the string
# The string will consist of lowercase and/or
# uppercase letters and/or digits, with a length of at
# least 1 character and not exceeding 10,000
# characters.


arr = list(map(int,input().split()))
flag = False
for i in range (len(arr)):
    rotated = arr[i:] + arr[:i]
    if rotated == rotated[::-1]:
        print("Yes, it's a Palindome")
        flag = True
        break
if not flag:
    print("Not a Palindrome")