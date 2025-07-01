import json
FILENAME = "tasks.txt"
tasks = []

class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = True
    
    def mark_completed(self):
        self.done = True
        
    def to_dict(self):
        return {'title': self.title, 'done': self.done}
        
    @staticmethod
    def from_dict(data):
        return Task(data['title'], data['done'])
        









def load_tasks():
    try:
        with open(FILENAME, 'r') as file:
           loaded = json.load(file)
            for task in loaded:
                if 'tittle' in task and 'done' in task:
                    tasks.append(task)
        print(f'Loaded{len(tasks)} tasks(s).')
    except FileNotFoundError:
       print('no saved task found. starting fresh.')


def save_task():
    with open(FILENAME, 'w') as file:
        json.dump(tasks, file)

def show_menu():
    print('\nto-do list menu:')
    print('1. Add a task')
    print('2. View tasks')
    print('3. Remove a task')
    print('4. mark task as completed')
    print('5. Exit')


def add_task():
    title = input('enter a new task: ')
    task = {'tittle': title, 'done': False}
    tasks.append(task)
    save_task()
    print("task added")

def view_task():
    if not tasks:
        print("no tasks yet")
    else:
        print('\nyour tasks')
        for i, task in enumerate(tasks, start=1):
            status = '✓' if task ['done'] else ''
            print(f'{i}. [{status}] {task['title']}')

def mark_completed():
    view_task()
    if not tasks:
        return
    try:
        num = int(input('enter the task number to mark as completed: '))
        if 1 <= num <= len(tasks):
            tasks[num - 1]['done'] = True
            save_task()
            print(f"task '{tasks[num - 1]['title']}' marked as completed ")
        else:
            print('Invalid task number.')
    except ValueError:
        print("please enter a valid number.")


def remove_task():
    view_task()
    if not tasks:
        return
    try:
        num = int(input('Enter the task number to remove: '))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_task()
            print(f"Removed task: '{removed}'")
        else:
            print("Invalid task number")
    except ValueError:
        print('please enter a valid number')







load_tasks()

#main loop
while True:
    show_menu()
    choice = input('choose an option (1-3): ')

    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        mark_completed()
    elif choice == '5':
        print('Goodbye')
        break
    else:
        print('invalid choice try again')





