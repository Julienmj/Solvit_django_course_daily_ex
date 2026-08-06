mg = []

while True:
    print("\n===== STUDENT MENU =====")
    print("1. Create Student")
    print("2. Read Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose an option: ")

    # CREATE
    if choice == "1":
        student = {}
        student["name"] = input("Name: ")
        student["marks"] = input("Marks: ")

        mg.append(student)
        print("Student added.")

    # READ
    elif choice == "2":
        if len(mg) == 0:
            print("No students found.")
        else:
            for i in range(len(mg)):
                print(i, mg[i])

    # UPDATE
    elif choice == "3":
        index = int(input("Enter student index: "))

        if index < len(mg):
            mg[index]["name"] = input("New Name: ")
            mg[index]["marks"] = input("New Marks: ")
            print("Student updated.")
        else:
            print("Invalid index.")

    # DELETE
    elif choice == "4":
        index = int(input("Enter student index: "))

        if index < len(mg):
            mg.pop(index)
            print("Student deleted.")
        else:
            print("Invalid index.")

    # EXIT
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")