import csv
import re
fh = file("VocabularyNoteBook.dat",'r')
pattern = re.compile(r'({[\s\S]*?})')
toCSV = map(eval, pattern.findall(fh.read()))
keys = ['word','meaning','ctime']

with open('VocabularyNoteBook.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writerows(toCSV)
