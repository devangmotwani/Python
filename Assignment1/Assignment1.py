ip_address = input("Enter the IP address: ")
count = 1
element=0
total_length=0
segments=1
total =''
incorrect=0

for i in ip_address:
     if i=='.':
         segments=segments+1
# segments=count+1

for seg in ip_address:
    if seg in '1234567890.':
        if seg!='.':
            element=element+1
            total_length=total_length+1
        else:
            #print("Segment Number: {}".format(count))
            #print("Length of segment {} is {}".format(count,element))
            count=count+1
            total = total + str(element) + ','
            element=0
    else:
        total_length = -1
        #print("Invalid character entry.")
        break;

total = total + str(element)
count=1

for i in total:
    if i==',':
        continue
    else:
        if int(i)>3:
            incorrect=1
            break


if(total_length)==0:
    print("Length too short. Invalid entry")
elif (total_length)==-1:
    print("Invalid character entry")
elif segments<4:
    print("Error: Number of segments < 4")
elif segments>4:
    print("Error: Number of segments > 4")
elif incorrect==1:
    print("Length of a segment is greater")
else:
    print("Total segments: {}".format(segments))
    for i in total:
        if i==',':
            continue
        else:
            print("Length of segment {} = {}".format(count,i))
            count+=1
#print("Total length = {}".format(total))
#print("Number of segments= {}".format(segments))

