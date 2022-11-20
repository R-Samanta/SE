import os
MAXSIZ = 100

def siz_chk(file):
    file_siz = os.path.getsize(file)
    # if file_siz > MAXSIZ * 1024 or file_siz == 0:
    #     return 0
    return not(file_siz > MAXSIZ * 1024 or file_siz == 0)