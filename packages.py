# packages.py
# Class representing a package with its associated delivery information.
class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.departure_time = None
        self.delivery_time = None
        self.status = "at hub"

    # Method to retrieve all package details based on a given time input.
    '''
     It returns data such as the package ID, delivery address, deadline, city, zip code, weight,
     and the current delivery status (i.e., "at hub", "en route", or "delivered")
     with delivery time when applicable.
     
    '''
    def fetch_details(self, current_time):
        if self.delivery_time is not None and current_time >= self.delivery_time:
            # Include the truck that delivered the package
            current_status = f"Status: delivered\t Delivered Time: {self.delivery_time}\t Delivered by: {self.delivered_by}"
        elif self.delivery_time is not None and self.departure_time is not None and self.delivery_time > current_time > self.departure_time:
            current_status = f"Status: en route on {self.en_route_truck}"
        else:
            # Otherwise, the package remains at the hub.
            current_status = "Status: at hub"

        # Construct and return the full package details as a formatted string.
        return (
            f"Package ID: {self.package_id:<5} "
            f"Address: {self.address:<40} "
            f"City: {self.city:<20} "
            f"State: {self.state:<5} "
            f"Zip Code: {self.zip_code:<10} "
            f"Deadline: {self.deadline:<10} "
            f"Weight(kg): {self.weight:<5} "
            f"{current_status:<25} "
            f"Notes: {self.notes:<30}"
)

