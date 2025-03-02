# Name: Ryan Deaton
# Student ID: 001468560

from user_interface import start_user_interface
from import_data_function import load_packages, load_addresses, load_distances
from delivery import execute_delivery, first_truck, second_truck, third_truck

print("Western Governors University Parcel Service Program\n")

# Begin importing data from CSV files.
# Load package objects into the global hash_table.
load_packages("csv/package_files.csv")

# Load addresses into the address_data list.
load_addresses("csv/addresses.csv")

# Load distances into the distance_data matrix.
# Note: distance_data[2][6] is the same as distance_data[6][2].
load_distances("csv/distances.csv")

# Execute the delivery routine for each truck.
execute_delivery(first_truck)
execute_delivery(second_truck)
execute_delivery(third_truck)

# Launch the user interface.
start_user_interface()
