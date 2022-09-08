#BACA TEXT DARI FILE .TXT

#membaca file
f2 =  open('Kata.txt','r')
content = f2.read()
print(content)

#split per kata
words = open('Kata.txt').read().split()
print(words)

#menampilkan macam2 kata dan jml nya
from collections import Counter
Counter(words)
print(Counter(words))

print('Number of words in text file :',len(words))