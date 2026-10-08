import task_manager
import validator
while True:
    print("\n1. View\n2. Add\n3. Complete\n4. Delete\n5. Quit")
    pick = input("Option: ").strip()
    if pick == "1":
        tasks = task_manager.get_tasks()
        if not tasks:
            print("Empty!")
        for i, t in enumerate(tasks, 1):
            box = "[X]" if t[0] == "done" else "[ ]"
            print(f"{i}. {box} {t[1]}")
    elif pick == "2":
        txt = input("Task title: ")
        val = validator.check_text(txt)
        if not val:
            print("Cannot be blank!")
        else:
            task_manager.create_task(val)
    elif pick == "3":
        tasks = task_manager.get_tasks()
        idx = validator.check_number(input("Task number:"), len(tasks))
        if idx is False:
            print("Invalid!")
        else:
            task_manager.finish_task(idx)
    elif pick == "4":
        tasks = task_manager.get_tasks()
        idx = validator.check_number(input("Task number; "), len(tasks))
        if idx is False:
            print("Invalid!")
        else:
            task_manager.remove_task(idx)
    elif pick == "5":
        print("Goodbye!")
        break
    