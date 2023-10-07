from datetime import time

from navigation import *


def lookup_package_by_id(target_id, trucks):
    for truck in trucks:
        for package in truck.get('log'):
            if package.get('id') == target_id:
                print(package)


def process_deliveries(truck, end_time):
    while truck.get('cargo'):
        address, distance = next(iter(closest_delivery_location(truck).items()))
        update_arrive_time(truck, distance)

        match end_time:
            case None:
                deliver_packages(truck, address, distance, 'Delivered')
            case _ if truck.get('depart_time') < end_time < truck.get('arrive_time'):
                handle_enroute(truck, address, end_time)
                return truck
            case _ if end_time == truck.get('arrive_time'):
                handle_arrive(truck, address, distance)
                return truck
            case _ if end_time <= truck.get('depart_time'):
                handle_depart(truck)
                return truck
            case _:
                deliver_packages(truck, address, distance, 'Delivered')
    return_to_hub(truck)

    return truck


def initialize_and_process_trucks(end_time):
    package_data = create_package_data('data/package_data.csv')

    cargo_1 = package_data.get(*[1, 4, 6, 7, 25, 26, 28, 29, 30, 31, 32, 40])
    cargo_2 = package_data.get(*[3, 5, 13, 14, 15, 16, 18, 19, 20, 21, 34, 36, 37, 38, 39])
    cargo_3 = package_data.get(*[2, 8, 9, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35])

    for package in cargo_3:
        if package.get('id') == '9':
            package.assoc('address', '410 S State St')

    cargo_list = [cargo_1, cargo_2, cargo_3]
    truck_times = [time(9, 5), time(8), time(10, 20)]

    truck_1, truck_2, truck_3 = [
        process_deliveries(create_truck(cargo, depart_time=depart_time), end_time)
        for cargo, depart_time in zip(cargo_list, truck_times)
    ]

    return truck_1, truck_2, truck_3


def main(target_id=None, end_time=None):
    truck_1, truck_2, truck_3 = initialize_and_process_trucks(end_time)

    if target_id:
        lookup_package_by_id(target_id, [truck_1, truck_2, truck_3])

    for package in truck_1.get('log'):
        print(
            f"ID: {package.get('id'):4} "
            f"ADDRESS: {package.get('address')[:30]:30} "
            f"STATUS: {package.get('status'):12} "
            f"TIME: {package.get('delivery_time'):10} "
            f"DEADLINE: {package.get('has_deadline'):4}")
    print(
        f"Truck 1 ARRIVED AT HUB: {truck_1.get('arrive_time')} "
        f"Distance Traveled: {round(truck_1.get('distance'), 2):<10}")

    for package in truck_2.get('log'):
        print(
            f"ID: {package.get('id'):4} "
            f"ADDRESS: {package.get('address')[:30]:30} "
            f"STATUS: {package.get('status'):12} "
            f"TIME: {package.get('delivery_time'):10} "
            f"DEADLINE: {package.get('has_deadline'):4}")
    print(
        f"Truck 2 ARRIVED AT HUB: {truck_2.get('arrive_time')} "
        f"Distance Traveled: {round(truck_2.get('distance'), 2):<10}")

    for package in truck_3.get('log'):
        print(
            f"ID: {package.get('id'):4} "
            f"ADDRESS: {package.get('address')[:30]:30} "
            f"STATUS: {package.get('status'):12} "
            f"TIME: {package.get('delivery_time'):10} "
            f"DEADLINE: {package.get('has_deadline'):4}")
    print(
        f"Truck 3 ARRIVED AT HUB: {truck_3.get('arrive_time')} "
        f"Distance Traveled: {round(truck_3.get('distance'), 2):<10}")

    print(
        f"COMBINED DISTANCE TRAVELED: "
        f"{round(sum([truck.get('distance') for truck in [truck_1, truck_2, truck_3]]), 2)}")


main()
