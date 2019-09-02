import PySimpleGUI as s
import back

col = 'lavender'


def front():
    flayout = [
        [s.Text("To Do List", background_color=col)],
        #[s.Text("Press ENTER to continue", background_color=col)],
        #[s.Button("ENTER"), s.Button("EXIT")]

    ]

    w = s.Window("To Do List", flayout, size=(500, 100), element_justification='center', resizable=1,
                 background_color=col, auto_close=1, auto_close_duration=1)

    button, values = w.Read()

    if button == "ENTER":
        w.close()

    if button == "EXIT":
        exit()


task = back.readtask()
priority = back.readpriority()
completed = back.readcompleted()

layout = [
    [s.Text("Enter New Task to be added", background_color=col), s.InputText("", key='data')],
    [s.Text("Priority Selector", background_color=col),
     s.Slider(orientation='horizontal', key='priority', background_color=col, )],
    [s.Button("ADD NEW ITEM")],
    [s.Text("", background_color=col)],
    [s.Text("TO-DO List", background_color=col)],
    [s.Text("Tasks                                                                                       Priority",
            background_color=col)],
    [s.Listbox(task, size=(50, 10), key='tbox'), s.Listbox(priority, size=(10, 10), key='pbox')],
    [s.Button("COMPLETED"), s.Button("VIEW COMPLETED")],
    [s.Button("DELETE"), s.Button("CLEAR LIST"), s.Button("EXIT")]
]

w = s.Window("Main Page", layout, resizable=1, background_color=col)

front()

while True:
    button, values = w.Read()


    

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
        if task:
            back.cleartable()
            task = back.readtask()
            priority = back.readpriority()
            w.FindElement('tbox').Update(task)
            w.FindElement('pbox').Update(priority)

        else:
            s.Popup("You have no tasks", auto_close=1, auto_close_duration=3)
            continue

    if button == "DELETE":
        if task:
            x = values['tbox'][0]
            back.delete(x)
            task = back.readtask()
            priority = back.readpriority()
            w.FindElement('tbox').Update(task)
            w.FindElement('pbox').Update(priority)
        else:
            s.Popup("You have no tasks", auto_close=1, auto_close_duration=3)
            continue

    if button == "COMPLETED":
        if task:
            x = values['tbox'][0]
            back.complete(x)
            task = back.readtask()
            priority = back.readpriority()
            completed = back.readcompleted()
            w.FindElement('tbox').Update(task)
            w.FindElement('pbox').Update(priority)

        else:
            s.Popup("You have no tasks", auto_close=1, auto_close_duration=3)
            continue

    if button == "VIEW COMPLETED":
        layoutc = [
            [s.Text("Completed Tasks")],
            [s.Listbox(completed, key='comp', size=(50, 10))],
            [s.Button("REMOVE"), s.Button("REMOVE ALL"), s.Button("CLOSE")]
        ]

        c = s.Window("Completed", layoutc, resizable=1, background_color=col, force_toplevel=1)

        while True:
            events, values = c.Read()

            c.FindElement('comp').Update(completed)

            if events == "REMOVE":
                if completed:
                    d = values['comp'][0]
                    back.deletecompleted(d)
                    completed = back.readcompleted()
                    c.FindElement('comp').Update(completed)

                else:
                    s.Popup("You have no tasks", auto_close=1, auto_close_duration=3)
                    continue

            elif events == "REMOVE ALL":
                if completed:
                    back.deleteallcompleted()
                    completed = back.readcompleted()
                    c.FindElement('comp').Update(completed)
                else:
                    s.Popup("You have no tasks", auto_close_duration=3)
                    continue

            elif events == "CLOSE":
                c.close()
                break

            elif events is None:
                c.close()
                break

    if button is None or button == 'EXIT':
        w.close()
        break

w.close()
