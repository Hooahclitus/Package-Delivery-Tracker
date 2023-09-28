from hash_table import *
from navigation import *

# todo: remove destination if not needed
def create_truck(cargo=None):
    truck = HashTable(6, 
        'hub', '4001 South 700 East',
        'location', '4001 South 700 East', 
        # 'destination', None,
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
# todo: remove package.update for status
def deliver_packages(truck):
    for index, package in enumerate(truck.get('cargo')):
        if package.get('addr') == truck.get('location'):
            # package.update('status', 'Delivered')
            unload_cargo(truck, index) 
            log_cargo(truck, f"ID: {package.get('id')}, ADDRESS: {package.get('addr')}, STATUS: {package.get('status')}")
    return truck

def update_distance_traveled(truck, distance):
    truck.update('distance', truck.get('distance') + distance)
    return truck

# def change_position(truck):
#     destination = shortest_destination(truck)
#     destination_address = destination[0]
#     distance = destination[1]

#     truck.update('location', destination_address, 'destination', None, 'distance', truck.get_value('distance') + distance)
#     return truck
