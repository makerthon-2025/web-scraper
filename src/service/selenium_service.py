from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import threading
import requests

lock = threading.Lock()

def get_category():
    # Cấu hình Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    service = Service(executable_path="resource/driver/chromedriver.exe")  

    # Khởi tạo trình duyệt
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Truy cập trang báo Dân Trí
    driver.get("https://dantri.com.vn/")

    # Lấy HTML
    html = driver.page_source

    menu_more = driver.find_element(By.CLASS_NAME, 'menu-more')
    menu_more.click()

    submenu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'nf-menu')) 
    )

    html_content = submenu.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'lxml')

    div_elements = soup.find('ol')

    list_items = div_elements.find_all('li')

    arr = []

    for item in list_items:
        # Lấy tên và link
        name = item.find('a').text.strip()
        link = item.find('a')['href']

        arr.append({
            'name': name,
            'link': link
        })

        print(f"Name: {name}, Link: {link}")

    return arr

def get_content(url):
    try:
        # Cấu hình Selenium
        chrome_options = Options()
        chrome_options.add_argument("--headless")  
        service = Service(executable_path="resource/driver/chromedriver.exe")  

        # Khởi tạo trình duyệt
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Truy cập trang báo Dân Trí
        driver.get(url)

        # Lấy HTML
        html = driver.page_source

        soup = BeautifulSoup(html, 'lxml')

        arr = []

        div_elements = soup.find_all('div', class_='article-content')
        next_page = soup.find('a', class_='page-item next')['href']

        for item in div_elements:
            # Lấy tên và link
            name = item.find('h3').find('a').text.strip()
            link = item.find('h3').find('a')['href']
            content = item.find('div').text.strip()

            arr.append({
                'name': name,
                'link': link,
                'content': content
            })
        
        print(f"next_page: {next_page}")

        while next_page:
            driver.get(f"https://dantri.com.vn{next_page}")
            html = driver.page_source

            soup = BeautifulSoup(html, 'lxml')

            div_elements = soup.find_all('div', class_='article-content')
            next_page = soup.find('a', class_='page-item next')

            if next_page is None: break

            next_page = next_page['href']

            for item in div_elements:
                # Lấy tên và link
                name = item.find('h3').find('a').text.strip()
                link = item.find('h3').find('a')['href']
                content = item.find('div').text.strip()

                arr.append({
                    'name': name,
                    'link': link,
                    'content': content
                })

            print(f"next_page: {next_page}")

        return arr
    except Exception as e:
        print(f"Error: {e}")

def update_content(url, content_data):
    out_content= []
    try:
        response = requests.get(url)
        html = response.text

        soup = BeautifulSoup(html, 'lxml')


        arr = []

        div_elements = soup.find_all('div', class_='article-content')
        next_page = soup.find('a', class_='page-item next')['href']

        def foo():
            nonlocal arr
            nonlocal content_data
            nonlocal out_content
            for item in arr:
                for content_item in content_data:
                    if (content_item['name'] == item['name']):
                        print(f"Đã có nội dung {item['name']}")
                        return False
                
                out_content.append({
                    'name': item['name'],
                    'link': item['link'],
                    'content': item['content']
                })
                print(f"Đã cập nhật nội dung {item['name']}")
            
            arr = []
            return True

        for item in div_elements:
            # Lấy tên và link
            name = item.find('h3').find('a').text.strip()
            link = item.find('h3').find('a')['href']
            content = item.find('div').text.strip()

            arr.append({
                'name': name,
                'link': link,
                'content': content
            })

        while next_page:
            if not foo():
                break

            response = requests.get(f"https://dantri.com.vn{next_page}")
            html = response.text
            soup = BeautifulSoup(html, 'lxml')

            div_elements = soup.find_all('div', class_='article-content')
            next_page = soup.find('a', class_='page-item next')

            if next_page is None: break

            next_page = next_page['href']

            for item in div_elements:
                # Lấy tên và link
                name = item.find('h3').find('a').text.strip()
                link = item.find('h3').find('a')['href']
                content = item.find('div').text.strip()

                arr.append({
                    'name': name,
                    'link': link,
                    'content': content
                })

            print(f"next_page: {next_page}")

        return out_content
    except Exception as e:
        print(f"Error: {e}")