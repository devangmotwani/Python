s=input("Enter the string: ")
modify=list(s)
print(modify)
for i in range(len(modify)):
    if modify[i] in 'abcdefghijklmnopqrstuvwxyz':
        modify[i]=modify[i].upper()
    elif modify[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        modify[i]=modify[i].lower()
    else:
        continue
modify="".join(modify)
print(modify)
