# One day, Jack was going home by tram. When he got his ticket, he noticed that number on the ticket was not lucky.
# A lucky ticket is a six-digit number on the ticket in which sum of the first three digits is equal to the sum of
# the last three digits.
# For example, number 165912 is lucky because sum of , and .
# Since the number on the ticket wasn't lucky, Jack needs your help to find the next lucky ticket number.
# For example, if Jack's ticket number is 165901, then the next lucky ticket number is 165903.
# Given Jack's current ticket number, find and print the next lucky ticket number.
# Input Format
# The first line contains an integer, x, denoting the  number on the ticket.

import sys

def onceInATram(x):
    # Complete this function
    while(True):
        x+=1
        a=int(x/1000)
        b=x%1000
        if sum_of_digits(a)==sum_of_digits(b):
            return x


def sum_of_digits(x):
    d=int(x/10)
    a=int(d/10)
    b=int(d%10)
    c=int(x%10)
    sum =a+b+c
    return sum

if __name__ == "__main__":
    x = int(input().strip())
    result = onceInATram(x)
    print(result)
