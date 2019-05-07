# writeing file
f = open('newfile.txt', 'w')
lines = ['Hello', 'World', 'Welcome', 'To', 'File IO']
f.writelines(lines)
f.close()

# appending to file
appendFile = open('appendfile.txt', 'a')
appendFile.write("Hello World\n")
appendFile.close()
