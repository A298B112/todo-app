import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Write a todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My to-do app",
                   layout=[[label], [input_box, add_button]],
                   icon="bot.ico",
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
