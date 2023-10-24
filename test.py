import pandas as pd
import requests


def get_data(day: int, month: int, year: int, days_count: int = 30):
    data = {"rouble": [], "date": []}
    for _ in range(days_count):
        str_day = str(day)
        str_month = str(month)
        str_year = str(year)
        if len(str_day) == 1:
            str_day = "0" + str_day
        if len(str_month) == 1:
            str_month = "0" + str_month
        data_json = requests.get(
            f"https://www.cbr-xml-daily.ru/archive/{str_year}/{str_month}/{str_day}/daily_json.js"
        ).json()
        try:
            data["rouble"].append(data_json["Valute"]["USD"]["Value"])
            data["date"].append(data_json["Date"][0:-15])
        except:
            data["rouble"].append("-")
            data["date"].append(f"{str_year}-{str_month}-{str_day}")
        if day == 1:
            if month == 1:
                month = 12
                year -= 1
            else:
                month -= 1
            if month in (1, 3, 5, 7, 8, 10, 12):
                day = 31
            elif month in (4, 6, 9, 11):
                day = 30
            elif month == 2:
                if year % 4 == 0:
                    day = 28
                else:
                    day = 29
        else:
            day -= 1
    return data


def create_CSV(data: dict, to: str):
    df = pd.DataFrame(data)
    df.to_csv(to, sep=",", encoding="utf-8")


output_data = get_data(23, 10, 2023, 30)
create_CSV(output_data, "dollar_course.csv")
