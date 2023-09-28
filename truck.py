from hash_table import *

def create_truck(cargo=None):
    truck = HashTable(6, 
        'hub', '4001 South 700 East',
        'location', '4001 South 700 East', 
        'destination', None,
        'depart_time', None,
        'arrive_time', None,
        'cargo', cargo,
        'distance', 0
    )
    return truck
    
def load_cargo(truck, cargo):
    truck.insert_item('cargo', cargo)
    return truck

def deliver_packages(truck):
    for package in truck.get_value('cargo'):
        if package.get_value('addr') == truck.get_value('location'):
            package.update('status', 'Delivered')

def update_distance_traveled(truck, distance):
    truck.update('distance', truck.get_value('distance') + distance)
