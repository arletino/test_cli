import subprocess
from string import punctuation
import argparse


def cmd_stdout(cmd: str) -> str:
    '''Return stdout from command''' 
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return result.stdout
    
def clean_words(lst_words: list[str]) -> list[str]:
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
    
    parser.add_argument(
            'command', 
            type=str, 
            help='Input command', 
            nargs='*'
            )
    parser.add_argument(
            '-t',
            '--text', 
            type=str,
            default=None, 
            nargs='*',
            help='Input search text in stdout'
            )
    parser.add_argument(
            '-w',
            '--word', 
            default=False, 
            action='store_true',
            help='Search just word in stdout'
            )
    parser.add_argument(
            '-v', '--verbose', 
            action='store_true', 
            default=False, 
            help='Verbose output'
            )
    args = parser.parse_args()
    command = ' '.join(args.command)
    stdout = cmd_stdout(command)
    search_text = None
    
    if args.text is not None:
        if args.word:
            search_text = args.text[0]
            stdout = get_lst_words(stdout)
            stdout = clean_words(stdout)
        else:
            search_text = ' '.join(args.text)
        if args.verbose:
            print(f'STDOUT: \n', stdout)
            print(f'Searching text:', search_text)
        print(f'Text in stdout: {text_in_stdout(stdout, search_text)}')
    else:
         print('No text for search')
        
