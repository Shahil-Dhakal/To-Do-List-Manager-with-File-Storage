def displayMenu():
    print("\nYou can perform following operations: ")
    print("1.Add Task")
    print("2.View Task")
    print("3.Remove Task")
    print("4.Exit\n")   

def userInput():
    operation = int(input("Please choose an operation: "))
    return operation

task_list = []
def addTask():
    task = {}
    task_name = input("Enter the Task: ")
    task['name'] = task_name
    task['status'] = "incomplete"
    task_list.append(task)
    with open ("to-do.txt","a") as f:
        f.write(f"{task}\n")

def viewTask():
    with open ("to-do.txt","r") as f:
        data = f.read()
        print(data)

def deleteTask():
    with open ("to-do.txt","r") as f:
        lines = f.readlines()
        for index, line in enumerate(lines, start=1):
            print(index, line.strip()) #.strip() removes any extra spaces or newline characters.
    delete = int(input("Which of the following task do you want to delete?\n"))
    if delete < 1 or delete > len(lines):
        print("Error! Please input valid task number.")
    else:
        # task_list.pop(delete - 1)
        lines.pop(delete - 1)
        with open("to-do.txt","w") as f:
            for line in lines:
                f.write(line)

print("\nWelcome to the to-do app!!")
while True:
    displayMenu()
    operation = userInput()

    if operation == 4 :
        print("Thank You!!\n")
        break

    elif operation <=4 and operation >=1:
        if operation == 1:
            addTask()
        elif operation == 2:
            viewTask()
        elif operation == 3:
            deleteTask()

    else:
        print("Please enter valid input!!\n")
