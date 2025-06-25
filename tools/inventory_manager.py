''' a json file will be created automatically while execuation
the same file will be used again if it is present in the same folder '''
import json
import tkinter as tk

try:
    with open('data.json', 'r') as file:
        inv = json.load(file)
except:
    inv = dict()

''' everytime the function is called, the label is removed, and the whole dictionary
is printed again, to avoid overlapping '''
def add_input():
    try:
        destroy_label()
    except:
        pass
    item=item_input.get()
    item=item.capitalize()
    number=number_input.get()
    inv[item]=inv.get(item,0)+int(number)
    txt=''
    for k,v in inv.items():
        txt = txt + k + ' : ' + str(v) + '\n'
    global show_label
    show_label = tk.Label(root, text = txt)
    show_label.grid(row=2, column=0)

def show():
    txt=''
    for k,v in inv.items():
        txt = txt + k + ' : ' + str(v) + '\n'
    global show_label
    show_label = tk.Label(root, text = txt)
    show_label.grid(row=2, column=0)

def clear():
    global inv
    inv = dict()
    show_label.destroy()

def destroy_label():
    show_label.destroy()

def close():
    root.destroy()

#creating display window
root=tk.Tk()
root.title('Inventory manager')
root.geometry('600x600')


#creating buttons
show_button = tk.Button(root, text='Refresh', command=show)
show_button.grid(row=0, column=0)
input_button = tk.Button(root, text = 'Add item', command= add_input)
input_button.grid(row=1, column=4)
clear_button = tk.Button(root, text = 'Clear List', command=clear)
clear_button.grid(row = 0, column = 1)
close_button = tk.Button(root, text = 'Close', command = close)
close_button.grid(row = 0, column = 2)

#creating input
item_input=tk.Entry(root)
item_input.grid(row=1, column=1)
item_label=tk.Label(root, text='item:')
item_label.grid(row =1, column= 0)

number_input=tk.Entry(root)
number_input.grid(row=1, column= 3)
number_label=tk.Label(root, text= '  number:')
number_label.grid(row= 1,  column= 2)

root.mainloop()

with open('data.json', 'w') as file:
    json.dump(inv, file)

#make a function for output
#last commit was save in to and load out of a file