#MENAMPILKAN MACAM2 KATA DAN JUMLAHNYA

words = ('aku ya aku kamu ya kamu').split()

from collections import Counter
Counter(words)
print(Counter(words))

print('Number of words in text file :',len(words))