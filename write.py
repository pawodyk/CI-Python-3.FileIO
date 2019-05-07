#writeing file
f = open('newfile.txt', 'w')
f.write("Hello")
f.close()

# appending to file
appendFile = open('appendfile.txt', 'a')
appendFile.write("Hello World\n")
appendFile.close()