from hash_table import *


def create_truck(cargo=None):
    table = HashTable(6, 
        'location', '4001 South 700 East', 
        'destination', None,
        'depart_time', None,
        'arrive_time', None,
        'hub', '4001 South 700 East',
        'cargo', cargo
    )
    return table
    
def load_cargo(truck, cargo):
    truck.insert_item('cargo', cargo)
    return truck
        
