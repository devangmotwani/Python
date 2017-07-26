import sys


n = int(input().strip())
a = []
sum_lr=sum_rl=0
for i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
for i in range(len(a)):
    sum_lr+=a[i][i]
    #print("lr: {}".format(a[i][i]))
    sum_rl+=a[(len(a)-1)-i][i]
    #print("rl: {}".format(a[(len(a)-1)-i][i]))
print(abs(sum_lr-sum_rl))