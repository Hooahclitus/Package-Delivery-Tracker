def display_main_menu():
    print("Main Menu:")
    print("1) Print delivery data from a start and end time:")
    print("2) Print delivery data for today:")
    print("3) Lookup package status by ID:")


def ask_for_time(time_name):
    return input(f"Please enter {time_name} time (or type 'q' to quit): ")


def ask_for_package_id():
    return input("Please enter a package ID between 1 and 40 (or type 'q' to quit): ")


def ask_for_selection():
    return input("Please enter your selection (or type 'q' to quit): ").lower()


def show_invalid_time():
    print("Invalid time. Please try again.")


def show_invalid_package_id():
    print("Invalid package ID. Please try again.")


def show_invalid_input():
    print("Invalid input. Please try again.")


def show_quit_message():
    print("Quitting program!")
