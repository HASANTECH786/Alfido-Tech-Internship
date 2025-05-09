todo_list = []

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print("✅ Task added successfully.")

def view_tasks():
    if not todo_list:
        print("📭 No tasks in the list.")
        return
    print("\n📝 Your Tasks:")
    for i, task in enumerate(todo_list, start=1):
        print(f"{i}. {task}")

def remove_task():
    view_tasks()
    if not todo_list:
        return
    try:
        index = int(input("Enter the task number to remove: "))
        if 1 <= index <= len(todo_list):
            removed = todo_list.pop(index - 1)
            print(f"🗑️ Removed: {removed}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    while True:
        print("\n📋 To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("👋 Exiting. Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
