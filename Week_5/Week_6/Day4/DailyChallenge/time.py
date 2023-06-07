import requests

def get_time_in_city(city):
    # Формирование URL-адреса API для получения времени
    url = f"http://worldtimeapi.org/api/timezone/Europe/{city}"

    try:
        # Отправка GET-запроса к API
        response = requests.get(url)
        data = response.json()

        # Получение данных о времени из ответа API
        current_time = data['datetime']
        time_zone = data['timezone']

        return current_time, time_zone
    except requests.exceptions.RequestException as e:
        print("Ошибка при отправке запроса:", e)
        return None, None

# Получение названия города от пользователя
city = input("Введите название города: ")

# Получение времени в указанном городе с использованием API
current_time, time_zone = get_time_in_city(city)

if current_time and time_zone:
    print(f"Текущее время в городе {city}: {current_time} ({time_zone})")
else:
    print("Не удалось получить время для указанного города.")