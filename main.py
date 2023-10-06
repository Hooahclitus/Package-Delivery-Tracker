from truck import *
from navigation import *
from csv_parser import *
from datetime import time


def process_deliveries(truck, end_time=None):
    while truck.get('cargo'):
        (address, distance) = next(iter(closest_delivery_location(truck).items()))
        update_arrive_time(truck, distance)

        match end_time:
            case None:
                deliver_packages(truck, address, distance, 'Delivered')
            case enroute if end_time > truck.get('depart_time') and end_time < truck.get('arrive_time'):
                handle_enroute(truck, address, end_time)
                return truck
            case arrive if end_time == truck.get('arrive_time'):
                handle_arrive(truck, address, distance)
                return truck
            case depart if end_time == truck.get('depart_time'):
                handle_depart(truck)
                return truck
            case _:
                deliver_packages(truck, address, distance, 'Delivered')

    return_to_hub(truck)
    return truck

def main():
    package_data = create_package_data('data/package_data.csv')

    truck_1_packages = package_data.get(*[1, 4, 6, 7, 25, 26, 28, 29, 30, 31, 32, 40])
    truck_2_packages = package_data.get(*[3, 5, 13, 14, 15, 16, 18, 19, 20, 21, 34, 36, 37, 38, 39])
    truck_3_packages = package_data.get(*[2, 8, 9, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35])

    truck_1 = create_truck(truck_1_packages, depart_time=time(9, 5))
    truck_2 = create_truck(truck_2_packages, depart_time=time(8))

    process_deliveries(truck_1)
    process_deliveries(truck_2)

    for package in truck_3_packages:
        if package.get('id') == '9':
            package.assoc('address', '410 S State St')
    
    truck_3 = create_truck(truck_3_packages, depart_time=time(10,20))

    process_deliveries(truck_3)

    for package in truck_1.get('log'):
        print(f"ID: {package.get('id'):4} ADDRESS: {package.get('address')[:30]:30} STATUS: {package.get('status'):12} TIME: {package.get('delivery_time'):10} DEADLINE: {package.get('has_deadline'):4}")
    print(f"Truck 1 ARRIVED AT HUB: {truck_1.get('arrive_time')} Distance Traveled: {round(truck_1.get('distance'), 2):<10}")

    for package in truck_2.get('log'):
        print(f"ID: {package.get('id'):4} ADDRESS: {package.get('address')[:30]:30} STATUS: {package.get('status'):12} TIME: {package.get('delivery_time'):10} DEADLINE: {package.get('has_deadline'):4}")
    print(f"Truck 2 ARRIVED AT HUB: {truck_2.get('arrive_time')} Distance Traveled: {round(truck_2.get('distance'), 2):<10}")

    for package in truck_3.get('log'):
        print(f"ID: {package.get('id'):4} ADDRESS: {package.get('address')[:30]:30} STATUS: {package.get('status'):12} TIME: {package.get('delivery_time'):10} DEADLINE: {package.get('has_deadline'):4}")
    print(f"Truck 3 ARRIVED AT HUB: {truck_3.get('arrive_time')} Distance Traveled: {round(truck_3.get('distance'), 2):<10}")

    print(f"COMBINED DISTANCE TRAVELED: {round(sum([truck.get('distance') for truck in [truck_1, truck_2, truck_3]]), 2)}")

main()
