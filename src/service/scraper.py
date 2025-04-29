from src.service.selenium_service import get_category, get_content, update_content
from src.helper.file_helper import save_file, read_file
import threading
import time
import os
# --------------------------------------------------------------------------------

lock = threading.Lock()
thread_num = 0

def load_header_service():
    cate = get_category()
    
    save_file('category.json', cate)

    print(f"Đã lưu {len(cate)} danh mục vào file category.json")

def load_content_service():
    cate = __get_category()
    error = __get_error_file()
    success = []
    
    while(len(cate) > 0):
        if thread_num < 5:
            first_item = cate.pop(0)
            threading.Thread(target=__process_item, args=(first_item, error, success)).start()

        save_file('cache/remain.json', cate)
        time.sleep(1)

    print("Tất cả các thread đã hoàn thành.")

def update_content_service():
    sucess = read_file('cache/success.json')

    for i in range(1, len(sucess)):
        try:
            content = read_file(f"content/{sucess[i]['name']}.json")
            uc = update_content(sucess[i]['link'], content.copy())
            for item in uc:
                
                    content.append(item)
                    print(f"Đã thêm {item['name']} vào file content/{sucess[i]['name']}.json")
                    save_file(f"content/{sucess[i]['name']}.json", content)
        except Exception as e:
            continue

# --------------------------------------------------------------------------------
# ========================= PRIVATE FUNCTION =========================
# --------------------------------------------------------------------------------

def __get_category():
    cate = read_file('cache/remain.json')
    if cate is None:
        cate = read_file('category.json')

    return cate

def __get_error_file():
    error = read_file('cache/error.json')
    if error is None:
        error = []

    return error

def __save_to_cache(file_name, data, name, link):
    data.append({
        'name': name,
        'link': link
    })

    save_file(file_name, data)

def __process_item(item, error, success):
    global thread_num
    with lock:
        thread_num += 1

    print(f"Đang tải {item['name']}...")
    file_check = read_file(f"content/{item['name']}.json")

    if file_check is not None:
        print(f"\033[33mĐã có file content/{item['name']}.json, bỏ qua.\033[0m")
        with lock:
            __save_to_cache("cache/success.json", success, item['name'], item['link'])
            thread_num -= 1
            return 
        return

    arr = get_content(item['link'])

    if arr is None:
        with lock:
            __save_to_cache("cache/error.json", error, item['name'], item['link'])

        print(f"\033[31mKhông thể tải {item['name']}, bỏ qua.\033[0m")
    else: 
        with lock:
            save_file(f"content/{item['name']}.json", arr)
            __save_to_cache("cache/success.json", success, item['name'], item['link'])
        print(f"Đã lưu {item['name']} vào file content/{item['name']}.json")

    with lock:
        thread_num -= 1
        return True