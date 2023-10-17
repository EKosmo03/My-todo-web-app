import streamlit as st
import functions

todos = functions.get_todos('todos.txt')

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos, 'todos.txt')


st.title('My Todos')
st.subheader("Web App")
st.write('This app is used to make a list of things to do.')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos, 'todos.txt')
        del st.session_state[todo]
        st.experimental_rerun()

# label is a required value left it blank here
st.text_input(label='h', placeholder='Add a new todo...',
              on_change=add_todo, key="new_todo", label_visibility='hidden')