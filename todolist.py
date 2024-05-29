class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def mark_completed(self, index):
        self.tasks[index - 1] = f"[DONE] {self.tasks[index - 1]}"

    def delete_task(self, index):
        del self.tasks[index - 1]

def main():
    todo_list = TodoList()

    while True:
        print("\n===== Todo List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            print("\n===== Tasks =====")
            todo_list.view_tasks()
        elif choice == "3":
            index = int(input("Enter task number to mark as completed: "))
            todo_list.mark_completed(index)
        elif choice == "4":
            index = int(input("Enter task number to delete: "))
            todo_list.delete_task(index)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
