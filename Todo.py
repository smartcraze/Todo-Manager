import sqlite3

conn = sqlite3.connect("Todo.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Todo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    todo_text TEXT,
                    done INTEGER DEFAULT 0)''')
conn.commit()


def add_todo():
    todo_text = input("Enter the todo: ")
    cursor.execute("INSERT INTO Todo (todo_text, done) VALUES (?, ?)", (todo_text, 0))
    conn.commit() 
    print("Todo added successfully.")

def update_todo():
    try:
        todo_id = int(input("Enter the ID of the Todo to update: "))
        new_text = input("Enter the new text: ")
        cursor.execute("UPDATE Todo SET todo_text = ? WHERE id = ?", (new_text, todo_id))
        conn.commit()
        print("Todo updated successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid todo ID.")
def remove_todo():
    try:
        todo_id = int(input("Enter the ID of the todo to remove: "))
        cursor.execute("DELETE FROM Todo WHERE id = ?", (todo_id,))
        conn.commit()
        print("Todo removed successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid todo ID.")
def mark_as_done():
    try:
        todo_id = int(input("Enter the ID of the todo to mark as done: "))
        cursor.execute("UPDATE Todo SET done = 1 WHERE id = ?", (todo_id,))
        conn.commit()
        print("Todo marked as done.")
    except ValueError:
        print("Invalid input. Please enter a valid todo ID.")
def view_all_todo():
    cursor.execute("SELECT * FROM Todo")
    todo = cursor.fetchall()
    if todo:
        print("ID\tTodo\t\tDone")
        print("-" * 30)
        for todo in todo:
            print(f"{todo[0]}\t{todo[1]}\t\t{'Yes' if todo[2] else 'No'}")
    else:
        print("No todo found.")

# Main function
def main():
    try:
        while True:
            print("1. Add Todo")
            print("2. Update Todo")
            print("3. Remove Todo")
            print("4. Mark as Done")
            print("5. View All Todo")
            print("6. Exit")
            choice = input("Enter Your Choice: ")
            if choice == "1":
                add_todo()
            elif choice == "2":
                update_todo()
            elif choice == "3":
                remove_todo()
            elif choice == "4":
                mark_as_done()
            elif choice == "5":
                view_all_todo()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please select a number from 1 to 6.")
    finally:
        conn.close()
if __name__ == "__main__":
    main()
