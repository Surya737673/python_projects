tasks = []

def show_menu():
    print("\nTo-Do List Menu")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark as complete")
    print("4. Remove a task")
    print("5. Exit")

def add_task():
    title = input("Enter a new title: ")
    tasks.append({"title": title, "completed": False})
    print("Task '{title}' added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{index}. [{status}] {task['title']}")

def mark_complete():
    view_tasks()
    if not tasks:
        return
    else:
        task_index = int(input("Enter the number of the task to mark as complete: "))
        if 1 <= task_index <= len(tasks):
            tasks[task_index - 1]["completed"] = True
            print(f"Task '{tasks[task_index - 1]['title']}' marked as complete.")
        else:
            print("Invalid task number. Please try again.")

def remove_task():
    view_tasks()
    if not tasks:
        return
    else:
        task_index = int(input("Enter the number of the task to remove: "))
        if 1 <= task_index <= len(tasks):
            removed_task = tasks.pop(task_index - 1)
            print(f"Task '{removed_task['title']}' removed successfully.")
        else:
            print("Invalid task number. Please try again.")

while True:
    show_menu()
    choice = input ("choose an option(1 - 5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")