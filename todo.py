from datetime import datetime


tasks = []


try:
    with open("task.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    pass


def save_tasks():
    with open("task.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Mark Done")
    print("5. Exit")


    choice = input("Enter choice: ")


    if choice == "1":
        task = input("Enter Task: ")
        time = datetime.now().strftime("%Y-%m-%d %H:%M")
        full_task = "[ ] " + task + " | " + time
        tasks.append(full_task)
        save_tasks()



    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")



    elif choice == "3":
        try:
            num = int(input("Enter task number: "))
            if 0 < num <= len(tasks):
                tasks.pop(num - 1)
                save_tasks()
            else:
                print("Invalid")
        except ValueError:
            print("Enter a valid number")



    elif choice == "4":
        try:
            num = int(input("Enter task number: "))
            if 0 < num <= len(tasks):
                if "[DONE]" in tasks[num-1]:
                    print("Already done")
                else:
                    tasks[num-1] = tasks[num-1].replace("[ ]", "[DONE]")
                    save_tasks()
            else:
                print("Invalid")
        except ValueError:
            print("Enter a valid number")



    elif choice == "5":
        print("Tasks Saved. Exiting...")
        break



    else:
        print("Invalid choice")