import requests
from bs4 import BeautifulSoup
from src.config import rss_path_config

def get_rss_dashboard_from_dantri():
    output = []
    url_config = rss_path_config.path

    print(url_config[0]["path"])
    response = requests.get(url_config[0]["path"])
    
    # Parse HTML với BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Tìm phần tử theo XPath tương đương
    target_element = soup.select_one('body > main > div > div:nth-child(1) > ol')
    
    if target_element:
        # Lấy tất cả các thẻ li
        list_items = target_element.find_all('li')
        
        for item in list_items:
            a_element = item.find('a')
            url = a_element.get('href')
            text = a_element.text.strip()
            output.append({
                "url": url,
                "text": text
            })
            
        return output
    else:
        print("Không tìm thấy phần tử")
        return None
