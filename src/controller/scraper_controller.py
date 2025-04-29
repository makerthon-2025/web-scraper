from src.service.selenium_service import get_category, get_content
from src.helper.file_helper import save_file, read_file
import threading
import time

lock = threading.Lock()
thread_num = 0

def load_header_controller():
    cate = get_category()
    
    save_file('category.json', cate)

    print(f"Đã lưu {len(cate)} danh mục vào file category.json")

def load_content_controller():
    cate = read_file('cache/category.json')
    if cate is None:
        cate = read_file('category.json')
    # arr = get_content(cate[0]['link'])

    error = read_file('cache/error.json')
    if error is None:
        error = []

    def process_item(item):
        global thread_num
        with lock:
            thread_num += 1

        print(f"Đang tải {item['name']}...")
        file_check = read_file(f"content/{item['name']}.json")

        if file_check is not None:
            print(f"\033[33mĐã có file content/{item['name']}.json, bỏ qua.\033[0m")
            with lock:
                thread_num -= 1
                return True
            return

        arr = get_content(item['link'])

        if arr is None:
            with lock:
                error.append({
                    'name': item['name'],
                    'link': item['link']
                })
            print(f"\033[31mKhông thể tải {item['name']}, bỏ qua.\033[0m")
            save_file(f"cache/error.json", error)
        else: 
            save_file(f"content/{item['name']}.json", arr)
            print(f"Đã lưu {item['name']} vào file content/{item['name']}.json")

        with lock:
            thread_num -= 1
            return True
    
    while(len(cate) > 0):
        if thread_num < 3:
            first_item = cate.pop(0)
            threading.Thread(target=process_item, args=(first_item,)).start()

        save_file('cache/category.json', cate)
        time.sleep(1)

    print("Tất cả các thread đã hoàn thành.")
    
def update_content_controller():
    import os

    # Đường dẫn thư mục chứa file json
    directory = "resource/data/content"

    # Lấy danh sách tất cả các file .json trong thư mục
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]

    # In ra danh sách các file json
    print(json_files)
