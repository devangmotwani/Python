#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# Input Format
# A single line of five space-separated integers.
# Constraints
# Each integer is in the inclusive range .
# Output Format
# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly
# four of the five integers. (The output can be greater than 32 bit integer.)

arr = list(map(int, input().strip().split(' ')))
n=5
sum=[]
temp=0
for j in range(0,n):
    #for j in range(0,n):
        #if j+(n-1)>n-1:
    temp=arr[j%n]+arr[(j+1)%n]+arr[(j+2)%n]+arr[(j+3)%n]
    sum.append(temp)
print(min(sum),max(sum),sep=' ')