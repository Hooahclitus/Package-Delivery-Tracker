from utilities.data_processing import *
from utilities.time_conversion import *


# Initialize truck with given parameters
def create_truck(cargo, depart_hub, truck_id=None):
    truck = HashTable(
        8,
        "id",
        truck_id,
        "location",
        "4001 South 700 East",
        "depart_hub",
        depart_hub,
        "depart_time",
        depart_hub,
        "arrive_time",
        depart_hub,
        "cargo",
        group_by_address(cargo),
        "distance",
        0,
        "log",
        [],
    )
    return truck


# Load cargo into truck
def load_cargo(truck, cargo):
    truck.assoc("cargo", cargo)
    return truck


# Unload packages at given address
def unload_packages(truck, address):
    truck.get("cargo").dissoc(address)
    return truck


# Clear all cargo from truck
def dump_cargo(truck):
    truck.get("cargo").clear()
    return truck


# Log delivered packages
def log_cargo(truck, *packages):
    for package in packages:
        truck.assoc("log", truck.get("log") + package)
    return truck


# Update truck's total distance traveled
def update_distance_traveled(truck, distance):
    truck.assoc("distance", truck.get("distance") + distance)
    return truck


# Update truck's current location
def update_location(truck, address):
    truck.assoc("location", address)
    return truck


# Update truck's arrival time based on distance
def update_arrive_time(truck, distance):
    depart_time = datetime.combine(date.today(), truck.get("depart_time"))
    arrival_timedelta = timedelta(seconds=distance_to_seconds(distance))
    expected_arrival_time = (depart_time + arrival_timedelta).time()

    truck.assoc("arrive_time", expected_arrival_time)
    return truck


# Update truck's departure time to its last arrival time
def update_depart_time(truck):
    truck.assoc("depart_time", truck.get("arrive_time"))
    return truck
