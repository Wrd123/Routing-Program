# user_interface.py
import datetime
from delivery import first_truck, second_truck, third_truck
from import_data_function import hash_table

# Convert a time string in 'HH:MM:SS' format into a timedelta object.
def convert_time(time_str):
    hours, minutes, seconds = time_str.split(":")
    return datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

def start_user_interface():
    # Calculate and display the total mileage traveled by all trucks.
    total_mileage = first_truck.miles_traveled + second_truck.miles_traveled + third_truck.miles_traveled
    total_mileage = round(total_mileage, 1)
    print("Total distance traveled for all trucks: {} miles".format(total_mileage))
    
    # Display the delivered package IDs for each truck.
    print("\nPackage IDs on " + first_truck.truck_id + ":")
    print(first_truck.delivered)
    print("\nPackage IDs on " + second_truck.truck_id + ":")
    print(second_truck.delivered)
    print("\nPackage IDs on " + third_truck.truck_id + ":")
    print(third_truck.delivered)
    print("\nType an option to:")

    running = True
    
    while running:
        print("[1] Single package STATUS details @ specific time")
        print("[2] FULL package details @ specific time")
        print("[0] Quit program")
        try:
            user_option = int(input("[?]: "))
            if user_option == 0:
                try:
                    print("Customer First, People Led, Innovation Driven.")
                    running = False
                except Exception as e:
                    print("Invalid input, try again")
            elif user_option == 1:
                try:
                    # Prompt for a time input in the correct format and convert it.
                    time_input = input("Enter time with format, HH:MM:SS: ")
                    time_obj = convert_time(time_input)
                    # Request the package ID from the user.
                    package_id = int(input("Enter package ID: "))
                    # Retrieve and display the package details.
                    package = hash_table.search(package_id)
                    print(package.fetch_details(time_obj))
                except Exception as e:
                    print("Invalid input, try again")
            elif user_option == 2:
                try:
                    # Prompt for a time input and convert it.
                    time_input = input("Enter time with format, HH:MM:SS: ")
                    time_obj = convert_time(time_input)
                    # Iterate over package IDs 1 through 40 and display their details.
                    for pkg_id in range(1, 41):
                        package = hash_table.search(pkg_id)
                        print(package.fetch_details(time_obj))
                except Exception as e:
                    print("Invalid input, try again")
            else:
                print("Invalid input, try again")
        except Exception as e:
            print("Invalid input, try again")

if __name__ == "__main__":
    start_user_interface()
