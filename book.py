import re
import collections

text = open('chapter.txt', "r").read().lower()
words = re.findall('\w+', text)

print(collections.Counter(words).most_common(10))
