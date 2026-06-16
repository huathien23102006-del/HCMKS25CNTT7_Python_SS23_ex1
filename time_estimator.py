import datetime

def predict_eta(departure_str, distance_km, speed=60):
    dep_time = datetime.datetime.strptime(departure_str, "%Y-%m-%d %H:%M:%S")
    hours_needed = distance_km / speed
    return dep_time + datetime.timedelta(hours=hours_needed)
