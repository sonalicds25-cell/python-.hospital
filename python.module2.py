patients = []

def add_patient():
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    disease = input("Enter disease: ")

    patients.append({
        "Name": name,
        "Age": age,
        "Disease": disease
    })

    print("Patient added successfully!")

def view_patients():
    for p in patients:
        print(p)

while True:
    print("\n--- Hospital Management System ---")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        view_patients()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")