def prepFile(file, i=0):
    count = 0
    f = open(file, "w")
    while count < i:
        count += 1
        f.write("Line " + str(count) + "\n")
    f.close()


# Challenge:
# Create a sample file consisting of four lines of text.
prepFile("challenge.txt", 4)

# Using the r+ mode, overwrite the first line. Then, move the file cursor to overwrite the third line. Finally, append a line to the file.
f = open("challenge.txt", "r+")

f.write("New 1 \n")
f.seek(16)
f.write("New 2 \n")
f.read()
f.write("New 3 \n")

# f.seek(0)
# print(f.readlines())

f.close()
