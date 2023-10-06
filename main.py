from truck import *
from navigation import *
from csv_parser import *
from datetime import time


package_data = create_package_data('data/package_data.csv')

tk_1 = package_data.get(*[10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 34, 39])
truck_1 = create_truck(tk_1)

tk_2 = package_data.get(*[1, 2, 3, 4, 5, 7, 18, 27, 29, 30, 33, 35, 36, 37, 38, 40])
truck_2 = create_truck(tk_2)

tk_3 = package_data.get(*[6, 8, 9, 25, 26, 28, 31, 32])
truck_3 = create_truck(tk_3)


def process_deliveries(truck, start_time=time(8), end_time=None):
    truck.assoc('depart_time', start_time)

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

process_deliveries(truck_1)
for package in truck_1.get('log'):
    print(f"ID: {package.get('id'):4} ADDRESS: {package.get('address')[:30]:30} STATUS: {package.get('status'):12} TIME: {package.get('delivery_time'):10} DEADLINE: {package.get('has_deadline'):4}")
print(f"Distance Traveled: {round(truck_1.get('distance'), 2):<10} ARRIVAL TIME: {truck_1.get('arrive_time')}")


process_deliveries(truck_2)
for package in truck_2.get('log'):
    print(f"ID: {package.get('id'):4} ADDRESS: {package.get('address')[:30]:30} STATUS: {package.get('status'):12} TIME: {package.get('delivery_time'):10} DEADLINE: {package.get('has_deadline'):4}")
print(f"Distance Traveled: {round(truck_2.get('distance'), 2):<10} ARRIVAL TIME: {truck_2.get('arrive_time')}")


process_deliveries(truck_3, start_time=time(9,45))
for package in truck_3.get('log'):
    print(f"ID: {package.get('id'):4} ADDRESS: {package.get('address')[:30]:30} STATUS: {package.get('status'):12} TIME: {package.get('delivery_time'):10} DEADLINE: {package.get('has_deadline'):4}")
print(f"Distance Traveled: {round(truck_3.get('distance'), 2):<10} ARRIVAL TIME: {truck_3.get('arrive_time')}")


round(sum([truck.get('distance') for truck in [truck_1, truck_2, truck_3]]), 2)
