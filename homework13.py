#Подключіться до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ),
# отримайте теперішній курс валют и запишіть його в TXT-файл в такому форматі:
# "[дата, на яку актуальний курс]"
#1. [назва валюти 1] to UAH: [значення курсу валюти 1]
#2. [назва валюти 2] to UAH: [значення курсу валюти 2]
#3. [назва валюти 3] to UAH: [значення курсу валюти 3]
#n. [назва валюти n] to UAH: [значення курсу валюти n]
#опціонально передбачте для користувача можливість обирати дату, на яку він хоче отримати курс

import requests
import json
url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
params = {
    "json": "",
    "valcode": "",
    "date": ""# Внести дату на яку необхідно отримати курс валют.
}
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    with open("currency_rates.txt", "w") as file:
        file.write(f"[дата, на яку актуальний курс]: {data[0]['exchangedate']}\n")

        for i, currency in enumerate(data[:10], start=1):
            file.write(f"{i}. {currency['cc']} to UAH: {currency['rate']}\n")

    print("Курс валют успішно збережений у файлі currency_rates.txt")
else:
    print("Помилка підключення до API НБУ. Спробуйте пізніше")