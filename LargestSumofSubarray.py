# Given an integer array arr, write a program to find the
# subarray which has the largest sum and return its sum.
# If the array is empty (say n=0), print 0.
# Constraints:
# (The number of elements in the array can
# be as large as 1 million.)
# (Each element in the array is an integer
# and can range from -10,000 to 10,000.)
# (If the array is empty, you should print as
# the output.)


l = int(input())
arr = list(map(int,input().split()))
if l==0:
    print("0")
else:
    m = float('-inf')
    for i in range(0,l):
        store = 0
        for j in range(i,l):
            store = store + arr[j]
            m = max(store,m)
    print(m)