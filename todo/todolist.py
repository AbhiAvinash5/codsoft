tasks = []

print("=" * 30)
print("       TO-DO LIST")
print("=" * 30)

while True:

    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        if len(tasks) == 0:

            print("\nNo tasks available")

        else:

            print("\nYour Tasks:")

            for i in range(len(tasks)):

                print(f"{i + 1}. {tasks[i]}")

    elif choice == "2":

        task = input("\nEnter new task: ")

        tasks.append(task)

        print("\nTask Added Successfully")

    elif choice == "3":

        if len(tasks) == 0:

            print("\nNo tasks to remove")

        else:

            print("\nYour Tasks:")

            for i in range(len(tasks)):

                print(f"{i + 1}. {tasks[i]}")

            try:

                remove_task = int(input("\nEnter task number to remove: "))

                if remove_task > 0 and remove_task <= len(tasks):

                    removed = tasks.pop(remove_task - 1)

                    print(f"\n'{removed}' removed successfully")

                else:

                    print("\nInvalid task number")

            except:

                print("\nPlease enter a valid number")

    elif choice == "4":

        print("\nProgram Closed")

        break

    else:

        print("\nInvalid Choice")