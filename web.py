import streamlit as st
import fun

todos=fun.get_todos()

def add_todo():
   todo= st.session_state["new_todo"]+"\n"
   todos.append(todo)
   fun.write_todos(todos)


st.title("MY TO-DO WEB APP")
st.subheader("This App Will Increase your Productivity :) ")
st.write("Enter your To-Do")



for index, todo in enumerate(todos):
   checkbox=st.checkbox(todo,key=todo)
   if checkbox:
      todos.pop(index)
      fun.write_todos(todos)
      del st.session_state[todo]
      st.experimental_rerun()

st.text_input(label=" ", placeholder="Add new To-do", on_change=add_todo, key='new_todo')

