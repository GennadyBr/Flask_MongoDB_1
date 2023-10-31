import time
import psutil
import requests


# Функция для отправки HTTP-запроса на API
def send_alarm():
    # Определение URL и параметров запроса к API
    API_URL = 'https://httpbin.org/'
    PARAMS = {
        'message': 'High memory_check usage detected!'
    }
    result = requests.get(API_URL, params=PARAMS)
    print(result)


def run():
    # Определение порогового значения потребления памяти в процентах
    MEMORY_THRESHOLD = 80

    # Основной цикл скрипта
    while True:
        # Получение информации о потреблении памяти
        memory_usage = psutil.virtual_memory().percent
        print(memory_usage)

        # Проверка на превышение порогового значения
        if memory_usage > MEMORY_THRESHOLD:
            send_alarm()

        # Интервал между проверками состояния памяти (в секундах)
        time.sleep(1)


if __name__ == "__main__":
    run()
