# Assume you are an awesome parent and want to give your
# children some cookies. But, you should give each child at most
# one cookie. Each child i has a greed factor which is
# the minimum size of a cookie that the child will be content
# with; and each cookie j has a size
# we can assign the cookie Cil to the child CC],
# i
# and the child will be content. Your goal is to maximize
# the number of content children and output the maximum
# number.
# Input Format
# 1. The first line contains an the number of
# children.
# 2, The second line contains space-separated
# integers, the greed factors of the children•
# 2
# n
# 3. The third line contains an integer the number of
# cookies.
# 4. The fourth line contains space-separated integers,
# the sizes of the cookies.
g = list(map(int,input().split()))
s = list(map(int,input().split()))
store = 0
g.sort()
s.sort()
j=0
for i in range(len(g)):
    while j<len(s):
        if s[j]>=g[i]:
            store = store + 1
            j += 1
            break
        j += 1
print(store)    
        