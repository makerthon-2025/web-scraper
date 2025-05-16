from src.service.scraper import load_header_service, load_content_service, update_content_service, load_rss_service

def load_rss_controller():
    try:
        load_rss_service()
        print("\033[32mTải rss dashboard thành công!\033[0m")
    except Exception as e:
        print(f"\033[31mLỗi khi tải rss dashboard: {e}\033[0m")

def load_header_controller():
    try:
        load_header_service()
        print("\033[32mTải header thành công!\033[0m")
    except Exception as e:
        print(f"\033[31mLỗi khi tải header: {e}\033[0m")
        return

def load_content_controller():
    try:
        load_content_service()
        print("\033[32mTải content thành công!\033[0m")
    except Exception as e:
        print(f"\033[31mLỗi khi tải content: {e}\033[0m")
    
def update_content_controller():
    try:
        update_content_service()
        print("\033[32mCập nhật content thành công!\033[0m")
    except Exception as e:
        print(f"\033[31mLỗi khi cập nhật content: {e}\033[0m")


