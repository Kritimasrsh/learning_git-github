# Simple To-Do List Program

to_do_list = []

def show_tasks():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(to_do_list, 1):
            print(f"{i}. {task}")

def add_task(task):
    to_do_list.append(task)
    print(f'Added task: "{task}"')

def remove_task(task_number):
    if 0 < task_number <= len(to_do_list):
        removed = to_do_list.pop(task_number - 1)
        print(f'Removed task: "{removed}"')
    else:
        print("Invalid task number.")

# Example usage:
add_task("Finish Git tutorial")
add_task("Write Python program")
show_tasks()
remove_task(1)
show_tasks()