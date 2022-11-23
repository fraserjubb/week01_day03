tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
# As a user, to manage my task list I would like a program that allows me to:

# 1. Print a list of uncompleted tasks
def find_uncompleted_tasks():
    uncompleted_tasks = []
    for task in tasks:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
            
    return uncompleted_tasks
print(find_uncompleted_tasks())


# 2. Print a list of completed tasks
def find_completed_tasks():
    completed_tasks = []
    for task in tasks:
        if task["completed"] == True:
            completed_tasks.append(task)
            
    return completed_tasks
print(find_completed_tasks())

# 3. Print a list of all task descriptions
def find_all_task_descriptions():
    all_task_descriptions = []
    for task in tasks:
            all_task_descriptions.append(task['description'])
            
    return all_task_descriptions
print(find_all_task_descriptions())


# 4. Print a list of tasks where time_taken is at least a given time
def find_tasks_longer_than():
    tasks_longer_than = []
    user_time = input("Enter time taken for task")
    for task in tasks:
        if tasks["time_taken"] > user_time:
            tasks_longer_than.append(tasks["time_taken"])

    return tasks_longer_than
print(find_tasks_longer_than())

# 5. Print any task with a given description