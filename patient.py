class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def format_info(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"

    @staticmethod
    def enter_patient_info():
        pid = input("Enter the patient's ID: ")
        name = input("Enter the patient's name: ")
        disease = input("Enter the patient's disease: ")
        gender = input("Enter the patient's gender: ")
        age = input("Enter the patient's age: ")
        return Patient(pid, name, disease, gender, age)

    @staticmethod
    def read_patients_file(file_name):
        patients = []
        try:
            with open(file_name, "r") as file:
                for line in file:
                    parts = line.strip().split("_")
                    patient = Patient(parts[0], parts[1], parts[2], parts[3], parts[4])
                    patients.append(patient)
        except FileNotFoundError:
            print("Patients file not found.")
        return patients

    @staticmethod
    def search_patient_by_id(patients, target_id):
        for patient in patients:
            if patient.pid == target_id:
                return patient
        return None

    @staticmethod
    def display_patients_list(patients):
        print("ID   Name                   Disease         Gender          Age")
        for patient in patients:
            print(f"{patient.pid:4} {patient.name:20} {patient.disease:15} {patient.gender:15} {patient.age:15}")

    @staticmethod
    def write_list_of_patients_to_file(patients, file_name):
        try:
            with open(file_name, "w") as file:
                for patient in patients:
                    file.write(patient.format_info() + "\n")
            print("Patients list written to file.")
        except Exception as e:
            print("An error occurred while writing to the file:", str(e))

    @staticmethod
    def add_patient_to_file(patients, patient, file_name):
        patients.append(patient)
        Patient.write_list_of_patients_to_file(patients, file_name)
        print("Patient added successfully.")

# Sample data: patients.txt (data file provided)
file_name = "patients.txt"
patients = Patient.read_patients_file(file_name)

# Display patients list
Patient.display_patients_list(patients)

# Example usage of methods
new_patient = Patient.enter_patient_info()
patients.append(new_patient)
Patient.write_list_of_patients_to_file(patients, file_name)

search_id = input("Enter the patient's ID to search: ")
found_patient = Patient.search_patient_by_id(patients, search_id)
if found_patient:
    print("Patient found:")
    print(f"ID: {found_patient.pid}")
    print(f"Name: {found_patient.name}")
    print(f"Disease: {found_patient.disease}")
    print(f"Gender: {found_patient.gender}")
    print(f"Age: {found_patient.age}")
else:
    print("Patient not found.")
