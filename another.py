import time
import multiprocessing
from ping3 import ping
import requests
import os
from dotenv import load_dotenv

def ping_item(domain):
    result = ping(dest_addr=domain['name'], timeout=4, ttl=64)
    if(result == False or result == None):
        if(domain['buyer']['telegramLogin'] is None):
            return f"{domain['name']} is down now ---- {domain['owner']['name']}"
        else:
            return f"{domain['name']} is down now ---- {domain['buyer']['telegramLogin']}"



if __name__ == "__main__":

    load_dotenv()

    AUTH_KEY = os.getenv('AUTH_KEY')
    TOKEN = os.getenv('TELEGRAM_TOKEN')
    CHATID = os.getenv('TELEGRAM_CHATID')
    

    while True:
        information = requests.get(f"https://integration-api-wp.com/domain/integration-pull?auth_key={AUTH_KEY}").json()
        start = time.perf_counter()

        with multiprocessing.Pool() as pool:
            results = pool.map(ping_item, information)
            results = [x for x in results if x is not None]
            if(len(results) > 0):
                for text in results:
                    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHATID}&text={text}")
                    time.sleep(3)

        finish = time.perf_counter()
        print(f'Выполнение заняло {finish-start: .2f} секунд.')
        
        time.sleep(10)
