import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("To-Do app")
st.subheader("This is a todo app.")
st.write("This app is to increase your productivity.")

for i, t in enumerate(todos):
    checkbox = st.checkbox(t, key=t)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[t]
        st.experimental_rerun()

st.text_input("Enter a new todo:", placeholder="Write the new todo here",
              on_change=add_todo, key="new_todo")

st.session_state