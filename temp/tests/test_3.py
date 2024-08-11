from .checkers import checkout, PATH_ARC, PATH_FILES, PATH, PATH_EXTRACT, FILE1

def test_file_exist():
    '''Test exist extract files from archive'''
    make_arch = checkout(f'cd {PATH}/{PATH_FILES} && 7z a {PATH}/{PATH_ARC}/{FILE1}', 'Everything is Ok')
    cmd_test_file = f'test -f {PATH}/{PATH_ARC}/{FILE1} && echo True'
    file_exist = checkout(cmd_test_file, 'True')
    assert make_arch and file_exist

def test_extract_file_compare_7z_e():
    '''Compare files in original folder 
    with extracted files from archive with key "e"'''
    extract_arch = checkout(f'cd {PATH} && 7z e ./{PATH_ARC}/{FILE1} -o{PATH}/{PATH_EXTRACT} -y', 
                            'Everything is Ok')
    compare_cmd = f'diff -qr {PATH}/{PATH_FILES} {PATH}/{PATH_EXTRACT};  echo $?'
    compare = checkout(compare_cmd, '0')
    assert  compare and extract_arch