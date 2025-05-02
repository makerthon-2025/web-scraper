import os
import json

# Resource path for saving and reading files

def save_file(file_path, content):
    file_path = f"resource/data/{file_path}"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    content = json.dumps(content, ensure_ascii=False, indent=4)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def read_file(file_path):
    try:
        file_path = f"resource/data/{file_path}"
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.loads(file.read())
    except Exception:
        return None
    

# Dyanamic path for saving and reading files (!!!BE CAREFUL!!!)

def save_txt_file(file_path, content):
    # os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    

def read_txt_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception:
        return None