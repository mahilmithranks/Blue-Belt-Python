# Write a program that takes an array of integers and a target
# sum as input, and finds the starting and ending indices
# of a contiguous subarray whose elements sum up to If
# such a subarray exists, print its starting and ending indices. If
# no such subarray exists, print
# The program should output only the first matching subarray
# (from the beginning of the array) even if multiple subarrays
# meet the criteria.
# Constraints:
# 1. The length of the array@is at least 1 and at most
# 1000.
# 2. Each element of the array is an integer between -1000
# and 1000.
# 3. The target sum is an integer between -IO and
# 10


l = int(input())
arr = list(map(int,input().split()))
tar = int(input())
flag = False
for i in range(len(arr)):
    store = 0
    for j in range(i,len(arr)):
        store = store + arr[j]
        if store == tar:
            print(i,j)
            flag = True
            break
    if flag:
        break
    
if not flag:
    print("No subarray")