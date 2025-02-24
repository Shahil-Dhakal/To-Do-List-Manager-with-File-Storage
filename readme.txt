INTRODUCTION:
    This project is basically, a small to-do manager, done in python using simple logic and python programming. User can add, delete, mark the tasks, etc. Its completely done using pure python without any framework, for the purpose of logic building.

    I will be using Incremental model to do this project. I will assume the time frame to be 1 week. Right now, I have no idea how much increment would it take but let's assume it would be completed after 7 increment. The last increment, obviously would be about testing and debugging the whole system, refining and improving by handling edge cases.

1st INCREMENT:
    In the first increment, I have made a menu where the action that the user can perform would be shown. I have used simple function to print all those menus and incase of wrong input by user, I have handled it by using else case and re-calling the function in else block for asking valid input to the user.

    A little update in the code is done to write a clear and good code. For example, displaying menu is inserted in a function and taking user input is also done through function. Used while loop to run the code untill the use chooses to exit.

2nd INCREMENT:
    "Add task" feature is added. Used Dictionaries inside list to store all those tasks.

3rd INCREMENT:
    "View Task" feature is added. Used simple logic to perform operation. Read the file data and printed it to implement this feature.

4th INCREMENT:
    "Remove Task" feature is added. Used "readlines()" function to read each line in the file and stored it in a variable. While printing each lines, Used "strip()" function that removes extra space at the end of each line in the file, to make the output user friendly. Used "pop()" function to remove the data and the new data after poping is added in the file with "w" methos.

5th INCREMENT:
    Refinement is done. There was a small un-noticed logical error in the program, causing false output and error. That was fixed. Still a lot of un-seen problem may arise. Which Will be further updated.

