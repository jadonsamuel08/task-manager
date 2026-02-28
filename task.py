from datetime import datetime

class Task:
    def __init__(self, id, title, due_date, priority, completed=False):
        self.id = id
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.completed = completed
    
    def mark_completed(self):
        self.completed = True
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed,
        }
    
    @staticmethod
    def from_dict(data):
        return Task(
            data["id"],
            data["title"],
            data["due_date"],
            data["priority"],
            data["completed"]
        )