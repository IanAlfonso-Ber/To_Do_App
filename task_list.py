import json

# ------------------- TASK CLASS ---------------------------
class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def mark_completed(self):
        self.done = True

    def to_dict(self):
        return {'title': self.title, 'done': self.done}

    @staticmethod
    def from_dict(data):
        return Task(data['title'], data['done'])


# --------------------- TO DO LIST CLASS -------------------------
class ToDoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        self.save_tasks()
        print(f"task '{title}' added")

    def view_task(self):
        if not self.tasks:
            print("no tasks yet")
        else:
            print('\nyour tasks')
            for i, task in enumerate(self.tasks, start=1):
                status = '✓' if task.done else ''
                print(f'{i}. [{status}] {task.title}')


    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f'removed: {removed.title}')
        else:
            print('invalid index')


    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.save_tasks()
            print(f'marked as completed: {self.tasks[index].title}')
        else:
            print('invalid index.')


    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f)


    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
            self.tasks = [Task.from_dict(item) for item in data]
            print(f'Loaded {len(self.tasks)} task(s).')
        except FileNotFoundError:
            print('no saved tasks found. Starting Fresh.')


# ---------------------- MAIN PROGRAM -----------------------------

def show_menu():
    print('\nto-do list menu:')
    print('1. Add a task')
    print('2. View task')
    print('3. Remove a task')
    print('4. mark task as completed')
    print('5. Exit')


def main():
    todo = ToDoList()

    while True:
        show_menu()
        choice = input('choose an option (1-5)')

        if choice == '1':
            title = input('Enter task: ')
            todo.add_task(title)

        elif choice == '2':
            todo.view_task()

        elif choice == '3':
            todo.view_task()
            try:
                index = int(input('Enter task number to remove: ')) - 1
                todo.remove_task(index)
            except ValueError:
                print('please enter a valid number.')

        elif choice == '4':
            todo.view_task()
            try:
                index = int(input('Enter task number to mark as completed')) - 1
                todo.mark_completed(index)
            except ValueError:
                print('please Enter a Valid number.')

        elif choice == '5':
            print('goodbye')
            break

        else:
            print('invalid choice. try again.')

# ----------------------- Entry Point ----------------------------

if __name__ == '__main__':
    main()
















