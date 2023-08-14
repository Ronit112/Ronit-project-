class Doctor:
    def __init__(self, id, name, specialization, working_time, qualification, room_number):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def format_info(self):
        return f"{self.id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"

    def enter_info(self):
        self.id = input("Enter Doctor ID: ")
        self.name = input("Enter Doctor Name: ")
        self.specialization = input("Enter Doctor Specialization: ")
        self.working_time = input("Enter Doctor Working Time: ")
        self.qualification = input("Enter Doctor Qualification: ")
        self.room_number = input("Enter Doctor Room Number: ")

    def display_info(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Specialization: {self.specialization}")
        print(f"Working Time: {self.working_time}")
        print(f"Qualification: {self.qualification}")
        print(f"Room Number: {self.room_number}")


# Sample data
sample_data = [
    "21_Dr.Gody_ENT_5-11AM_MBBS,MD_17",
    "32_Dr.Vikram_Physician_10-3AM_MBBS,MD_45",
    "17_Dr.Amy_Surgeon_8-2AM_BDM_8",
    "33_Dr.David_Artho_10-4PM_MBBS,MS_40",
    "123_Dr. Ross_Headackes_8-10am_Mst_102"
]

# Create Doctor objects from sample data
doctors = [Doctor(*data.split("_")) for data in sample_data]

# Display list of doctors
print("List of Doctors:")
for doctor in doctors:
    doctor.display_info()
    print("-" * 20)

# Search for doctor by ID
search_id = input("Enter Doctor ID to search: ")
found_doctor = next((doctor for doctor in doctors if doctor.id == search_id), None)
if found_doctor:
    print("\nSearch Result by ID:")
    found_doctor.display_info()
else:
    print(f"\nDoctor with ID {search_id} not found.")
