from yollor import *
import time
import os
import platform
import random
from misc.scanning import *

def banner_starter(name):
    ban1 = rf"""
    {c.cyan('Hi ')}{c.red(name)}"""
    ban2 = rf"""
    {c.cyan('Welcome to the')} {c.red('Revenge')}"""
    print(ban1)
    time.sleep(1)
    print(ban2)
    
def banner_menu(name2):
    banner = rf"""
{c.green('n     n')}  {c.yellow('eeeeee')}  {c.blue('y     y')}   {c.blue('m       m ')}      {c.yellow('a')}         {c.green('rrrr')}
{c.green('nn    n')}  {c.yellow('e     ')}   {c.blue('y   y')}    {c.blue('mm     mm ')}     {c.purple('Yyax')}       {c.green('r   r')}
{c.green('n n   n')}  {c.yellow('e     ')}    {c.blue('y y')}     {c.blue('m m   m m   ')}   {c.yellow('a  a')}       {c.green('rrrr')}
{c.green('n  n  n')}  {c.yellow('eeeee ')}     {c.blue('y')}      {c.blue('m  m m  m  ')}   {c.yellow('aaaaaa  ')}    {c.green('rr')}
{c.green('n   n n')}  {c.yellow('e     ')}     {c.blue('y')}     {c.blue(' m   m   m')}    {c.yellow('a      a ')}    {c.green('r r')}
{c.green('n    nn')}  {c.yellow('e     ')}     {c.blue('y')}     {c.blue(' m       m ')}  {c.yellow('a        a ')}   {c.green('r  r')}
{c.green('n     n')}  {c.yellow('eeeeee')}     {c.blue('y')}     {c.blue(' m       m')}  {c.yellow('a          a ')}  {c.green('r   r')}

{c.green('National')} {c.yellow('Ender')} {c.blue('Yyax')} {c.blue('Malware')} {c.cyan('in')} {c.yellow('Archive')} {c.green('Rooter')}
{c.cyan('by')} {c.purple('Yyax')} {c.cyan('for')} {c.red(name2)}"""
    print(banner)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def att():
    sistema_operacional = platform.system()
    if sistema_operacional == 'Linux':
        if os.path.exists('/etc/apt'):
            os.system('sudo apt-get install clamav')
            os.system('pip install pyclamd')
            os.system('sudo freshclam')
        else:
            print(f"{c.red('Este script suporta apenas sistemas baseados em')} {c.yellow('Debian')} {c.red('ou')} {c.yellow('Ubuntu')}{c.red('.')}")
    else:
        print(f"{c.red('O sistema operacional ')}{c.yellow(sistema_operacional)}{c.red(' não é suportado.')}")

possible_api_keys = [
    "0845dd8121dcd672b6a9de14e1b17ca98b983d970546abb2d93acf66a4f2d731",
    "f5fe2c1332e368b9fa2ea2aa5c4de9bb5c0c77ffc195a6d2e9be323a7814723b",
    "41cf3b65c8f3516b7f4a326574a388cb0435ad05f4006359487f17bbd7abf7b4",
    "c72455e79d70bef8dd401d1d26a8d9f82a5c12f862ad8b8ba15472bae9b4307e"
]

def options(name):
    att_opt = input(rf"""
    {t.hashtag_yellow}{c.cyan(' Deseja atualizar/instalar os repos? (s/n) ')}""")
    if att_opt in ["s", "S"]:
        att()
    else:
        pass
    opt = input(rf"""
    {t.tagn1_yellow} {c.cyan('Scan Archive')}
    {c.cyan('[')}{c.yellow('X')}{c.cyan(']')} {c.cyan('Exit')}

    {t.hashtag_yellow} {c.cyan('Escolha uma opção: ')}""")
    if opt == "1":
        target_arch = input(rf"    {t.hashtag_yellow} {c.cyan('Caminho do arquivo para scan: ')}")
        final_key = random.choice(possible_api_keys)
        scanProcess = Scanner(final_key)
        scanProcess.start(arquivo=target_arch)
    elif opt in ["x", "X"]:
        pass


def main():
    clear()
    intro_name = input(f"{c.cyan('Seu nome')}{c.red(': ')}")
    clear()
    time.sleep(1)
    banner_starter(name=intro_name)
    time.sleep(1)
    clear()
    banner_menu(intro_name)
    options(intro_name)

if __name__ == "__main__":
    main()