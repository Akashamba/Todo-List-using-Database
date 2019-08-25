import PySimpleGUI as s
import back

task = back.readtask()
priority = back.readpriority()

layout = [
    [s.Text("Enter New Task to be added"), s.InputText("", key='data'), s.Button("ADD")],
    [s.Text("Priority Selector")],
    [s.Slider(orientation='horizontal', key='priority')],
    [s.Text("TO-DO List")],
    [s.Text("Tasks                                                                                       Priority")],
    [s.Listbox(task, size=(50, 10), key='tbox'), s.Listbox(priority, size=(10, 10), key='pbox')],
    [s.Button("DELETE"), s.Button("CLEAR LIST"), s.Button("EXIT")]
]

w = s.Window("To Do", layout)

while True:
    button, values = w.Read()
    w.FindElement('tbox').Update(task)
    w.FindElement('pbox').Update(priority)

    if button == "ADD":
        task = values['data']
        priority = values['priority']
        back.write(task, priority)
        task = back.readtask()
        priority = back.readpriority()
        w.FindElement('data').Update("")
        w.FindElement('tbox').Update(task)
        w.FindElement('pbox').Update(priority)

    if button == "CLEAR LIST":
        back.cleartable()
        task = back.readtask()
        priority = back.readpriority()
        w.FindElement('tbox').Update(task)
        w.FindElement('pbox').Update(priority)


    if button == "DELETE":
        x = values['tbox'][0]
        back.delete(x)
        task = back.readtask()
        priority = back.readpriority()
        w.FindElement('tbox').Update(task)
        w.FindElement('pbox').Update(priority)


    if button == "EXIT":
        break
