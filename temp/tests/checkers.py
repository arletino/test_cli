import subprocess
from random import randbytes
from os import walk

PATH = '/home/atitkov/Documents/test_cli/tst'
PATH_ARC = 'archive'
FILE1 = 'arx2.7z'
FILE2 = 'arx3.7z'
PATH_EXTRACT = 'extract'
PATH_FILES = 'files'
PATH_FILES2 = 'files_folder'
PATH_EXTRACT2 = 'extract_folder'
FILE3 = 'arx4.7z'


def broke_arch(file):
    somebytes = randbytes(100)
    with open(file, 'wb+') as f:
        len_f = len(f.read())
        f.seek(len_f // 2)
        f.write(somebytes)
    return True

def get_crc32(file):
    cmd = f'crc32 {file}'
    result = subprocess.run(
        cmd, 
        shell=True, 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, 
        encoding='utf-8'
        )
    return result.stdout

def checkout(cmd, text):
    result = subprocess.run(
        cmd, 
        shell=True, 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, 
        encoding='utf-8'
        )
    return ((text in result.stdout and not result.returncode) or 
            (text in result.stderr and result.returncode))

def get_list_nf(path):
    lst_dir_fls = []
    for _, dirs, files in walk(path):
        lst_dir_fls.extend(dirs)
        lst_dir_fls.extend(files)
    return lst_dir_fls

def checkout_lst(cmd, lst_f_d):
    result = subprocess.run(
        cmd, 
        shell=True, 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, 
        encoding='utf-8'
        )
    temp = result.stdout.split('\n')
    res = []
    for row in temp:
        if '2024' in row:
            res.extend(row.split()[-1].split('/'))
    res.pop()
    return set(res) == set(lst_f_d) and not result.returncode 

if __name__ == '__main__':
    lst_folders_files = get_list_nf(f'{PATH}/{PATH_FILES2}')
    checkout_lst(f'cd {PATH} && 7z l {PATH_ARC}/{FILE3}', lst_folders_files)
