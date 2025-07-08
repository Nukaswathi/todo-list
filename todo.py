tasks = []

while True:
    print("\n=== TO-DO LIST MENU ===")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
