
tasks = []
next_id = 1


def add_task():
    global next_id

    task_name = input("Enter task: ").strip()

    if task_name == "":
        print("Task cannot be empty!")
        return

    task = {
        "id": next_id,
        "name": task_name,
        "status": "Pending"
    }

    tasks.append(task)
    print("Task added successfully!")

    next_id += 1


def view_tasks():
    if len(tasks) == 0:
        print("No tasks found!")
        return

    print("\n----- TASK LIST -----")

    for task in tasks:
        print(
            f"ID: {task['id']} | "
            f"Task: {task['name']} | "
            f"Status: {task['status']}"
        )


def find_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


def update_task():
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Enter a valid numeric ID!")
        return

    task = find_task(task_id)

    if task:
        new_name = input("Enter new task: ").strip()

        if new_name:
            task["name"] = new_name
            print("Task updated successfully!")
        else:
            print("Task cannot be empty!")
    else:
        print("Task not found!")


def complete_task():
    try:
        task_id = int(input("Enter task ID to complete: "))
    except ValueError:
        print("Enter a valid numeric ID!")
        return

    task = find_task(task_id)

    if task:
        task["status"] = "Completed"
        print("Task completed successfully!")
    else:
        print("Task not found!")


def delete_task():
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Enter a valid numeric ID!")
        return

    task = find_task(task_id)

    if task:
        tasks.remove(task)
        print("Task deleted successfully!")
    else:
        print("Task not found!")
