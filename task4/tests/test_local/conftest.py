import pytest
from test_local.checkers import broke_arch


@pytest.fixture(scope='function', autouse=True)
def make__tmp_base_folder(tmp_path_factory,make_file, load_config_yml, request):
    '''Create temporary folders for testing'''
    test_data = load_config_yml
    dir_base = tmp_path_factory.mktemp('tmp')
    dir_a =  dir_base / test_data['dir_arch']
    dir_a.mkdir()
    dir_e = dir_base / test_data['dir_extr'] 
    dir_e.mkdir()
    dir_f = dir_base / test_data['dir_files']
    dir_f.mkdir()
    for i in range(int(test_data['count'])):
        make_file(i, int(test_data['bs']), dir_f)
    dir_f_d = dir_f / 'folder_in'
    dir_f_d.mkdir()
    for i in range(int(test_data['count'])):
        make_file(i, int(test_data['bs']), dir_f_d)
    request.cls.dir_b = dir_base
    request.cls.dir_a = dir_a
    request.cls.dir_e = dir_e
    request.cls.dir_f = dir_f
    request.cls.dir_f_d = dir_a
    request.cls.arch_name = test_data['arch_name']
    

@pytest.fixture
def make_file():
    '''Create some test file with size and name as parameters'''
    def _make_file(fname, size, dir_f):
        fn = dir_f / f'file_{fname}.txt'
        with open(fn, 'w') as f:
            f.truncate(size)
        return fn
    return _make_file

@pytest.fixture
def broken_arc():
    '''Get brocken archive'''
    def _brocken(arch_name):
        broke_arch(arch_name)
    return _brocken
