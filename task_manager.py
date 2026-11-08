
import streamlit as st

import database

st.set_page_config(page_title= "Task Manager", page_icon= "👨🏢")


database.create_table()

st.title(" Task Manager 👨🏢")
st.caption("A basic Task Management program")

if "message" in st.session_state: 
    st.success(st.session_state.pop("message"))

tasks = database.get_tasks()

def describe(task): 
    return f"#{task["task_id"]} - {task["title"]}"

tab_view, tab_add, tab_update, tab_delete = st.tabs(["View", "Add", "Update", "Delete"])

with tab_view: 
    st.subheader("All Tasks")
    if tasks: 
        st.tasks(tasks, hide_index= True)
        st.write(f"Total: {len(tasks)} task(s)")
    else: 
        st.info("No tasks yet. Add one in the **Add** tab")


with tab_add: 
    st.subheader("Add a task")
    with st.form("add_form", clear_on_submit= True): 
        title= st.text_input("Title: ")
        description= st.text_input("Short Description: ")
        due_date= st.text_input("Due Date: ", placeholder= "e.g In an hour")
        completed=st.checkbox("Completed: ")
        submitted= st.form_submit_button("Add task")

    if submitted: 
        if due_date.strip == "":
            st.error("Please enter a due date")
        else: 
            database.add_task(title.strip(), description.strip(), due_date.strip())
            st.session_state["message"]= f"Added {title.strip()} successfully"
            st.rerun()


with tab_update: 
    st.subheader("Update a task")
    if tasks: 
        task= st.selectbox("Choose a task: ", tasks, format_func= describe, key= "update_choice")

        new_title= st.text_input("Title ", value=task["title"], key= f"title_{task["task_id"]}")
        new_desc= st.text_input("Description ", value=task["description"], key= f"description_{task["description"]}")
        new_due_date= st.text_input("Due Date ", value=task["due_date"] or "", key=f"due_date_{task["due_date"]}")

        if st.button("Save changes"):
            if new_due_date.strip == "": 
                st.error("Due date can't be empty")
            else: 
                database.update_task(task["task_id", new_title.strip(), new_desc.strip(), new_due_date.strip()])
                st.session_state["message"]= f"Updated {due_date.strip()} successfully"
                st.rerun()
    else: 
        st.info("There is no tasks to update")

with tab_delete: 
    st.subheader("Delete a task")
    if completed == True: 
        del task["task_id"]
    else: 
        st.info("There is no tasks to delete")









