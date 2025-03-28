# Given a square matrix of size n x n, write a program to rotate
# the matrix by 90 degrees clockwise.
# Input:
# The input consists of n lines, where each line contains n space-
# separated integers representing the elements of the matrix.
# Output:
# Print the rotated matrix.
# Constraints:
# • The size of the matrix is between 1 and 1000.
# (1 n leee)
# • The matrix elements are integers in the range of -1000 to 1000


n = int(input())
store = []
for i in range(n):
    row = list(map(int,input().split()))
    store.append(row)

for i in range(n):
    for j in range(i+1,n):
        store[i][j],store[j][i] = store[j][i],store[i][j]

for i in range(n):
    for j in range(n//2):
        store[i][j],store[i][n-1-j]=store[i][n-1-j],store[i][j]
for i in store:
    print(*i)
print("__")