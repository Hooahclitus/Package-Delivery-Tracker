from datetime import datetime, date, timedelta


def distance_to_seconds(distance):
    return distance * 200

def seconds_to_distance(seconds):
    return seconds * 0.005

def difference_of_times(time_1, time_2):
    t1 = datetime.combine(date.today(), time_1)
    t2 = datetime.combine(date.today(), time_2)

    t1_delta = timedelta(hours=t1.hour, minutes=t1.minute, seconds=t1.second)
    t2_delta = timedelta(hours=t2.hour, minutes=t2.minute, seconds=t2.second)
    
    return t2_delta - t1_delta
