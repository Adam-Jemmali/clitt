import os
import sys
import json
from datetime import datetime
#read json file


{}

FICHER = 'data.json'

# [
#     {
#     "id": 1,
#     "description": "Description of Task 1",
#     "status": "todo",
#     "created_at": "2023-06-01T10:00:00",
#     "updatedat": "2023-06-01T10:00:00" 
#     },

#     {
#     "id": 2,
#     "description": "Description of Task 2",
#     "status": "in progress",
#     "created_at": "2023-06-02T11:00:00",
#     "updatedat": "2023-06-02T11:00:00"}
# ]


def load_tasks():
    if not os.path.exists(FICHER):
        return []
    with open(FICHER, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FICHER, 'w') as file:
        json.dump(tasks, file, indent=4) # python object to json object


#PYTHON OBJECT AFTER CONVERTING JSON TO PYTHON OBJECT
#[{'id': 1, 'title': 'Task 1', 'description': 'Description of Task 1', 'status': 'todo', 'created_at': '2023-06-01T10:00:00', 'updatedat': '2023-06-01T10:00:00'}, {'id': 2, 'title': 'Task 2', 'description': 'Description of Task 2', 'status': 'in progress', 'created_at': '2023-06-02T11:00:00', 'updatedat': '2023-06-02T11:00:00'}]

def get_next_id(tasks):
    
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def find_task_id(tasks,task_id):
    for t in tasks:
        if t['id'] == task_id:
            return t
    return None

#FIND  THE TIME FOR UPDATED AT AND CREATE AT TIMESTAMP
def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

####################### COMAND LISTS COMMAND
#clitt ADD "BUY GROCERIES"

#PYTHON task_cli.py add "Buy groceries" sys.argv = ["task_cli.py", "add", "Buy groceries"]

def cmd_add(args):
    if len(args)<1:
        print("Error: Missing task description.")
        return
    description = args[0]
    tasks = load_tasks() # load the tasks from the JSON  into python object
    next_id = get_next_id(tasks) # get the next id for the new task
    current_timestamp = get_current_timestamp() # get the current timestamp for created_at and updated_at

    new_task_add = {
        "id": next_id,
        "description": description,
        "status": "todo",
        "created_at": current_timestamp,
        "updated_at": current_timestamp
    }

    tasks.append(new_task_add)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {next_id})")#RETURNS INT DT

#task-cli UPDATE 1 "Buy groceries and cook dinner"

def cmd_update(args):
    if len(args) < 2:
        print("Error: Missing task ID or description.")
        return

    task_id = int(args[0]) #since the id IN CLI IS A STRING SO MUST BE CONVERTED TO INT

    new_description = args[1] # args[0]is the task ID and args[1] is the new description
    tasks = load_tasks() # load the tasks from the JSON file into a Python object

    task = find_task_id(tasks, task_id) # find the task with the given ID
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return
    task['description'] = new_description # update the task's description
    task['updated_at'] = get_current_timestamp() # update the task's updated_at timestamp
    save_tasks(tasks)
    print(f"Task with ID {task_id} updated successfully.")

#task-cli DELETE 1

def cmd_delete(args):
    if len(args) < 1:
        print("Error: Missing task ID.")
        return

    try:
        task_id = int(args[0]) # convert the task ID from string to int
    except ValueError:
        print("Error: Task ID in CLI must be an integer.")
        return
 
    tasks = load_tasks() # load the tasks from the JSON file into a Python object

    task = find_task_id(tasks, task_id) # find the task with the given ID
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    tasks.remove(task) # remove the task from the list

    save_tasks(tasks) # save the updated list back to the JSON file
    print(f"Task with ID {task_id} deleted successfully.")

def cmd_mark(args,new_status):
    if len(args) < 1:
        print("Error: Missing task ID.")
        return

    try:
        task_id = int(args[0]) # convert the task ID from string to int
    except ValueError:
        print("Error: Task ID in CLI must be an integer.")
        return

    tasks = load_tasks() # load the tasks from the JSON file into a Python object

    task = find_task_id(tasks, task_id) # find the task with the given ID
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    task['status'] = new_status # update the task's status
    task['updated_at'] = get_current_timestamp() # update the task's updated_at timestamp
    save_tasks(tasks) # save the updated list back to the JSON file
    print(f"Task with ID {task_id} marked as '{new_status}' successfully.")

def cmd_list(args):
#task-cli list
# Listing tasks by status
#task-cli list done

    tasks = load_tasks() # load the tasks from the JSON file into a Python object
    if len(args)==0:
        all_tasks=tasks # load the tasks from the JSON file into a Python object
    else:
        status_filter = args[0] # get the status filter from the command line arguments
        #example clitt.py list DONE

        valid_statuses = ['todo', 'in progress', 'done'] # define the valid statuses
        if status_filter not in valid_statuses:
            print(f"Error: Invalid status '{status_filter}'. Valid statuses are: {', '.join(valid_statuses)}.")
            return
        all_tasks = [task for task in tasks if task['status'] == status_filter] # filter the tasks by status


    

    if len(all_tasks) == 0:
        print("No tasks found.")
        return

    for task in all_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['created_at']}, Updated At: {task['updated_at']}")


def main():
    args = sys.argv[1:]  # Exclude the script name that is in args[0] from the arguments


    if len(args)==0:
            print("Commands: add, update, delete, mark-in-progress, mark-done, list")
            return
    command=args[0]
    rest_args=args[1:]

    if command=="add":
        cmd_add(rest_args)  

    elif command=="update":
        cmd_update(rest_args)
    elif command=="delete":
        cmd_delete(rest_args)
    elif command=="mark-in-progress":
        cmd_mark(rest_args,"in progress")
    elif command=="mark-done":
        cmd_mark(rest_args,"done")
    elif command=="list":
        cmd_list(rest_args)
    else:
        print(f"Error: Unknown command '{command}'. Valid commands are: add, update, delete, mark-in-progress, mark-done, list.")

if __name__ == "__main__":
    main()
