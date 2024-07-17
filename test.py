import subprocess
from string import punctuation
import argparse




def cmd_stdout(cmd: str) -> bool:
    '''Return stdout from command''' 
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return result.stdout
    
def clean_words(lst_words: list[str])
    res = []
    for word in lst_words:
        res.append(remove_punctuation(word))
    return res 

def get_lst_words(text: str) -> list[str]:
    text = text.replace('=', ' ')
    text = text.replace('\n', ' ')
    words = text.split()
    return words

def remove_punctuation(word:str) -> str:
    for item in punctuation:
        word = word.replace(item, '')
    return word

def text_in_stdout(stdout: str | list[str], text: str) -> bool:
    return text in stdout


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Тестирование наличие строки в ввыводе')
    
    parser.add_argument('command', type=str, help='Input command')
    parser.add_argument('text',type=str, help='Inpt search text in stdout')
    parser.add_argument('--word', '-w', default=None, type=str,help='Search just word in stdout')
    parser.add_argument('-v', '--verbouse', action='store_true' default=None, help='Verbose output')
    args = parser.parse_args()
    #if args.word is not None:

    print(args)
    cmd = args.command 
    str_in = args.text 
    print(test_cmd(cmd, str_in))
