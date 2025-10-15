class Task:
    def __init__( self, priority, title, description ):
        self.priority = priority
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed( self ):
        self.completed = True

    def edit_description( self, new_priority, new_description ):
        self.priority = new_priority
        self.description = new_description

    def __str__( self ):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.priority}: {self.title} - {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, priority, title, description):
        task = Task(priority,title, description)
        self.tasks.append(task)
        print(f"Successfully added Task {title} - {description}")

    def edit_task( self, task_index, new_priority, new_description ):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].edit_description( new_priority, new_description )
            print( f"Task {task_index + 1} updated." )
        else:
            print("Invalid task index.")

    def mark_task_completed( self, task_index ):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
            print(f"Task {task_index + 1} marked as completed.")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")


def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input( "Enter your choice: " )

        if choice == "1":
            priority=input( "Enter priority of task: " )
            title=input( "Enter the task title: " )
            description = input("Enter task description: ")
            todo_list.add_task( priority, title, description )
        elif choice == "2":
            task_index = int( input( "Enter task number to edit: " )) - 1
            new_priority =input( "Enter new priority: " )
            new_description = input( "Enter new description: " )
            todo_list.edit_task( task_index, new_priority, new_description )
        elif choice == "3":
            task_index = int( input( "Enter task number to mark as completed: " )) - 1
            todo_list.mark_task_completed( task_index )
        elif choice == "4":
            todo_list.view_tasks()
        elif choice == "5":
            print( "Exiting the application. Goodbye!" )
            break
        else:
            print( "Invalid choice. Please try again." )


if __name__ == "__main__":
    main()

