"""
A simple to_do application that allows users to add tasks, view them, and mark them as done.
This application is designed to be run in a terminal or command line interface.
"""

"""
A simple to_do application that allows users to add tasks, view them, and mark them as done.
This application is designed to be run in a terminal or command line interface.
"""
class ToDoList:
    """
    A class to represent a to-do list.
    
    Attributes:
        tasks (list): A list to store tasks.
    """

    def __init__(self):
        """Initializes the ToDoList with an empty task list."""
        self.tasks = []

    def add_task(self, task: str) -> None:
        """Adds a task to the to-do list."""
        self.tasks.append(task)

    def view_tasks(self) -> list:
        """Returns the list of tasks."""
        return self.tasks

    def mark_task_done(self, task_index: int) -> None:
        """Marks a task as done by removing it from the list."""
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
        else:
            raise IndexError("Task index out of range.")




# class ToDoList:

#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task: str) -> None:
#         """Adds a task to the to-do list."""
#         self.tasks.append(task)

#     def view_tasks(self) -> list:
#         """Returns the list of tasks."""
#         return self.tasks

#     def mark_task_done(self, task_index: int) -> None:
#         """Marks a task as 1done by removing it from the list."""
#         if 0 <= task_index < len(self.tasks):
#             self.tasks.pop(task_index)
#         else:
#             raise IndexError("Task index out of range.")

#todo = ToDoList()

# def to_do_example(list_of_commands: list) -> None:
#     """
#     A to do application that captures tasks and allows them to be marked off. 
#     Args:
#         list_of_commands (list, optional): A list of commands to be executed in sequential order. 
#     Returns:
#         None
#     """
#     listo: list = []
#     for command_1 in list_of_commands:
#         print("1. Add Task")
#         print("2. View Tasks")
#         print("3. Mark Task as Done")
#         print("4. Exit")
#         print("="*50)
#         command_1 = input("Enter your choice:")
#         if command_1 == '1':
#             tsk = input("Enter task:")
#             listo.append(tsk)
#             print("-"*50)
#         elif command_1 == '2':
#             print("Tasks:")
#             for i, t in enumerate(listo):
#                 print(f"{i+1}. {t}")
#             print("-"*50)
#         elif command_1 == '3':
#             usr_input = input("Enter task number to mark as done:")
#             if 0 <=  int(usr_input) - 1 < len(listo):
#                 listo.pop(int(usr_input) - 1)
#                 print("Task marked as done.")
#             else:
#                 print("Invalid task number.")
#         elif command_1 == '4':
#             print("Exiting.")
#             print("-"*50)
#             break
#         else:
#             print("Invalid choice.")
#             print("-"*50)
#     return listo

# to_do_example(["1", "2", "3", "4", "5"])  


def to_do_example(list_of_commands: list=[]) -> None:
    """
    A to do application that captures tasks and allows them to be marked off. 
    
    Args:
        list_of_commands (list, optional): A list of commands to be executed in sequential order. 
        
    Returns:
        None
    """

    listo: list = []
    for command_1 in list_of_commands:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        print("="*50)
        command_1 = input("Enter your choice: ")
        if command_1 == '1':
            tsk = input("Enter task: ")
            listo.append(tsk)
            print("-"*50)
        elif command_1 == '2':
            print("Tasks:")
            for i, t in enumerate(listo):
                print(f"{i+1}. {t}")
            print("-"*50)
        elif command_1 == '3':
            usr_input = input("Enter task number to mark as done: ")
            if 0 <=  int(usr_input) - 1 < len(listo): 
                listo.pop(int(usr_input) - 1)
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        elif command_1 == '4':
            print("Exiting.")
            print("-"*50)
            break
        else:
            print("Invalid choice.")
            print("-"*50)

    return listo
