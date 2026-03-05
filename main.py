from planner import Planner
from datetime import datetime

planner = Planner()

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def main() -> None:
    while True:
        print("\n1. Add Tasks")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")
        
        choice = input("\nChoose option: ")
        
        if choice == "1":
            title = input("Title: ")
            
            while True:
                due = input("Due date (YYYY-MM-DD): ")
                if is_valid_date(due): break
                print("ERROR: Date is Invalid")
                
            while True:
                priority = input("Priority (low/medium/high): ")
                if priority in ["low", "medium", "high"]: break
                print("ERROR: Priority is Invalid")
                
            planner.add_task(title, due, priority)
        
        elif choice == "2":
            tasks = planner.list_tasks()
            for task in tasks:
                status = "✔" if task.completed else "✘"
                print(f"{task.id}. {task.title} ({task.due_date}) [{status}]")
        
        elif choice == "3":
            task_id = int(input("Task ID: "))
            planner.complete_task(task_id)

        elif choice == "4":
            break

if __name__ == "__main__":
    main()