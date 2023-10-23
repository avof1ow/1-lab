import requests
import pandas as pd

current_date = {"day": 22, "month": 10, "year": 2023}  # вчерашняя дата или раньше
data = {"rouble": [], "date": []}
for _ in range(int(input("На сколько дней\n>>>"))):
    str_day = str(current_date["day"])
    str_month = str(current_date["month"])
    str_year = str(current_date["year"])
    if len(str_day) == 1:
        str_day = "0" + str_day
    if len(str_month) == 1:
        str_month = "0" + str_month
    data_json = requests.get(
        f"https://www.cbr-xml-daily.ru/archive/{str_year}/{str_month}/{str_day}/daily_json.js"
    ).json()
    try:
        data["rouble"].append(data_json["Valute"]["USD"]["Value"])
        data["date"].append(data_json["Date"])
    except:
        data["rouble"].append("Курс не найден")
        data["date"].append(f"{str_year}-{str_month}-{str_day}")
    if current_date["day"] == 1:
        if current_date["month"] == 1:
            current_date["month"] = 12
            current_date["year"] -= 1
        else:
            current_date["month"] -= 1
        match current_date["month"]:
            case 1:
                current_date["day"] = 31
            case 2:
                if current_date["year"] % 4 == 0:
                    current_date["day"] = 28
                else:
                    current_date["day"] = 29
            case 3:
                current_date["day"] = 31
            case 4:
                current_date["day"] = 30
            case 5:
                current_date["day"] = 31
            case 6:
                current_date["day"] = 30
            case 7:
                current_date["day"] = 31
            case 8:
                current_date["day"] = 31
            case 9:
                current_date["day"] = 30
            case 10:
                current_date["day"] = 31
            case 11:
                current_date["day"] = 30
            case 12:
                current_date["day"] = 31
    else:
        current_date["day"] -= 1
        df = pd.DataFrame(data)
        df. to_csv("dollar_course.csv", sep=",", encoding="utf-8") 
  