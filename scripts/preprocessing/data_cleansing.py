import csv
from sys import argv
import re

patt = re.compile(r'<([^>])+>')

file = argv[1]

with open (file, 'r', encoding='utf-8') as f:
	read = csv.reader(f)
	with open(file[:-4] + '_cleaned.csv', 'w', newline='', encoding='utf-8') as w:
		write = csv.writer(w)
		for row in read:
			cleaned = [i[i.find('title="')+7:len(i)-i[::-1].find('"')-1] if i.find('title="') > -1 else i for i in row]
			cleaned = [patt.sub('', i) for i in cleaned]
			write.writerow(cleaned)