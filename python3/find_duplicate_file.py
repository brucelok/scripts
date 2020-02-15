import os
import shutil
import hashlib
'''
author: lok.bruce@gmail.com
'''

def get_md5(fname, chunk_size=4096):
    hash = hashlib.md5()

    with open(fname, 'rb') as f:
        chunk = f.read(chunk_size)

        while chunk:
            hash.update(chunk)
            chunk = f.read(chunk_size)

    return hash.hexdigest()


if __name__ == "__main__":

    src_folder = "/Users/brucelok/main/repo_my/awesome/"
    dest_folder = "/Users/brucelok/main/tmp/"
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
    #print(str(dup_dict))

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for i, j in dup_dict.items():
        if len(j) > 1:
            print("Filenames %s has same md5 hash %s" %(j, i))
            for n in j:
                src = src_folder + str(n)
                shutil.move(src, dest_folder)
