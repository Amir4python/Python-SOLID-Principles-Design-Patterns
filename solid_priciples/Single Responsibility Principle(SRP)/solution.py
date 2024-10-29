class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

class TaskDisplay:
    @staticmethod
    def display_tasks(tasks):
        for task in tasks:
            print(task)

class TaskInput:
    @staticmethod
    def input_task():
        task = input("Enter task: ")
        TaskManager.add_task(task=task)

    @staticmethod
    def remove_task():
        task = input("Enter task to remove: ")
        TaskManager.delete_task(task)


if __name__ == "__main__":



    todo = TaskManager()
    todo.add_task('gym')
    todo.add_task('cook')
    todo.add_task('dance')


    todo.add_task('pray')

    TaskDisplay.display_tasks(todo.tasks)
    print('-----------------')
    todo.delete_task('dance')
    TaskDisplay.display_tasks(todo.tasks)
