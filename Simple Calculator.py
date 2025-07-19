import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task['done'] else "✗"
        print(f"{i}. [{status}] {task['task']}")

def add_task(tasks):
    new_task = input("Enter a new task: ")
    tasks.append({"task": new_task, "done": False})
    print("Task added.")

def mark_completed(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        tasks[index]["done"] = True
        print("Task marked as completed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task(tasks):
=

