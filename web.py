import streamlit as sm
import functions
sm.title("My Todo app")
sm.subheader("This is my todo app")
sm.write("This is to increase my productivity of the day")

todos = functions.get_todos()
def add_todo():
    todo = sm.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)




for index , todo in enumerate(todos):
    checkbox =  sm.checkbox(todo , key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del sm.session_state[todo]
        sm.experimental_rerun()

sm.text_input(label="", placeholder="Add a new todo",on_change = add_todo,key = "new_todo")
print("Hello")
sm.session_state

