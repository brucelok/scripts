import os, sys
import shutil
import hashlib
'''
find duplicated files based on MD5 hash in the same folder
args: the absolute path you want to check files
return: a list of duplicated files with MD5
author: lok.bruce@gmail.com
'''

def get_md5(fname, chunk_size=4096):
    '''
    MD5 hash is generated here
    args: the target filename
    return: the encoded data in hexadecimal format
    '''
    hash = hashlib.md5()
    with open(fname, 'rb') as f:
        chunk = f.read(chunk_size)

        while chunk:
            hash.update(chunk)
            chunk = f.read(chunk_size)

    return hash.hexdigest()


if __name__ == "__main__":

    if len(sys.argv) < 2:
        sys.stderr.write("Usage: $ python %s <absolute path>\n" % sys.argv[0])
        sys.exit(1)

    src_folder = sys.argv[1]
    md5_dict = {}

    with os.scandir(src_folder) as entries:
        for entry in entries:
            if entry.is_file():
                name = entry.name
                md5 = get_md5(name)
                md5_dict.update({name:md5})

    dup_dict = {}

    for k, v in md5_dict.items():
        dup_dict.setdefault(v, set()).add(k)

    for i, j in dup_dict.items():
        if len(j) > 1:
            print("Filenames %s has same md5 hash %s" %(j, i))
