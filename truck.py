from hash_table import *

# todo: add distance traveled
def create_truck(cargo=None):
    table = HashTable(6, 
        'hub', '4001 South 700 East',
        'location', None, 
        'destination', None,
        'depart_time', None,
        'arrive_time', None,
        'cargo', cargo,
        'distance', 0
    )
    return table
    
def load_cargo(truck, cargo):
    truck.insert_item('cargo', cargo)
    return truck
        
