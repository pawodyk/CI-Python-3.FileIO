# writeing file
f = open('newfile.txt', 'w')
lines = ['Hello', 'World', 'Welcome', 'To', 'File IO']
text = '\n'.join(lines)
f.writelines(text)
f.close()

# appending to file
appendFile = open('appendfile.txt', 'a')
appendFile.write("Hello World\n")
appendFile.close()
