# At a lemonade stand, each Lemonade costs $5 Customers ye
# standing in a queue to buy from you paying one  at a time in
# order specified by bills Each customer pay either a $5, $10, or
# $20 bill You must provide the correct change to each customer

# You start with no Yow task is to determine
# whethe pu cm proade the correct chart* to etery customer
# If possibie, print true otherwise print flase

n = int(input())
arr = list(map(int,input().split()))
five = 0
ten = 0
for i in arr:
    if i==5:
        five += 1
    elif i==10:
        if five >= 1:
            five -= 1
            ten += 1
        else:
            print("False")
            exit()
    elif i==20:
        if five >= 3:
            five -= 3
        elif ten>=1 and five>=1:
            ten -= 1
            five -= 1
        else:
            print("False")
            exit()
print("True")