tasks = []
completed = []

while True:
    print("\n" + "=" *30)
    print("          📝 TO-DO LIST")
    print("=" *30)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Clear All Tasks")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    # Add Task
    if choice == "1":
        task = input("Enter your task: ")

        if task.strip() == "":
            print("Task cannot be empty!")
        else:
            tasks.append(task)
            completed.append(False)
            print("✓ Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            print("-" * 40)

            for i in range(len(tasks)):
                if completed[i]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(f"{i + 1}. {tasks[i]} - {status}")

            print("-" * 40)
            print(f"Total Tasks     : {len(tasks)}")
            print(f"Completed Tasks : {completed.count(True)}")
            print(f"Pending Tasks   : {completed.count(False)}")

    # Mark Task as Completed
    elif choice == "3":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            number = int(input("Enter task number to complete: "))

            if 1 <= number <= len(tasks):
                completed[number - 1] = True
                print("✓ Task marked as completed!")
            else:
                print("Invalid task number.")

    # Update Task
    elif choice == "4":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            number = int(input("Enter task number to update: "))

            if 1 <= number <= len(tasks):
                new_task = input("Enter the new task: ")

                if new_task.strip() == "":
                    print("Task cannot be empty!")
                else:
                    tasks[number - 1] = new_task
                    print("✓ Task updated successfully!")
            else:
                print("Invalid task number.")

    # Delete Task
    elif choice == "5":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)    
                completed.pop(number - 1)
                print("✓ Task deleted successfully!")
            else:
                print("Invalid task number.")

    # Clear All Tasks
    elif choice == "6":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            confirm = input("Are you sure you want to clear all tasks? (yes/no): ")

            if confirm.lower() == "yes":
                tasks.clear()
                completed.clear()
                print("✓ All tasks cleared!")
            else:
                print("Operation cancelled.")

    # Exit
    elif choice == "7":
        print("\nThank you for using To-Do List!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 7.")      