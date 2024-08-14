import pytest
from .checkers import checkout, get_list_nf, checkout_lst

@pytest.mark.usefixtures('atype')
class TestArch7z():

    @pytest.mark.exp   
    def test_7z_a(self):
        '''put files to arch'''
        assert checkout(f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}', 'Everything is Ok')

    @pytest.mark.exp   
    def test_7z_e(self):
        '''test unpack files from arch to some folder'''
        res = []
        res.append(checkout(f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}', 'Everything is Ok'))
        res.append(checkout(f' 7z e {self.atype} {self.dir_a}/{self.arch_name}.* -o{self.dir_e} -y', 'Everything is Ok'))
        assert all(res)

    @pytest.mark.exp 
    def test_7z_t(self):
        '''check test files inside arch'''
        res = []
        res.append(checkout(f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}', 'Everything is Ok'))
        res.append(checkout(f'7z t {self.atype} {self.dir_a}/{self.arch_name}.*', 'Everything is Ok'))
        assert all(res)

    @pytest.mark.exp
    def test_7z_d(self):
        '''delete files inside arch'''
        res = []
        res.append(checkout(f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}', 'Everything is Ok'))
        res.append(checkout(f'7z d {self.atype} {self.dir_a}/{self.arch_name}.*', 'Everything is Ok'))
        assert all(res)

    @pytest.mark.exp
    def test_7z_u(self):
        '''update files in arch'''
        res = []
        res.append(checkout(f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}', 'Everything is Ok'))
        res.append(checkout(f'cd {self.dir_f} && 7z u {self.atype} {self.dir_a}/{self.arch_name}.*', 'Everything is Ok'))
        assert all(res)

    @pytest.mark.exp
    def test_file_exist(self):
        '''Test exist extract files from archive'''
        res = []
        res.append(checkout(f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}', 'Everything is Ok'))
        cmd_test_file = f'test -f {self.dir_a}/{self.arch_name}.* && echo True'
        res.append(checkout(cmd_test_file, 'True'))
        assert all(res)

    @pytest.mark.exp
    def test_extract_file_compare_7z_e(self):
        '''Compare files in original folder 
        with extracted files from archive with key "e"'''
        res = []
        res.append(checkout(f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}', 'Everything is Ok'))
        res.append(checkout(f' 7z e {self.atype} {self.dir_a}/{self.arch_name}.* -o{self.dir_e} -y', 'Everything is Ok'))
        compare_cmd = f'diff -qr {self.dir_f} {self.dir_e};  echo $?'
        res.append(checkout(compare_cmd, '0'))
        assert  all(res)

    @pytest.mark.exp
    def test_crc32(self):
        '''Compare hash from crc32 with 7z h "archive_name"'''
        res = []
        res.append(checkout(f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}', 'Everything is Ok'))
        res.append(checkout(f'7z h {self.dir_a}/{self.arch_name}.* | grep -q `echo \"print(\'$(crc32 {self.dir_a}/{self.arch_name}.* )\'.upper())\" | python`; $?', '0'))
        assert all(res)

    @pytest.mark.exp
    def test_7z_x(self):
        '''Compare files and folders
        with paths extracted archive'''
        res = []
        res.append(checkout(f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}', 'Everything is Ok'))
        res.append(checkout(f' 7z x {self.atype} {self.dir_a}/{self.arch_name}.* -o{self.dir_e} -y', 'Everything is Ok'))
        compare_cmd = f'diff -qr {self.dir_f} {self.dir_e};  echo $?'
        res.append(checkout(compare_cmd, '0'))
        # compare = checkout(compare_cmd, '0')
        assert all(res)

    @pytest.mark.exp
    def test_7z_l(self):
        '''Compare list dirs and files 
        from output 7z l with 
        list dirs and files in original folder'''
        res = []
        res.append(checkout(f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}', 'Everything is Ok'))
        lst_folders_files = get_list_nf(f'{self.dir_f}')
        res.append(checkout_lst(f'7z l {self.dir_a}/{self.arch_name}.*', lst_folders_files))
        assert all(res)

    
    @pytest.mark.exp
    def test_extract_broken(self, broken_arc):
        '''Try extract files from broken arch'''
        res = []
        res.append(checkout(f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}', 'Everything is Ok'))
        broken_arc(f'{self.dir_a}/{self.arch_name}.*')
        res.append(checkout(f'7z e {self.dir_a}/{self.arch_name}.* -o{self.dir_e}', 'ERROR'))
        assert all(res)

    @pytest.mark.exp
    def test_test_broken(self, broken_arc):
        '''Testing broken arch'''
        res = []
        res.append(checkout(f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}', 'Everything is Ok'))
        broken_arc(f'{self.dir_a}/{self.arch_name}.*')
        res.append(checkout(f'7z t {self.dir_a}/{self.arch_name}.*', 'ERROR'))
        assert all(res)