from utils import *
from hash_table import *
from datetime import datetime, date, time, timedelta

# todo: remove destination if not needed
def create_truck(cargo=None, time=time(8, 00)):
    truck = HashTable(6, 
        'location', '4001 South 700 East', 
        'arrive_time', time,
        'depart_time', time,
        'cargo', cargo,
        'distance', 0,
        'log', []
    )
    return truck
    
def load_cargo(truck, cargo):
    truck.insert('cargo', cargo)
    return truck

def unload_cargo(truck, index):
    truck.get('cargo').pop(index)
    return truck

def log_cargo(truck, entry):
    truck.get('log').append(entry)
    return truck

def deliver_packages(truck):
    for index, package in enumerate(truck.get('cargo')):
        if package.get('addr') == truck.get('location'):
            unload_cargo(truck, index) 
            log_cargo(truck, f"ID: {package.get('id')}, ADDRESS: {package.get('addr')}, STATUS: Delivered, TIME: {truck.get('arrive_time')}")
    return truck

def update_distance_traveled(truck, distance):
    truck.update('distance', truck.get('distance') + distance)
    return truck

def update_location(truck, address):
    truck.update('location', address)
    return truck

def update_arrive_time(truck, distance):
    truck.update('arrive_time', (datetime.combine(date.today(), truck.get('depart_time')) + timedelta(seconds=distance_to_seconds(distance))).time())
    return truck

def update_depart_time(truck):
    truck.update('depart_time', truck.get('arrive_time'))
    return truck
