from checkers import checkout, PATH_ARC, PATH, PATH_EXTRACT,PATH_FILES, FILE1


def test_7z_d():
    '''delete files inside arch'''
    assert checkout(f'cd {PATH} && 7z d {PATH_ARC}/{FILE1}', 'Everything is Ok')

def test_7z_u():
    '''update files in arch'''
    assert checkout(f'cd {PATH}/{PATH_FILES} && 7z u ../{PATH_ARC}/{FILE1} ', 'Everything is Ok')

