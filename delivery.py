# delivery.py
import datetime
from trucks import *
from import_data_function import distance_data, address_data, hash_table

# Initialize trucks with their assigned package IDs and scheduled departure times.
first_truck = Truck(
    [13, 14, 15, 16, 19, 20, 1, 29, 30, 31, 34, 37, 40],
    datetime.timedelta(hours=8, minutes=0, seconds=0),
    "Truck One"
)
second_truck = Truck(
    [3, 6, 18, 25, 28, 32, 36, 38, 27, 35, 39],
    datetime.timedelta(hours=9, minutes=5, seconds=0),
    "Truck Two"
)
third_truck = Truck(
    [9, 2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 33],
    datetime.timedelta(hours=10, minutes=20, seconds=0),
    "Truck Three"
)

# Returns the index position of the specified address within the address list.
def lookup_address_index(address):
    return address_data.index(address)

# Calculates the distance between two addresses by referencing the distance matrix.
def compute_distance(address1, address2):
    return float(distance_data[lookup_address_index(address1)][lookup_address_index(address2)])

# Finds the next closest delivery location by determining the minimal distance from the truck's current location.
def find_nearest_delivery(truck):
    travel_distances = []
    # Iterate over all packages that have yet to be delivered.
    for package_id in truck.not_delivered:
        package_address = hash_table.search(package_id).address
        distance_val = compute_distance(truck.current_address, package_address)
        travel_distances.append(float(distance_val))
    # Identify the shortest travel distance and its corresponding index.
    closest_distance = min(travel_distances)
    closest_index = travel_distances.index(closest_distance)
    return closest_index, closest_distance

# Implements the delivery routine using a nearest neighbor strategy.
def execute_delivery(truck):
    # Update each package's status to en route and assign the departure time.
    for package_id in truck.not_delivered:
        package = hash_table.search(package_id)
        package.status = "en route"
        package.departure_time = truck.depart_time
        package.en_route_truck = truck.truck_id  # NEW: record which truck is carrying the package
        truck.current_time = truck.depart_time

    # Process deliveries until all packages have been delivered.
    while truck.not_delivered:
        nearest_idx, travel_distance = find_nearest_delivery(truck)
        target_package = hash_table.search(truck.not_delivered[nearest_idx])
        truck.current_address = target_package.address
        truck.miles_traveled += travel_distance
        # Update the truck's current time based on the travel duration (assuming a speed of 18 mph).
        truck.current_time += datetime.timedelta(hours=travel_distance / 18)
        # Mark the package as delivered and record its delivery time.
        target_package.status = "delivered"
        target_package.delivery_time = truck.current_time
        target_package.delivered_by = truck.truck_id  #record the truck identifier
        # Transfer the package from the undelivered list to the delivered list.
        truck.delivered.append(truck.not_delivered[nearest_idx])
        truck.not_delivered.remove(truck.not_delivered[nearest_idx])

    # Compute the distance from the final delivery location back to the hub.
    last_delivery_address = hash_table.search(truck.delivered[-1]).address
    return_to_hub_distance = compute_distance(last_delivery_address, truck.end_address)
    truck.miles_traveled += return_to_hub_distance
    truck.miles_traveled = round(truck.miles_traveled, 1)
    truck.current_time += datetime.timedelta(hours=return_to_hub_distance / 18)
    print(truck.truck_id + " departed hub at: " + str(truck.depart_time))
    print(truck.truck_id + " returned to hub at: " + str(truck.current_time))
    print(truck.truck_id + " traveled " + str(truck.miles_traveled) + " miles")
