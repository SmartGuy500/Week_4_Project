
import streamlit as st

import database

database.create_table()

tasks= database.get_tasks()

def describe(tasks): 
    return f"#{tasks["id"]} - {tasks["title"]}"

class Task:
    def __init__(self, id, title, description, due_date, completed): 
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = bool(completed)





