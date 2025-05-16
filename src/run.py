from src.helper.args_parse import args_init
from src.helper.env_loader import load_env
if __name__ == "__main__":
    try:
        load_env()
        args_init()
        print(1)
    except Exception as e:
        print(f"Error: {e}")