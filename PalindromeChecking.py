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