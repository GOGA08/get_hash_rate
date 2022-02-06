import pyautogui
import requests
from time import sleep
from playsound import playsound
from PIL import Image


def get_hash_rate():

    headers = {
            " " " (url:https://v3.antpool.com/home )" " "
    }
    params = (
        ('accessKey', 'QWXs6omJD41UFooS5rN7'),
        ('coinType', 'BTC'),
        ('observerUserId', 'arstage1'),
    )
    try:

        resp = requests.get(
            'https://v3.antpool.com/auth/v3/observer/api/hash/query',
            headers=headers,
            params=params
        )
        resp.raise_for_status()
        data = resp.json()['data']
        hash_rate = float(data['hsNow'])
        print("first attempt")
        return hash_rate
    except:
        try:
            resp = requests.get(
                'https://v3.antpool.com/auth/v3/observer/api/hash/query',
                headers=headers,
                params=params
            )
            resp.raise_for_status()
            data = resp.json()['data']
            hash_rate = float(data['hsNow'])
            print("second attempt")
            return hash_rate
        except:
            resp = requests.get(
                'https://v3.antpool.com/auth/v3/observer/api/hash/query',
                headers=headers,
                params=params
            )
            resp.raise_for_status()
            data = resp.json()['data']
            hash_rate = float(data['hsNow'])
            print("third attempt")
            return hash_rate


def main():
    while True:

            try:
                hash_rate = get_hash_rate()
                print(f'hashrate is {hash_rate}')
                print("main code")

                if hash_rate < 18.05:
                    while True:
                        playsound('C:\\Users\\Xeon\\Desktop\\alarm13.wav')
                        print('GO CHECK!!!')
                sleep(2 * 60)

            except:
                    tok = Image.open("C:\\Users\\Xeon\\PycharmProjects\\pythonProjecttokooo\\no wifi.jpg")
                    tok.show()
                    sleep(5)
                    pyautogui.doubleClick(x=300, y=25)
                    pyautogui.doubleClick(x=300, y=25)
                    while True:
                        print('No internet')
                        playsound('C:\\Users\\Xeon\\Desktop\\alarm13.wav')






if __name__ == '__main__':
    main()
