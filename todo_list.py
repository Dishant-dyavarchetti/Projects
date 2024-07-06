todo_list = []

def add_task(task):
    todo_list.append({"task": task, "done":False})
    print("task added successfully")

def mark_done(index):
    if 0 <= index < len(todo_list):
        todo_list[index]["done"] = True
        print("task marked as done successfully")
    else:
        print("Invalid index")

def del_task(index):
    if (0 <= index < len(todo_list)):
        todo_list.pop(index)
        print("Task deleted Successfully")
    else:
        print("Invalid index")

def show_task():
    for i, task in enumerate(todo_list):
        status = "done" if task["done"] else "not done"
        print(f"{i}. {task['task']} - {status}")



def main():
    while True:
        print("1)Add the task")
        print("2)delete the task")
        print("3)marked as done")
        print("4)Show Tasks")
        print("5)Exit")
        option = int(input("Enter the option: "))
        if (option == 1):
            task = str(input("Enter the task: "))
            add_task(task)
        elif (option == 3):
            index = int(input("Enter the index of the task you want to mark as done: "))
            mark_done(index)
        elif(option == 2):
            index = int(input("enter the index of the task you want to delete: "))
            del_task(index)
        elif(option == 4):
            show_task()
        elif(option == 5):
            break
        else:
            print("Invalid option entered")

if __name__ == "__main__":
    main()
