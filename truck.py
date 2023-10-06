from utils import *
from package import *
from hash_table import *
from datetime import datetime, date, time, timedelta


def create_truck(cargo=None, depart_time=None, arrive_time=None):
    truck = HashTable(6,
        "location", "4001 South 700 East",
        "depart_time", depart_time,
        "arrive_time", arrive_time,
        "cargo", group_by_address(cargo),
        "distance", 0,
        "log", [],
    )
    return truck


def load_cargo(truck, cargo):
    truck.assoc("cargo", group_by_address(cargo))
    return truck


def unload_packages(truck, address):
    del truck.get("cargo")[address]
    return truck


def dump_cargo(truck, remaining_packages):
    truck.get("cargo").clear()
    return truck


def log_cargo(truck, *packages):
    for package in packages:
        truck.assoc("log", truck.get("log") + package)
    return truck


def update_distance_traveled(truck, distance):
    truck.assoc("distance", truck.get("distance") + distance)
    return truck


def update_location(truck, address):
    truck.assoc("location", address)
    return truck


def update_arrive_time(truck, distance):
    truck.assoc(
        "arrive_time", (
            datetime.combine(date.today(), 
                truck.get("depart_time")) + 
                timedelta(seconds=distance_to_seconds(distance))
            ).time())
    return truck


def update_depart_time(truck):
    truck.assoc("depart_time", truck.get("arrive_time"))
    return truck


def deliver_packages(truck, address, distance, status):
    packages = truck.get('cargo').get(address)

    update_arrive_time(truck, distance)
    update_location(truck, address)
    update_distance_traveled(truck, distance)
    update_status_and_time(packages, status, truck.get('arrive_time'))
    log_cargo(truck, packages)
    unload_packages(truck, address)
    update_depart_time(truck)
    return truck

def handle_enroute(truck, address, end_time):
    packages = truck.get('cargo').get(address)
    remaining_packages = truck.get('cargo').values()
    end_time_distance = seconds_to_distance(
        difference_of_times(
            truck.get('depart_time'),
            end_time
        ).total_seconds()
    )

    update_distance_traveled(truck, end_time_distance)
    update_status_and_time(packages, 'En Route', end_time)
    log_cargo(truck, packages)
    unload_packages(truck, address)
    log_cargo(truck, *remaining_packages)
    dump_cargo(truck, remaining_packages)
    return truck

def handle_arrive(truck, address, distance):
    packages = truck.get('cargo').get(address)
    remaining_packages = truck.get('cargo').values()

    update_distance_traveled(truck, distance)
    update_status_and_time(packages, 'Delivered', truck.get('arrive_time'))
    log_cargo(truck, packages)
    unload_packages(truck, address)
    log_cargo(truck, *remaining_packages)
    dump_cargo(truck, remaining_packages)
    return truck

def handle_depart(truck):
    remaining_packages = truck.get('cargo').values()

    log_cargo(truck, *remaining_packages)
    dump_cargo(truck, remaining_packages)
    return truck
