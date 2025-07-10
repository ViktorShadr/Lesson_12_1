from datetime import datetime, timedelta

def get_days_between_dates(date1, date2):
    date_obj_start = datetime.strptime(date1, "%d.%m.%Y")
    date_obj_end = datetime.strptime(date2, "%d.%m.%Y")
    return (date_obj_end - date_obj_start).days


print(get_days_between_dates("01.01.2022", "31.01.2022"))