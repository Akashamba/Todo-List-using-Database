import PySimpleGUI as s
import back

lst=[]
lst=back.readall()

layout=[
    [s.Text("Enter New Task to be added"),s.InputText("",key='data'),s.Button("ADD")],
    [s.Slider(orientation='horizontal',key='priority')],
    [s.Text("TO-DO List")],
    [s.Listbox(lst,size=(50,10),key='box')],
    [s.Button("CLEAR"),s.Button("CLEAR LIST"),s.Button("EXIT")]
]

w=s.Window("To Do",layout)

while True:
    button,values=w.Read()
    w.FindElement('box').Update(lst)


    if button=="ADD":
        task=values['data']
        priority=values['priority']
        back.write(task,priority)
        lst=back.readall()
        w.FindElement('data').Update("")
        w.FindElement('box').Update(lst)


    if button=="EXIT":
        break
