from utils import *
from package import *
from hash_table import *
from datetime import datetime, date, time, timedelta


def create_truck(cargo=None, time=time(8, 00)):
    truck = HashTable(6,
        "location", "4001 South 700 East",
        "arrive_time", time,
        "depart_time", time,
        "cargo", cargo,
        "distance", 0,
        "log", [],
    )
    return truck


def load_cargo(truck, cargo):
    truck.insert("cargo", cargo)
    return truck


def unload_cargo(truck, address):
    truck.get("cargo").pop(address)
    return truck


def dump_cargo(truck):
    truck.get("cargo").clear()
    return truck


def log_cargo(truck, *packages):
    for package in packages:
        truck.update("log", truck.get("log") + package)
    return truck


def update_distance_traveled(truck, distance):
    truck.update("distance", truck.get("distance") + distance)
    return truck


def update_location(truck, address):
    truck.update("location", address)
    return truck


def update_arrive_time(truck, distance):
    truck.update(
        "arrive_time", (
            datetime.combine(date.today(), 
                truck.get("depart_time")) + timedelta(seconds=distance_to_seconds(distance))
            ).time())
    return truck


def update_depart_time(truck):
    truck.update("depart_time", truck.get("arrive_time"))
    return truck


def deliver_packages(truck, packages, address):
    update_status(packages, f"Delivered at {truck.get('arrive_time')}")
    log_cargo(truck, packages)
    unload_cargo(truck, address)
    update_depart_time(truck)
