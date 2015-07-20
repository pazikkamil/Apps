__author__ = 'KamilLeszekP'
import magic


def fn_check_filetype( par_file ):
    my_magic = magic.Magic(None, magic.MAGIC_MIME_TYPE)
    return my_magic.id_filename(par_file)
