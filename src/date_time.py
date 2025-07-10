from datetime import datetime, timedelta


def time_remake(dates):
    new_dates =[]
    for date in dates:
        date_string = date
        date_obj = datetime.strptime(date_string, "%Y.%m.%d")
        new_date_obj = date_obj + timedelta(days=7)
        date_string = new_date_obj.strftime("%B %#d, %Y")
        new_dates.append(date_string)

    return new_dates

user_dates = ["2022.12.31", "2023.1.7"]
print(time_remake(user_dates))