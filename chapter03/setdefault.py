import sys
import re

WORD_RE = re.compile(r'\w+')
index0 = {}
index1 = {}
with open(sys.argv[1], encoding='utf8') as fp:
	for line_no, line in enumerate(fp, 1):
		for match in WORD_RE.finditer(line):
			word = match.group()
			column_no = match.start()+1
			location = (line_no, column_no)
			occurrences = index0.get(word, [])
			occurrences.append(location)
			index0[word] = occurrences
			index1.setdefault(word, []).append(location)
for word in sorted(index0, key=str.upper):
	print(word, index0[word])
print(index0 == index1)
