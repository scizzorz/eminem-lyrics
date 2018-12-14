import sys
from collections import defaultdict

files = sys.argv[1:]

words = defaultdict(int)

spacechars = '.:;,!?*()[]{}'
badchars = '"\'-'
stopwords = {x.strip() for x in open('stopwords')}

for file in files:
  with open(file) as fp:
    text = fp.read()

  for char in spacechars:
    text = text.replace(char, ' ')

  for char in badchars:
    text = text.replace(char, '')

  text = text.lower().split()

  for word in set(text) - stopwords:
    words[word] += text.count(word)

for word, freq in sorted(words.items(), key=lambda x: (x[1], x[0])):
  print(freq, word)

print(sum(words.values()), 'TOTAL')
print(len(words), 'UNIQUE')
