# A teacher is preparing a test with true/false questions.
# The correct answers to these questions are given in a string
# answerKey, where each character is either (true) or
# (false),
# To confuse students, the teacher wants to maximize the
# number of consecutive questions with the same answer (either
# all or in a row).
# You are allowed to change up to answers in the
# string. For example, you can change
# to or to Your goal is to determine
# the maximum number of consecutive identical answers
# or that can be achieved after
# performing at most changes.
# Input Format
# I. The first line contains a string answerKey of length
# 2. The second line contains an integer representing
# the maximum number of changes allowed.
# Output Format
# • Print a single integer, the maximum number of
# consecutive or that can be achieved
# after performing at most changes.


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