import file_storage
def create_task(title):
    all_tasks = file_storage.read_all_tasks()
    all_tasks.append(["pending", title])
    file_storage.write_all_tasks(all_tasks)
def get_tasks():
    return file_storage.read_all_tasks()
def finish_tasks(index):
    all_tasks = file_storage.read-all_tasks()
    all_tasks[index] = ["done", all_tasks[index][1]]
    file_storage.write_all_tasks(all_tasks)
def remove_task(index):
    all_tasks = file_storage.read_all_tasks()
    all_tasks.pop(index)
    file_storage.write_all_tasks(all_tasks)
