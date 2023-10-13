import sys

from controller.main_controller import *
from view.delivery_view import *
from view.user_view import *


def parse_time(time_name):
    formats = ["%I:%M%p", "%I%p", "%H:%M", "%H:%M%p"]

    while True:
        user_input = ask_for_time(time_name)
        if user_input == 'q':
            show_quit_message()
            sys.exit()
        for fmt in formats:
            try:
                return datetime.strptime(user_input.replace(" ", "").upper(), fmt).time()
            except ValueError:
                continue
        show_invalid_time()


def parse_lookup_by_id(trucks):
    while True:
        user_input = ask_for_package_id()
        if user_input == 'q':
            show_quit_message()
            sys.exit()
        try:
            user_input = int(user_input)
            find_package_by_id(user_input, trucks)
            break
        except ValueError:
            show_invalid_package_id()


def main_interface():
    display_main_menu()

    while True:
        user_input = ask_for_selection()

        if user_input == '1':
            start_time = parse_time("start")
            end_time = parse_time("end")

            trucks = initialize_and_process_trucks(end_time)

            filtered_logs = [
                [
                    package for package in truck.get('log') if
                    package.get('delivery_time') == 'N/A' or
                    package.get('delivery_time') >= start_time
                ]
                for truck in trucks
            ]

            for log, truck in zip(filtered_logs, trucks):
                truck.assoc('log', log)
                if not log:
                    truck.assoc('distance', 0)

            output_travel_data(trucks)
            main_interface()
        elif user_input == '2':
            trucks = initialize_and_process_trucks()

            output_travel_data(trucks)
            main_interface()
        elif user_input == '3':
            trucks = initialize_and_process_trucks()

            parse_lookup_by_id(trucks)
            main_interface()
        elif user_input == 'q':
            show_quit_message()
            sys.exit()

        else:
            show_invalid_input()
