import logging
import requests
import simpleaudio as sa
from time import sleep
from PIL import Image


# Configuration options
config = {
    'antpool_url': 'https://v3.antpool.com/auth/v3/observer/api/hash/query',
    'access_key': 'QWXs6omJD41UFooS5rN7',
    'coin_type': 'BTC',
    'observer_user_id': 'arstage1',
    'hash_rate_threshold': 18.05,
    'check_interval': 2 * 60,  # seconds
    'alarm_sound_file': 'C:\\Users\\Xeon\\Desktop\\alarm13.wav',
    'no_internet_image_file': 'C:\\Users\\Xeon\\PycharmProjects\\pythonProjecttokooo\\no wifi.jpg',
    'double_click_pos': (300, 25),
}


def get_hash_rate() -> float:
    """Get the current hash rate from Antpool API."""
    headers = {}
    params = {
        'accessKey': config['access_key'],
        'coinType': config['coin_type'],
        'observerUserId': config['observer_user_id'],
    }
    try:
        resp = requests.get(config['antpool_url'], headers=headers, params=params)
        resp.raise_for_status()
        data = resp.json()['data']
        hash_rate = float(data['hsNow'])
        return hash_rate
    except requests.exceptions.RequestException as e:
        logging.error(f'Error getting hash rate: {e}')
        raise


def main() -> None:
    """Main program loop that checks the hash rate and alarms if it's below the threshold."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    alarm_sound = sa.WaveObject.from_wave_file(config['alarm_sound_file'])
    while True:
        try:
            hash_rate = get_hash_rate()
            logging.info(f'Hash rate is {hash_rate:.2f} TH/s')
            if hash_rate < config['hash_rate_threshold']:
                while True:
                    alarm_sound.play()
                    logging.warning('Hash rate is below threshold! Check your miner.')
            sleep(config['check_interval'])
        except requests.exceptions.RequestException:
            no_internet_image = Image.open(config['no_internet_image_file'])
            no_internet_image.show()
            sleep(5)
            pyautogui.doubleClick(*config['double_click_pos'])
            while True:
                logging.error('No internet connection!')
                alarm_sound.play()


if __name__ == '__main__':
    main()
