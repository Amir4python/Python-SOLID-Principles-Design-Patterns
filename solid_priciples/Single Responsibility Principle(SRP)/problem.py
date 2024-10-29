class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

    def display_tasks(self):
        for task in self.tasks:
            print(task)

    def input_task(self):
        task = input("Enter task: ")
        self.add_task(task)

    def remove_task(self):
        task = input("Enter task to remove: ")
        self.delete_task(task)


if __name__ == "__main__":
    todo = TodoList()
    todo.add_task('gym')
    todo.add_task('cook')
    todo.add_task('dance')


    todo.add_task('pray')
    todo.display_tasks()
    print('-----------------')
    todo.delete_task('dance')
    todo.display_tasks()
