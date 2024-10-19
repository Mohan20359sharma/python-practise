todo_list = []

def add_task(task):
    todo_list.append(task)

def view_tasks():
    for i, task in enumerate(todo_list,1):
        print(f"{i}.{task}")

def remove_task(index):
   if 0 < index <= len(todo_list):
       todo_list.pop(index-1)

add_task("Mohan")
add_task("rajat\n")
view_tasks()
remove_task(2)
view_tasks()