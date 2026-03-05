import json
from task import Task

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read().strip()
            if not content:
                return []
            data = json.loads(content)
            return [Task.from_dict(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)