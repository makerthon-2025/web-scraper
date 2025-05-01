from dotenv import load_dotenv
from dotenv import load_dotenv
import os

def load_env():
    if os.path.exists('.env'):
        load_dotenv(dotenv_path=".env")
    else:
        print("not exist .env")