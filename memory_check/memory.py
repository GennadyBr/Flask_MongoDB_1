import time
import psutil
import requests

from settings import logger


# Функция для отправки HTTP-запроса на API
def send_alarm(memory_usage):
    # Определение URL и параметров запроса к API
    api_url = 'https://httpbin.org/'
    params = {
        'message': 'High memory usage detected!'
    }
    result = requests.get(api_url, params=params)
    logger.info(f'{result}, {params["message"]}, {memory_usage}')


def run():
    # Определение порогового значения потребления памяти в процентах
    mem_threshold = 80

    # Основной цикл скрипта
    while True:
        # Получение информации о потреблении памяти
        memory_usage = psutil.virtual_memory().percent

        # Проверка на превышение порогового значения
        if memory_usage > mem_threshold:
            send_alarm(memory_usage)
        else:
            logger.info(f'Normal memory usage detected! {memory_usage}')

        # Интервал между проверками состояния памяти (в секундах)
        time.sleep(5)


if __name__ == "__main__":
    run()
