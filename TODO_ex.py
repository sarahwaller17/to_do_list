import logging
import argparse

parser = argparse.ArgumentParser()

# add arguments?




logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('todo.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

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
            print("Invalid task index")

def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            tasks = todo.view_tasks()
            if not tasks:
                print("No tasks in the list.")
            else:
                for i, task in enumerate(tasks):
                    print(f"{i}. {task}")
        elif choice == '2':
            task = input("Enter the task: ")
            todo.add_task(task)
            print("Task added.")
        elif choice == '3':
            index = int(input("Enter the index of the task to mark as done: "))
            todo.mark_task_done(index)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
