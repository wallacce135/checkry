import time
import multiprocessing
import os
import datetime
import requests
import urllib.request, socket, urllib.error
from dotenv import load_dotenv
from itertools import repeat




def pingDomain(domain, token):
    try:
        result = urllib.request.urlopen(url="https://" + domain['name'], timeout=35)
        # print(result)
        # print(domain['name'])

    except (urllib.error.HTTPError, urllib.error.URLError) as error:

        print(f"Data was not retrieved {error}\nURL: {domain['name']}")
        if(domain['buyer']['telegramLogin'] is None):
            if(domain['buyer']['name'] is None):
                text = f"💀{domain['name']}💀 data was not retrieved\nError:TimeoutError\n{domain['owner']['name']}"
                requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id=-1001832929433&text={text}")
            else:
                text = f"💀{domain['name']}💀 data was not retrieved\nError:TimeoutError\n{domain['buyer']['name']}"
                requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id=-1001832929433&text={text}")
        else:
            text = f"💀{domain['name']}💀 data was not retrieved\nError:TimeoutError\n{domain['buyer']['telegramLogin']}"
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id=-1001832929433&text={text}")
        

    except socket.timeout: 

        print(domain['name'] + "-- dead")
        if(domain['buyer']['telegramLogin'] is None):
            if(domain['buyer']['name'] is None):
                text = f"💀{domain['name']}💀 data was not retrieved\nError:TimeoutError\n{domain['owner']['name']}"
                requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id=-1001832929433&text={text}")
            else:
                text = f"💀{domain['name']}💀 data was not retrieved\nError:TimeoutError\n{domain['buyer']['name']}"
                requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id=-1001832929433&text={text}")
        else:
            text = f"💀{domain['name']}💀 data was not retrieved\nError:TimeoutError\n{domain['buyer']['telegramLogin']}"
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id=-1001832929433&text={text}")
        requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id=-1001832929433&text={text}")
    return



if __name__ == "__main__":
    
    load_dotenv()

    AUTH_KEY = os.getenv('AUTH_KEY')
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    TELEGRAM_CHATID = os.getenv('TELEGRAM_CHATID')

    while True:
        domains = requests.get(f"https://integration-api-wp.com/domain/integration-pull?auth_key={AUTH_KEY}").json()
        # print(domains)

        start = time.perf_counter()

        with multiprocessing.Pool() as pool:
            results = pool.starmap(pingDomain, zip(domains, repeat(TELEGRAM_TOKEN)))
            
        
        time.sleep(10)
        finish = time.perf_counter()
        print(f'Выполнение заняло {finish-start: .2f} секунд.')


