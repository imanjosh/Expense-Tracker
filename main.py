import PySimpleGUI as sg
import json

sg.theme("Kayak")

layout = [
    [sg.Text('Simple Expense Tracker', font=("Times Roman", 25))],
    [sg.Text('Enter expense name:'), sg.InputText()],
    [sg.Text('Enter expense amount:'), sg.InputText()],
    [sg.Text('Select category:'), sg.Radio('Food', 'CATEGORY', default=True), sg.Radio('Transportation', 'CATEGORY'),
     sg.Radio('Entertainment', 'CATEGORY'), sg.Radio('Other', 'CATEGORY')],
    [sg.Button('Add Expense'), sg.Button('Clear Expenses'), sg.Button('Save Expenses'),
     sg.Button('Load Expenses'), sg.Button('Quit')],
    [sg.Text('Total expenses:'), sg.Text('', key='total')],
    [sg.Listbox(values=[], key='expenses', size=(40, 10))]
]

window = sg.Window('Simple Expense Tracker', layout, element_justification='c')

expenses = {}

while True:
    event, values = window.read()
    if event in (None, 'Quit'):
        break
    elif event == 'Add Expense':
        expenses[values[0]] = (values[1], values[2], values[3])
        total = sum(float(v[0]) for v in expenses.values())
        window['total'].update(total)
        window['expenses'].update(values=[f'{k}: {v[0]}' for k, v in expenses.items()])
    elif event == 'Clear Expenses':
        expenses.clear()
        window['total'].update(0)
        window['expenses'].update(values=[])
    elif event == 'Save Expenses':
        with open('expenses.json', 'w') as f:
            json.dump(expenses, f)
    elif event == 'Load Expenses':
        with open('expenses.json', 'r') as f:
            expenses = json.load(f)
        total = sum(float(v[0]) for v in expenses.values())
        window['total'].update(total)
        window['expenses'].update(values=[f'{k}: {v[0]}' for k, v in expenses.items()])

window.close()
