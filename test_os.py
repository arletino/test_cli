import subprocess


if __name__ == '__main__':
    result = subprocess.run('cat /etc/os-release', shell=True,
                            stdout=subprocess.PIPE,  encoding='utf-8')
    out = result.stdout.split('\n')
    print(out)
    
    if ('VERSION="40 (Workstation Edition)"' in out 
        and 'NAME="Fedora Linux"' in out 
        and not result.returncode):
        print('SUCCESS')
    else:
        print('FAIL')
