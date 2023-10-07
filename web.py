import streamlit as st
import functions

todos = functions.get_todos()

st.title("To-Do app")
st.subheader("This is a todo app.")
st.write("This app is to increase your productivity.")

for i in todos:
    st.checkbox(i)

st.text_input("Enter a new todo:", placeholder="Write the new todo here")