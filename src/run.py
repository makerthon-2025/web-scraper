from src.helper.args_parse import args_init
from src.helper.env_loader import load_env
from src.helper.file_helper import read_file, save_file

def __get_category():
    cate = read_file('category.json')

    return cate

if __name__ == "__main__":
    try:
        load_env()
        args_init()

    except Exception as e:
        print(f"Error: {e}")