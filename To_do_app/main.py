
import user_options as uo


def main():
    while True:
        print("\n===== TODO APPLICATION =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        operations = {
            "1": uo.add_task,
            "2": uo.view_tasks,
            "3": uo.update_task,
            "4": uo.complete_task,
            "5": uo.delete_task
        }

        if choice == "6":
            print("Exiting ToDo Application...")
            break

        operation = operations.get(choice)

        if operation:
            operation()
        else:
            print("Invalid choice. Please select 1 to 6.")


if __name__ == "__main__":
    main()
