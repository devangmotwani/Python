# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.
#
# Input Format
#
# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.
#
# Constraints
#
# The elements added to the list must be integers.
# Output Format
#
# For each command of type print, print the list on a new line.
#
# Sample Input
#
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output
#
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]


N=int(input())
list_array = []
one_out=0
for i in range(1,N+1):
    command = input()
    command = command.split()
    if(len(command)>3):
        break
    elif len(command)==3:
        if "insert" in command:
            #if command[1] in '1234567890' and command[2] in '1234567890':
            list_array.insert(int(command[1]),int(command[2]))
            #else:
            #   break
        else:
            break
    elif len(command)==2:
        if "remove" in command:
            for i in list_array:
                if i==(int(command[1])):
                    #print(i)
                    #print(list_array.index(i))
                    list_array.pop(list_array.index(i))
                    break
        else:
            if "append" in command:
                list_array.append(int(command[1]))
            else:
                print("Invalid command or command entry")
                break
    else:
        if "print" in command:
            print(list_array)
        elif "sort" in command:
            list_array = sorted(list_array)
        elif "pop" in command:
            list_array.pop(-1)
        elif "reverse" in command:
            list_array.reverse()
        else:
            print("Invalid command or command entry")
            break

print(list_array)

# Other solution
# n = input()
# l = []
# for _ in range(n):
#     s = raw_input().split()
#     cmd = s[0]
#     args = s[1:]
#     if cmd !="print":
#         cmd += "("+ ",".join(args) +")"
#         eval("l."+cmd)
#     else:
#         print l