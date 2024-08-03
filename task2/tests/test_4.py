from checkers import (
    checkout, get_crc32, get_list_nf, checkout_lst,
    PATH_ARC, PATH, 
    PATH_EXTRACT2, PATH_FILES2, 
    FILE3, FILE1
)


def test_crc32():
    '''Compare hash from crc32 with 7z h "archive_name"'''
    crc32 = get_crc32(f'{PATH}/{PATH_ARC}/{FILE1}').strip().upper()
    assert checkout(f'7z h {PATH}/{PATH_ARC}/{FILE1}', crc32)

def test_7z_x():
    '''Compare files and folders
    with paths extracted archive'''
    test_7z_a = checkout(f'cd {PATH}/{PATH_FILES2} && 7z a {PATH}/{PATH_ARC}/{FILE3}', 
                         'Everything is Ok')
    test_7z_x = checkout(f'cd {PATH} && 7z x ./{PATH_ARC}/{FILE3} -o{PATH}/{PATH_EXTRACT2} -y', 
                            'Everything is Ok')
    compare_cmd = f'diff -qr {PATH}/{PATH_FILES2} {PATH}/{PATH_EXTRACT2};  echo $?'
    compare = checkout(compare_cmd, '0')
    assert test_7z_a and test_7z_x and compare

def test_7z_l():
    '''Compare list dirs and files 
    from output 7z l with 
    list dirs and files in original folder'''
    lst_folders_files = get_list_nf(f'{PATH}/{PATH_FILES2}')
    assert checkout_lst(f'cd {PATH} && 7z l {PATH_ARC}/{FILE3}', lst_folders_files)
    