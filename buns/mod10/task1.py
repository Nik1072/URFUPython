import requests
import json


def get_ship_info(name_of_ship):

    ship_url = f'https://swapi.dev/api/starships/?search={name_of_ship}'

    # Получаем информацию о корабле
    response = requests.get(ship_url)
    if response.status_code == 200:  # Проверка успешности запроса
        ship_data = response.json()
        ship = ship_data['results'][0]

        # Выносим информацию о пилотах корабля
        pilots_info = []
        for pilot_url in ship['pilots']:
            pilot_response = requests.get(pilot_url)
            if pilot_response.status_code == 200:  # Проверка успешности запроса
                pilot_data = pilot_response.json()

                # Получаем информацию о планете, откуда родом пилот
                homeworld_url = pilot_data['homeworld']
                homeworld_response = requests.get(homeworld_url)
                if homeworld_response.status_code == 200:  # Проверка успешности запроса
                    homeworld_data = homeworld_response.json()
                    homeworld_name = homeworld_data['name']
                # Если запрос с информацией о планете, откуда родом пилот неуспешен
                else:
                    homeworld_name = f"Ошибка при получении данных о планете пилота. Код ошибки: {homeworld_response.status_code}"

                # Формируем информацию о пилотах
                pilot_info = {
                    'name': pilot_data['name'],
                    'height': pilot_data['height'],
                    'mass': pilot_data['mass'],
                    'homeworld': homeworld_name,
                    'homeworld_url': homeworld_url
                }
                pilots_info.append(pilot_info)
            # Если запрос с информацией о пилотах неуспешен
            else:
                return f"Ошибка при получении данных о пилоте. Код ошибки: {pilot_response.status_code}"

        # Формируем и выводим результат
        result = {
            'ship_name': ship['name'],
            'starship_class': ship['starship_class'],
            'max_atmosphering_speed': ship['max_atmosphering_speed'],
            'pilots': pilots_info
        }

        print(json.dumps(result, indent=2))

        # Записываем результат в файл
        with open('searched_ship_info.json', 'w') as file:
            json.dump(result, file, indent=2)
    # Если запрос с информацией о корабле неуспешен
    else:
        return f"Ошибка при получении данных о корабле. Код ошибки: {response.status_code}"


if True:
    ship_name_to_search = 'Millennium Falcon'
    get_ship_info(ship_name_to_search)
