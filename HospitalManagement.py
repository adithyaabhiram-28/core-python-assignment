class Hospital:
    def __init__(self):
        self.patients = []
    def addPatient(self,patient):
        self.patients.append(patient)
    def searchPatient(self,disease):
        return [patient['Name'] for patient in self.patients if patient['Disease']==disease]

patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
hospital = Hospital()
for patient in patients:
    hospital.addPatient(patient)

search_disease = "Flu"
print("Patients with", search_disease, ":", hospital.searchPatient(search_disease))