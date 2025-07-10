import json
from datetime import datetime, timedelta

def duration_in_days(events: list[dict])-> list:
    result = []
    for event in events:
        date_string_start = event['start_date']
        date_string_end = event['end_date']
        date_obj_start = datetime.strptime(date_string_start, "%Y-%m-%d")
        date_obj_end = datetime.strptime(date_string_end, "%Y-%m-%d")
        number_of_days = (date_obj_end - date_obj_start).days
        result.append(number_of_days)

    return result

with open('../data/events.json', 'r') as file:
    events_in_days = json.load(file)

print(duration_in_days(events_in_days))


