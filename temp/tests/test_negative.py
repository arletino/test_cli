from .checkers import broke_arch, checkout, PATH_ARC, PATH, PATH_EXTRACT, FILE2

def test_make_broken_arc():
    '''Это должно быть в фикстуре, пока фикстуры мы не изучали будет так)'''
    drop_file = f'test -f {PATH}/{PATH_ARC}/{FILE2} && rm {PATH}/{PATH_ARC}/{FILE2} && echo True'
    checkout(drop_file, 'True')
    make_arch = checkout(f'cd {PATH} && 7z a {PATH_ARC}/{FILE2}', 'Everything is Ok')
    brake = broke_arch(f'{PATH}/{PATH_ARC}/{FILE2}')
    assert brake and make_arch

def test_extract_broken():
    '''Try extract files from broken arch'''
    assert checkout(f'cd {PATH} && 7z e {PATH_ARC}/{FILE2} -o./{PATH_EXTRACT}', 'ERROR') 

def test_test_broken():
    '''Testing broken arch'''
    assert checkout(f'cd {PATH} && 7z t {PATH_ARC}/{FILE2}', 'ERROR')