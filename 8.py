#average No in file (write mood)

input_file= open("test.txt", "r")
for line in input_file:
    line= line.rsplit(",")
    print(line)


