import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class Task:
    def __init__(self, description, priority=0):
        self.description = description
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        del self.tasks[index]

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task.description} (Priority: {task.priority})")

    def prioritize_task(self, index, priority):
        self.tasks[index].priority = priority

    def recommend_tasks(self, keyword):
        recommended_tasks = []
        for task in self.tasks:
            if keyword.lower() in task.description.lower():
                recommended_tasks.append(task)
        return recommended_tasks

def save_tasks_to_file(tasks):
    with open('tasks.csv', 'w', newline='') as csvfile:
        fieldnames = ['Description', 'Priority']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow({'Description': task.description, 'Priority': task.priority})

def load_tasks_from_file():
    tasks = []
    try:
        with open('tasks.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                task = Task(row['Description'], int(row['Priority']))
                tasks.append(task)
    except FileNotFoundError:
        pass
    return tasks

def main():
    task_manager = TaskManager()
    task_manager.tasks = load_tasks_from_file()

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Prioritize Task")
        print("5. Recommend Tasks")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            description = input("Enter task description: ")
            task = Task(description)
            task_manager.add_task(task)
            save_tasks_to_file(task_manager.tasks)
        elif choice == "2":
            task_manager.list_tasks()
            index = int(input("Enter index of task to remove: ")) - 1
            task_manager.remove_task(index)
            save_tasks_to_file(task_manager.tasks)
        elif choice == "3":
            task_manager.list_tasks()
        elif choice == "4":
            task_manager.list_tasks()
            index = int(input("Enter index of task to prioritize: ")) - 1
            priority = int(input("Enter priority level: "))
            task_manager.prioritize_task(index, priority)
            save_tasks_to_file(task_manager.tasks)
        elif choice == "5":
            keyword = input("Enter keyword for task recommendation: ")
            recommended_tasks = task_manager.recommend_tasks(keyword)
            if recommended_tasks:
                print("Recommended tasks:")
                for task in recommended_tasks:
                    print(task.description)
            else:
                print("No tasks found matching the keyword.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
