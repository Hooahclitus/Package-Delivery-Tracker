from itertools import chain

from controller.truck_controller import *
from utilities.data_processing import *

location_data = create_location_data('data/location_data.csv')


def closest_delivery_location(truck):
    destinations_data = location_data.get(truck.get('location'))
    destinations = [address for address in truck.get('cargo').keys()]
    valid_destinations = [(a, d) for a, d in destinations_data.items() if a in destinations]
    address, distance = min(valid_destinations, key=lambda e: e[1])

    return address, distance


def return_to_hub(truck):
    address = '4001 South 700 East'
    distance = location_data.get(truck.get('location')).get(address)

    update_arrive_time(truck, distance)
    update_location(truck, address)
    update_distance_traveled(truck, distance)

    return truck


def process_delivery(truck, address, distance, status):
    packages = truck.get('cargo').get(address)

    update_arrive_time(truck, distance)
    update_location(truck, address)
    update_distance_traveled(truck, distance)
    update_status_and_time(packages, status, truck.get('arrive_time'))
    log_cargo(truck, packages)
    unload_packages(truck, address)
    update_depart_time(truck)
    return truck


def process_enroute(truck):
    flattened_cargo = list(chain(*truck.get('cargo').values()))
    sorted_cargo = sorted(flattened_cargo, key=lambda kv: kv.get('id'))
    truck.assoc('log', truck.get('log') + sorted_cargo)
    truck.get('cargo').clear()
    return truck


def process_arrive(truck, address, distance):
    packages = truck.get('cargo').get(address)
    remaining_packages = truck.get('cargo').values()

    update_distance_traveled(truck, distance)
    update_status_and_time(packages, 'Delivered', truck.get('arrive_time'))
    log_cargo(truck, packages)
    unload_packages(truck, address)
    log_cargo(truck, *remaining_packages)
    dump_cargo(truck)
    return truck


def process_depart(truck):
    remaining_packages = truck.get('cargo').values()

    log_cargo(truck, *remaining_packages)
    dump_cargo(truck)
    return truck
