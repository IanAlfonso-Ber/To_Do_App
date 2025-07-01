
"""FILENAME = "task.txt"

def load_task():
    try:
        with open(FILENAME, 'r') as file:
            for line in file:
                tasks.append(line.strip())
        print(f'Loaded{len(tasks)} tasks(s).')
    except FileNotFoundError:
        print('no saved task found. starting fresh.')"""
