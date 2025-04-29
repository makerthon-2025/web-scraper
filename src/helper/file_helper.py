import os
import json
def save_file(file_path, content):
    """
    Save content to a file at the specified path.
    """
    file_path = f"resource/data/{file_path}"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    content = json.dumps(content, ensure_ascii=False, indent=4)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def read_file(file_path):
    """
    Read content from a file at the specified path.
    """
    try:
        file_path = f"resource/data/{file_path}"
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.loads(file.read())
    except Exception:
        return None