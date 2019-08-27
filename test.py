import PySimpleGUI as s
import back

task = back.readtask()
priority = back.readpriority()
completed = back.readcompleted()

layout = [
    [s.Text("Enter New Task to be added"), s.InputText("", key='data')],
    [s.Text("Priority Selector"), s.Slider(orientation='horizontal', key='priority')],
    [s.Button("ADD NEW ITEM")],
    [s.Text("")],
    [s.Text("TO-DO List")],
    [s.Text("Tasks                                                                                       Priority")],
    [s.Listbox(task, size=(50, 10), key='tbox'), s.Listbox(priority, size=(10, 10), key='pbox')],
    [s.Button("COMPLETED"), s.Button("VIEW COMPLETED")],
    [s.Button("DELETE"), s.Button("CLEAR LIST"), s.Button("EXIT")]
]

w = s.Window("To Do", layout)

while True:
    button, values = w.Read()
    w.FindElement('tbox').Update(task)
    w.FindElement('pbox').Update(priority)

    if button == "ADD NEW ITEM":
        task = values['data'].capitalize()
        priority = values['priority']

        if task != "":
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

    if button == "COMPLETED":
        x = values['tbox'][0]
        back.complete(x)
        task = back.readtask()
        priority = back.readpriority()
        completed = back.readcompleted()
        w.FindElement('tbox').Update(task)
        w.FindElement('pbox').Update(priority)

    if button == "VIEW COMPLETED":
        layoutc = [
            [s.Text("Completed Tasks")],
            [s.Listbox(completed, key='comp', size=(50, 10))],
            [s.Button("REMOVE"), s.Button("CLOSE")]
        ]

        c = s.Window("Completed", layoutc)

        while True:
            events, values = c.Read()

            c.FindElement('comp').Update(completed)

            if events == "REMOVE":
                d = values['comp'][0]
                back.deletecompleted(d)
                completed = back.readcompleted()
                c.FindElement('comp').Update(completed)

            elif events == "CLOSE":
                c.close()
                break

    if button == "EXIT":
        break
