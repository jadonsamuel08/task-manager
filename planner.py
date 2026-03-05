from task import Task
from storage import load_tasks, save_tasks

class Planner:
    def __init__(self):
        self.tasks = load_tasks()
    
    def add_task(self, title, due_date, priority):
        new_id = len(self.tasks) + 1
        task_inst = Task(new_id, title, due_date, priority)
        self.tasks.append(task_inst)
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_completed()
                break
        save_tasks(self.tasks)
    
    def list_tasks(self):
        return self.tasks