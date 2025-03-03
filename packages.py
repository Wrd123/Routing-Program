import datetime

class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes):
        self.package_id = package_id
        self.address = address  # original (wrong) address from CSV for routing
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.departure_time = None
        self.delivery_time = None
        self.status = "at hub"

    # New method that returns the dynamic address components based on the current time.
    def get_address_components(self, current_time):
        correction_time = datetime.timedelta(hours=10, minutes=20, seconds=0)
        if self.package_id == 9:
            if current_time >= correction_time:
                # Return corrected address components.
                return ("410 S. State St.", "Salt Lake City", "UT", "84111")
            else:
                # Return incorrect address components.
                return ("300 State St.", "Salt Lake City", "UT", "84103")
        else:
            # For all other packages, return the static address components.
            return (self.address, self.city, self.state, self.zip_code)

    # The get_address method used for routing (if needed) can return a full string.
    def get_address(self, current_time):
        street, city, state, zip_code = self.get_address_components(current_time)
        return f"{street}, {city}, {state} {zip_code}"

    # Updated fetch_details uses get_address_components to display address parts.
    def fetch_details(self, current_time):
        # Get the proper address components.
        street, city, state, zip_code = self.get_address_components(current_time)

        if self.delivery_time is not None and current_time >= self.delivery_time:
            current_status = (
                f"Status: delivered\t Delivered Time: {self.delivery_time}\t Delivered by: {self.delivered_by}"
            )
        elif self.delivery_time is not None and self.departure_time is not None and self.delivery_time > current_time > self.departure_time:
            current_status = f"Status: en route {self.en_route_truck}"
        else:
            current_status = "Status: at hub"

        return (
            f"Package ID: {self.package_id:<5} "
            f"Address: {street:<40} "
            f"City: {city:<20} "
            f"State: {state:<5} "
            f"Zip Code: {zip_code:<10} "
            f"Deadline: {self.deadline:<10} "
            f"Weight(kg): {self.weight:<5} "
            f"{current_status:<30} "
            f"Notes: {self.notes:<30}"
        )
