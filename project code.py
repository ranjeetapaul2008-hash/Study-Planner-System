# Simple Study Planner
# Class 11 CBSE Level                                                                                        

tasks=[]
while True:
    print("STUDY PLANNER")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        subject = input("Enter subject name: ")
        work = input("Enter work to do: ")
        date = input("Enter date (DD-MM-YYYY): ")

        task = subject + " - " + work + " - " + date
        tasks.append(task)

        print("Task added successfully!")

    elif choice == "2":                                                                                                
        if len(tasks) == 0:
            print("No tasks added yet.")
        else:
            print("Your Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        print("Exiting Study Planner. Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
