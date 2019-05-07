file = open('chapter.txt', 'r')
text = file.read()
file.close()

print(text)


# relative/absolute paths

print(open('files/relative_data.txt', 'r').read())