import sqlite3
import pandas as pd 
DB_FILE = "task_manager.db"
print("OK")

def create_table(): 
    connection= sqlite3.connect(DB_FILE)
    cursor= connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        task_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title TEXT, 
        description TEXT, 
        due_date TEXT NOT NULL, 
        completed BOOL FALSE
        )
    """)
    connection.commit()
    connection.close()

def add_task(title, description, due_date, completed): 
    connection= sqlite3.connect(DB_FILE)
    cursor= connection.cursor()
    cursor.execute("INSERT INTO tasks (title, description, due_date, completed) VALUES (?, ?, ?, ?)", (title, description, due_date, completed))
    connection.commit()
    connection.close()

def get_tasks(title, description, due_date, completed): 
    connection= sqlite3.connect(DB_FILE)
    cursor= connection.cursor()
    cursor.execute("SELECT task_id, title, description, due_date, completed FROM tasks")
    rows= cursor.fetchall()
    connection.close()

    task_list= []
    for row in rows: 
        task_list.append({"task_id": row[0], "title": row[1], "description": row[2], "due_date":row[3], "completed": row[4]})
    return task_list

def update_tasks(task_id, title, description, due_date, completed): 
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE tasks SET title = ?, description = ?, due_date = ?, completed= ? WHERE id = ? (?, ?, ?, ?)", (title, description, due_date, completed, task_id)
    )
    connection.commit()
    connection.close()


def delete_tasks(task_id): 
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM tasks WHERE task_id= ?", (task_id)
    )
    connection.commit()
    connection.close()









print("Done")
