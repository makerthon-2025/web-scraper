import argparse
import os
import importlib.util
import sys

folder_path = 'src/router'
py_files = [f for f in os.listdir(folder_path) if f.endswith('.py')]

def args_init():
    parser = argparse.ArgumentParser(description="Chương trình đọc đối số từ dòng lệnh.")

    for item in py_files:
        print(f"Đang thêm tham số cho {item}")

        file_name = item.split('.')[0]
        parser.add_argument(f'--{file_name}', type=str, help=f"Chạy {file_name}")

    args = parser.parse_args()

    print("--------------------------------------\n")

    # In ra các tham số đã phân tích từ args
    for item in py_files:
        file_name = item.split('.')[0]
        if getattr(args, file_name):  
            file_path = f"{folder_path}/{file_name}.py"
            router = getattr(args, file_name)
            
            # Dynamically import the module
            spec = importlib.util.spec_from_file_location("test", file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Kiểm tra xem hàm run có tồn tại trong module không và gọi hàm
            if hasattr(module, router):
                run_function = getattr(module, router)  # Lấy hàm run
                run_function()  # Gọi hàm run
            else:
                print(f"Hàm {router} không tồn tại trong module.")