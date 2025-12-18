import requests
from requests.exceptions import ConnectionError, Timeout


def check_website_status(url):
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        response = requests.get(url, timeout=10)
        
        if 200 <= response.status_code < 400:
            print(f"✅ Сайт доступен! Код ответа: {response.status_code}\n")
        else:
            print(f"❌ Сайт недоступен! Код: {response.status_code}\n")
            
    except ConnectionError:
        print("не удалось установить соединение\n")

    except Timeout:
        print("oшибка подключения: превышено время ожидания\n")

    except requests.exceptions.RequestException as err:
        print(f"uncorrect request: {err}\n")

    except Exception as err:
        print(f"uncnow error: {err}\n")
