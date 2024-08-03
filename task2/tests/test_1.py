from checkers import checkout, PATH_ARC, PATH, PATH_EXTRACT, PATH_FILES, FILE1

   
def test_7z_a():
    '''put files to arch'''
    assert checkout(f'cd {PATH}/{PATH_FILES} && 7z a {PATH}/{PATH_ARC}/{FILE1}', 'Everything is Ok')

def test_7z_e():
    '''test unpack files from arch to some folder'''
    assert checkout(f'cd {PATH} && 7z e ./{PATH_ARC}/{FILE1} -o./{PATH_EXTRACT} -y', 'Everything is Ok')
    
def test_7z_t():
    '''check test files inside arch'''
    assert checkout(f'cd {PATH} && 7z t ./{PATH_ARC}/{FILE1}', 'Everything is Ok')