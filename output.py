def print_route_data(trucks):
    for truck in trucks:
        for package in truck.get('log'):
            print(
                f"ID: {package.get('id'):4} "
                f"ADDRESS: {package.get('address')[:30]:30} "
                f"STATUS: {package.get('status'):12} "
                f"TIME: {package.get('delivery_time'):10} "
                f"DEADLINE: {package.get('has_deadline'):4}")

        print(
            f"Truck 1 ARRIVED AT HUB: {truck.get('arrive_time')} "
            f"Distance Traveled: {round(truck.get('distance'), 2):<10}")


def print_distance_traveled(trucks):
    print(
        f"COMBINED DISTANCE TRAVELED: "
        f"{round(sum([truck.get('distance') for truck in trucks]), 2)}"
    )
