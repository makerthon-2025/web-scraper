from dotenv import load_dotenv
from dotenv import load_dotenv
from src.helper.file_helper import read_txt_file, save_txt_file
import os

def load_env():
    if os.path.exists('.env'):
        load_dotenv(dotenv_path=".env")
        __gen_env_template()
    else:
        print("not exist .env")


# ==========================================
# ================ PRIVATE FUNCTION ========

def __gen_env_template():
    file = read_txt_file('.env')
    lines = file.split('\n')
    output = ''

    for item in lines:
        if item != '':
            output += item.split('=')[0] + '=...\n'
        else :
            output += '\n'

    save_txt_file('.env.template', output)