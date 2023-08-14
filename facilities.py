class Facility:
    def __init__(self, facility_name):
        self.facility_name = facility_name

    def add_facility(self):
        self.facility_name = input("Enter Facility Name: ")

    def display_facilities(self):
        print(self.facility_name)

    def write_to_file(self, filename):
        with open(filename, "a") as file:
            file.write(self.facility_name + "\n")

    @staticmethod
    def write_list_to_file(facilities, filename):
        with open(filename, "w") as file:
            for facility in facilities:
                file.write(facility.facility_name + "\n")

    @staticmethod
    def read_from_file(filename):
        facilities = []
        with open(filename, "r") as file:
            for line in file:
                facility_name = line.strip()
                facility = Facility(facility_name)
                facilities.append(facility)
        return facilities

    def format_info(self):
        return self.facility_name


# Sample data
sample_facility_data = [
    "Ambulance",
    "Admit Facility",
    "Canteen",
    "Emergency"
]

# Create Facility objects from sample data
facilities = [Facility(name) for name in sample_facility_data]

# Write sample data to file
Facility.write_list_to_file(facilities, "facilities.txt")

# Read data from file and create Facility objects
facilities_from_file = Facility.read_from_file("facilities.txt")

# Display list of facilities
print("The Hospital Facilities are:")
for facility in facilities_from_file:
    print(facility.format_info())

# Add a new facility and update file
new_facility = Facility("")
new_facility.add_facility()
facilities_from_file.append(new_facility)
Facility.write_list_to_file(facilities_from_file, "facilities.txt")

# Display updated list of facilities
print("\nUpdated List of Facilities:")
updated_facilities = Facility.read_from_file("facilities.txt")
for facility in updated_facilities:
    print(facility.format_info())
