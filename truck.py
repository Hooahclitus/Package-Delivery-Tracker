from utils import *
from package import *
from hash_table import *
from datetime import datetime, date, time, timedelta


def create_truck(cargo=None):
    truck = HashTable(6,
        "location", "4001 South 700 East",
        "depart_time", None,
        "arrive_time", None,
        "cargo", group_by_address(cargo),
        "distance", 0,
        "log", [],
    )
    return truck


def load_cargo(truck, cargo):
    truck.assoc("cargo", cargo)
    return truck


def unload_packages(truck, packages, address):
    log_cargo(truck, packages)
    truck.get("cargo").pop(address)
    return truck


def dump_cargo(truck, remaining_packages):
    log_cargo(truck, *remaining_packages)
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
