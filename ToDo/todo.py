import os

# Function to display the menu options
def display_menu():
    print("\nTo-Do List:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

# Function to view all tasks
def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks to show.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to add a new task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

# Function to remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("\nEnter the task number to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
