class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{idx}. {task.title} - {task.description} ({status})")

# Sample usage
if __name__ == "__main__":
    todo_list = ToDoList()

    task1 = Task("Complete Pixee Project", "Create a simple project for Pixee testing")
    task2 = Task("Learn Pixee Features", "Understand Pixeebot findings and how it works")

    todo_list.add_task(task1)
    todo_list.add_task(task2)

    todo_list.display_tasks()
