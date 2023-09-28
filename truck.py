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
        'distance', 0
    )
    return truck
    
def load_cargo(truck, cargo):
    truck.insert('cargo', cargo)
    return truck

def deliver_packages(truck):
    for package in truck.get('cargo'):
        if package.get('addr') == truck.get('location'):
            package.update('status', 'Delivered')
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
