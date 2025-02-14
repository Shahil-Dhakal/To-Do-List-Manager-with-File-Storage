def displayMenu():
    print("You can perform following operations: ")
    print("1.Add Task")
    print("2.View Task")
    print("3.Remove Task")
    print("4.Mark Completed")
    print("5.Exit\n")   

def userInput():
    operation = int(input("Please choose an operation: "))
    return operation

print("\nWelcome to the to-do app!!")
while True:
    displayMenu()
    operation = userInput()

    if operation == 5 :
        print("Thank You!!\n")
        break

    elif operation <=4 and operation >=1:
        pass

    else:
        print("Please enter valid input!!\n")
