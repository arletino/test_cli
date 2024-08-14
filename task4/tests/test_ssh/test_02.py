import pytest
# from tests.deploy import deploy
from test_ssh.sshcheckers import ssh_checkout, ssh_getout, ssh_checkout_negative

@pytest.mark.usefixtures('set_folder_ssh')
@pytest.mark.usefixtures('package_info')
@pytest.mark.usefixtures('atype')
class TestArch7z_ssh():

    @pytest.mark.ssh 
    def test_7z_a(self, create_folders_ssh):
        '''put files to arch'''
        res = create_folders_ssh
        cmd = f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}'  
        check = 'everything is ok'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        assert all(res)

    @pytest.mark.ssh  
    def test_7z_e(self, create_folders_ssh):
        '''test unpack files from arch to some folder'''
        res = create_folders_ssh
        cmd = f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}'  
        check = 'everything is ok'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        cmd = f' 7z e {self.atype} {self.dir_a}/{self.arch_name}.* -o{self.dir_e} -y'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        assert all(res)

    @pytest.mark.ssh 
    def test_7z_t(self, create_folders_ssh):
        '''check test files inside arch'''
        res = create_folders_ssh
        cmd = f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}'  
        check = 'everything is ok'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        cmd = f'7z t {self.atype} {self.dir_a}/{self.arch_name}.*'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        assert all(res)

    @pytest.mark.ssh
    def test_7z_d(self, create_folders_ssh):
        '''delete files inside arch'''
        res = create_folders_ssh
        cmd = f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}'  
        check = 'everything is ok'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        cmd = f'7z d {self.atype} {self.dir_a}/{self.arch_name}.*'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        assert all(res)

    @pytest.mark.ssh
    def test_7z_u(self, create_folders_ssh):
        '''update files in arch'''
        res = create_folders_ssh
        cmd = f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}'  
        check = 'everything is ok'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        cmd = f'cd {self.dir_f} && 7z u {self.atype} {self.dir_a}/{self.arch_name}.*'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        assert all(res)

    @pytest.mark.ssh
    def test_file_exist(self, create_folders_ssh):
        '''Test exist archive is a file'''
        res = create_folders_ssh
        cmd = f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}'  
        check = 'everything is ok'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        cmd = f'test -f {self.dir_a}/{self.arch_name}.* && echo true'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text='true' 
                )
            )
        assert all(res)

    @pytest.mark.ssh
    def test_extract_file_compare_7z_e(self, create_folders_ssh):
        '''Compare files in original folder 
        with extracted files from archive with key "e"'''
        res = create_folders_ssh
        check_cmd = 'if [ $? -eq 0 ]; then echo true; else echo false; fi'
        cmd = f'rm -r {self.dir_f_d}; {check_cmd}'
        check = 'true'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        cmd = f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}'  
        check = 'everything is ok'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        cmd = f' 7z e {self.atype} {self.dir_a}/{self.arch_name}.* -o{self.dir_e} -y'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        cmd = f'diff -qr {self.dir_f} {self.dir_e};  {check_cmd}'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text='true' 
                )
            )
        assert  all(res)

    @pytest.mark.ssh
    def test_crc32(self, create_folders_ssh):
        '''Compare hash from crc32 with 7z h "archive_name"'''
        res = create_folders_ssh      
        cmd = f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}'  
        check = 'everything is ok'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        check_cmd = 'if [ $? -eq 0 ]; then echo true; else echo false; fi'
        cmd = f'7z h {self.dir_a}/{self.arch_name}.* | grep -q `echo \"print(\'$(crc32 {self.dir_a}/{self.arch_name}.* )\'.upper())\" | python`; {check_cmd}'
        check = 'true'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        assert all(res)

    @pytest.mark.ssh
    def test_7z_x(self, create_folders_ssh):
        '''Compare files and folders
        with paths extracted archive'''
        res = create_folders_ssh      
        cmd = f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}'  
        check = 'everything is ok'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        cmd = f' 7z x {self.atype} {self.dir_a}/{self.arch_name}.* -o{self.dir_e} -y'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        check_cmd = 'if [ $? -eq 0 ]; then echo true; else echo false; fi'
        cmd = f'diff -qr {self.dir_f} {self.dir_e}; {check_cmd}'
        check = 'true'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        assert all(res)

    @pytest.mark.ssh
    def test_7z_l(self, create_folders_ssh):
        '''Compare list dirs and files 
        from output 7z l with 
        list dirs and files in original folder'''
        res = create_folders_ssh      
        cmd = f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}'  
        check = 'everything is ok'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        cmd = f'7z l {self.dir_a}/{self.arch_name}.*'
        lst_arch = ssh_getout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd
                )
        cmd = f'find {self.dir_f} -print'
        tst = ssh_getout(
            self.address, 
            self.user_name, 
            self.pwd, 
            cmd
        )
        base = f'{str(self.dir_f)}'
        tst = tst.split('\n')
        tst = [el.replace(base, '')[1::] for el in tst]
        compare = all(el in lst_arch for el in tst)
        res.append(compare)
        assert all(res)

    
    @pytest.mark.ssh
    def test_extract_broken(self, create_folders_ssh):
        '''Try extract files from broken arch'''
        res = create_folders_ssh      
        cmd = f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}'  
        check = 'everything is ok'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        check_cmd = 'if [ $? -eq 0 ]; then echo true; else echo false; fi'
        cmd = f'sed -i "2i head -c 15000000 /dev/urandom" {self.dir_a}/{self.arch_name}.*; {check_cmd}'
        check = 'true'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                check
                )
        )
        cmd = f'7z e {self.dir_a}/{self.arch_name}.* -o{self.dir_e}'
        check = 'error'
        res.append(ssh_checkout_negative(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        assert all(res)

    @pytest.mark.ssh
    def test_test_broken(self, create_folders_ssh):
        '''Testing broken arch'''
        res = create_folders_ssh      
        cmd = f'cd {self.dir_f} && 7z a {self.atype} {self.dir_a}/{self.arch_name}'  
        check = 'everything is ok'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        check_cmd = 'if [ $? -eq 0 ]; then echo true; else echo false; fi'
        cmd = f'sed -i "2i head -c 15000000 /dev/urandom" {self.dir_a}/{self.arch_name}.*; {check_cmd}'
        check = 'true'
        res.append(ssh_checkout(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                check
                )
        )
        cmd = f'7z t {self.dir_a}/{self.arch_name}.* -o{self.dir_e}'
        check = 'error'
        res.append(ssh_checkout_negative(
                self.address, 
                self.user_name, 
                self.pwd, 
                cmd,
                text=check 
                )
            )
        assert all(res)