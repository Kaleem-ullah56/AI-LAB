todo = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        todo.append(task)
        print("Task added successfully")

    elif choice == "2":
        if len(todo) == 0:
            print("No tasks in list")
        else:
            print("\nYour Tasks:")
            i = 1
            for t in todo:
                print(i, ".", t)
                i = i + 1

    elif choice == "3":
        if len(todo) == 0:
            print("Nothing to remove")
        else:
            print("\nTasks:")
            i = 1
            for t in todo:
                print(i, ".", t)
                i = i + 1

            num = int(input("Enter task number to remove: "))
            if num > 0 and num <= len(todo):
                removed = todo.pop(num - 1)
                print("Removed:", removed)
            else:
                print("Invalid number")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Wrong choice, try again")