import pytest
import pathlib
from datetime import datetime
from test_ssh.sshcheckers import ssh_getout, ssh_checkout


@pytest.fixture(scope='class')
def set_folder_ssh(request, load_config_yml):
    dir_b = pathlib.Path(load_config_yml['dir_base_ssh'])
    dir_f = dir_b / load_config_yml['dir_files']
    dir_f_d =dir_f / load_config_yml['dir_files']
    dir_a = dir_b / load_config_yml['dir_arch']
    dir_e = dir_b / load_config_yml['dir_extr']
    request.cls.dir_f = dir_f
    request.cls.dir_f_d = dir_f_d
    request.cls.dir_b = dir_b
    request.cls.dir_a = dir_a
    request.cls.dir_e = dir_e
    return dir_b, dir_f, dir_f_d, dir_a, dir_e

@pytest.fixture(scope='class')
def package_info(load_config_yml, request):
    request.cls.arch_name = load_config_yml['arch_name']
    request.cls.user_name = load_config_yml['user_name']
    request.cls.address = load_config_yml['ssh_address']
    request.cls.pwd = str(load_config_yml['ssh_pwd'])


@pytest.fixture
def create_folders_ssh(load_config_yml, set_folder_ssh, request):
    user_name = load_config_yml['user_name']
    address = load_config_yml['ssh_address']
    pwd = str(load_config_yml['ssh_pwd'])
    dir_b, dir_f, dir_f_d, dir_a, dir_e = set_folder_ssh
    res = []
    check_cmd = 'if [ $? -eq 0 ]; then echo true; else echo false; fi'
    cmd = f'mkdir -p {dir_f_d} {dir_a} {dir_e}; {check_cmd}'
    check = 'true'
    res.append(ssh_checkout(
            address, 
            user_name, 
            pwd, 
            cmd,
            check 
            ))
    for i in range(5):
        name = f'file_{i}.txt'
        file_name = dir_f / name
        size = load_config_yml['bs']
        cmd = f'truncate -s +{size} {file_name}; {check_cmd}'
        res.append(ssh_checkout(
                address, 
                user_name, 
                pwd, 
                cmd,
                check 
                )
            )
    for i in range(load_config_yml['count']):
        name = f'file_{i}.txt'
        file_name = dir_f_d / name
        cmd = f'truncate -s +{size} {file_name}; {check_cmd}'
        res.append(ssh_checkout(
                address, 
                user_name, 
                pwd, 
                cmd,
                check 
                )
            )
    yield res
    cmd = f'rm -r /home/user2/tmp; {check_cmd}'
    res.append(ssh_checkout(
                address, 
                user_name, 
                pwd, 
                cmd,
                check 
                )
            )

@pytest.fixture(autouse=True)
def system_log(request, load_config_yml):
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cmd = f'journalctl --since "{start_time}"'
    log = ssh_getout(
        request.cls.address, 
        request.cls.user_name, 
        request.cls.pwd, 
        cmd)
    file = load_config_yml['file_log']
    with open(file, 'w') as f:
        f.write(log)