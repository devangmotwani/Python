#For creating and writing to a binary file
with open("binary",'bw') as binary_file:
    for i in range(17):
        binary_file.write(bytes([i]))

#For reading binary characters from binary file
with open("binary",'br') as binaryFile:
    for b in binaryFile:
        print(b)