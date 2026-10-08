import os

FILE_NAME = "tasks.txt"

def read_all_tasks():
    tasks = []
    if not os.path.exists(FILE_NAME):
        return tasks
    
    f= open(FILE_NAME, "r")
    for line in f: 
        line = line.strip()
        if line:
            tasks.append(line.split("|"))
    f.close()
    return tasks

def write_all_tasks(tasks_list):
    f = open(FILE_NAME, "w")
    for task in tasks_list:
        f.write(task[0] + "|" + task[1] + "\n")
    f.close()
    