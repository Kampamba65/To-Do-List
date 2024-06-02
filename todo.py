import os

# File to store tasks
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file."""
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r") as file:
        tasks = [line.strip().split(";") for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(";".join(task) + "\n")

def add_task(tasks):
    """Add a new task."""
    description = input("Enter task description: ")
    tasks.append([description, "incomplete"])
    save_tasks(tasks)
    print("Task added.")

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks found.")
        return

    for index, (description, status) in enumerate(tasks):
        status_display = "✓" if status == "complete" else "✗"
        print(f"{index + 1}. {description} [{status_display}]")

def update_task(tasks):
    """Update task status."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to mark as complete: ")) - 1
        tasks[task_number][1] = "complete"
        save_tasks(tasks)
        print("Task updated.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task(tasks):
    """Delete a task."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to delete: ")) - 1
        tasks.pop(task_number)
        save_tasks(tasks)
        print("Task deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
