import json
PATH_TO_FILE = '../data/weather_date.json'

def average_temperature(path, city):
    with open(path, 'r') as file:
        data_weather = json.load(file)
    result = []
    for data in data_weather:
        if city in data:
            avg = sum(data[city].values())
            result = {
                city: {
                    'Average temperature': avg
                }
            }
    return json.dumps(result, indent=4)

user_city = str(input())
print(average_temperature(PATH_TO_FILE, user_city))
