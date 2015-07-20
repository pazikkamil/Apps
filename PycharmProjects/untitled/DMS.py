__author__ = 'KamilLeszekP'

import os
import re
import hashlib
import collections
import common.asm

def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

os.chdir('C:/Users/KamilLeszekP/Desktop/skypt/test')
lista = os.listdir(u".")

for i in lista:
    os.rename(i, i.replace(" ", "_"))

lista = os.listdir(u".")
sumy = list()
plik = open('checksums', 'w')
for i in lista:
    sumy.append(md5Checksum(i))


dictionary = dict(zip(lista, sumy))
duplikaty = common.asm.pr_find_duplicates(dictionary)

print 'Duplikaty to:'
print duplikaty
#duplicated = [x for x, y in collections.Counter(dictionary.viewvalues()).items() if y > 1]

#print sumy
#print 'Duplikaty to: ' + duplicated[0]

#for i in dictionary:
#    print dictionary.

#print(list(dictionary.keys())[list(dictionary.values()).index(duplicated))]

plik.close()
