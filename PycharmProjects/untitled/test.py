__author__ = 'KamilLeszekP'
import os
import common.asm
import common.asm_files
# magic

os.chdir('C:/Users/KamilLeszekP/Desktop/skypt/test')
lista = os.listdir(".")

for i in lista:
    print 'plik: ' + i + ' ma rozszerzenie: ' + common.asm_files.fn_check_filetype(i)
#f = magic.Magic(mime=True)
#f = magic.Magic
#my_magic = magic.Magic(None,magic.MAGIC_MIME_TYPE)
#my_magic.id_filename
#    m.id_filename('setup.py')
#magic.Magic.id_filename('nazwa.dms')


#ommon.asm.pr_find_duplicates()