from hash_table import *

# todo: remove destination if not needed
def create_truck(cargo=None):
    truck = HashTable(6, 
        'location', '4001 South 700 East', 
        'depart_time', None,
        'arrive_time', None,
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

# todo: add delivery time to log_cargo
def deliver_packages(truck):
    for index, package in enumerate(truck.get('cargo')):
        if package.get('addr') == truck.get('location'):
            unload_cargo(truck, index) 
            log_cargo(truck, f"ID: {package.get('id')}, ADDRESS: {package.get('addr')}, STATUS: Delivered")
    return truck

def update_distance_traveled(truck, distance):
    truck.update('distance', truck.get('distance') + distance)
    return truck

def update_location(truck, address):
    truck.update('location', address)
