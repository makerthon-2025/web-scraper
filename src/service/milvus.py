from src.helper import file_helper
from src.repository import news
from src.helper import vector
import os
import threading

lock = threading.Lock()
thread_num = 0

def insert_data_service():
    content_list = os.listdir("resource/data/content") 

    for item in content_list:
        content_file_item = file_helper.read_file(f"content/{item}")
        
        __insert_data(content_file_item, item)

# ===================================================================
# ========================= PRIVATE FUNCTION =========================

def __insert_data(content_file_item, type):
    for index, it in enumerate(content_file_item):
        vector_item = vector.encode_text(it['name'])
        id = hash(it['link']) & ((1 << 63) - 1)

        data = {
            'id': id,
            'vector': vector_item,
            'name': it['name'],
            'link': it['link'],
            'content': it['content'],
            'type': type.split(".")[0],
        }

        print(f"Đã cập nhật {it['name']}")
        news.insert_data(data)