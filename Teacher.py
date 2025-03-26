answerkey = input()
k = int(input())
left_T = left_F = 0
changes_T = changes_F = 0
max_len_T = max_len_F = 0

for right in range(len(answerkey)):
    if answerkey[right]!='T':
        changes_T += 1

    while changes_T > k:
        if answerkey[left_T]!='T':
            changes_T -= 1
        left_T += 1
    
    max_len_T = max(max_len_T,right-left_T+1)



for right in range(len(answerkey)):
    if answerkey[right]!='F':
        changes_F += 1

    while changes_F > k:
        if answerkey[left_F]!='F':
            changes_F -= 1
        left_F += 1
    
    max_len_F = max(max_len_F,right-left_F+1)

print(max_len_T,max_len_F)