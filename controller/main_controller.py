from datetime import time

from controller.delivery_controller import *
from controller.truck_controller import *
from utilities.data_processing import *


# Initialize trucks, assign cargo, and process their routes
def initialize_and_process_trucks(end_time=None):
    # Load package data from CSV file
    package_data = create_package_data()

    # Create cargo lists for each truck
    cargo_1 = package_data.get(*[1, 4, 6, 7, 25, 26, 28, 29, 30, 31, 32, 40])
    cargo_2 = package_data.get(
        *[3, 5, 13, 14, 15, 16, 18, 19, 20, 21, 34, 36, 37, 38, 39]
    )
    cargo_3 = package_data.get(*[2, 8, 9, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35])

    cargo_list = [cargo_1, cargo_2, cargo_3]
    depart_hub_times = [time(9, 5), time(8), time(10, 20)]

    # Process routes for each truck
    truck_1, truck_2, truck_3 = [
        process_route(create_truck(cargo, depart_time, truck_id), end_time)
        for cargo, depart_time, truck_id in zip(cargo_list, depart_hub_times, [1, 2, 3])
    ]

    return [truck_1, truck_2, truck_3]


# Manage the delivery route for a single truck
def process_route(truck, end_time):
    flattened_cargo = list(chain(*truck.get("cargo").values()))

    # Handle cases where end_time exists and is before truck departure
    if end_time and end_time < truck.get("depart_hub"):
        sorted_cargo = sorted(flattened_cargo, key=lambda kv: kv.get("id"))
        truck.assoc("log", sorted_cargo)
        truck.get("cargo").clear()
        return truck

    # Update package status and address corrections
    for package in flattened_cargo:
        package.assoc("status", "En Route")

        if truck.get("depart_hub") >= time(10, 20) and package.get("wrong_address"):
            package.assoc("address", "410 S State St")

    # Main delivery loop
    while truck.get("cargo").items():
        address, distance = closest_delivery_location(truck)
        update_arrive_time(truck, distance)

        # Decide how to update the truck and cargo based on end_time
        if end_time is None:
            process_delivery(truck, address, distance, "Delivered")
        elif truck.get("depart_time") < end_time < truck.get("arrive_time"):
            process_enroute(truck)
            return truck
        elif end_time == truck.get("arrive_time"):
            process_arrive(truck, address, distance)
            return truck
        elif end_time <= truck.get("depart_time"):
            process_depart(truck)
            return truck
        else:
            process_delivery(truck, address, distance, "Delivered")

    # Return truck to hub after all deliveries
    process_to_hub(truck)
    return truck
