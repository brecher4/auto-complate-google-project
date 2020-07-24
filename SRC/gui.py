from completion import get_list_completions
from data.init_data import init_meta_data
from tkinter import *


init_meta_data()
root = Tk() 
root.title('Auto Complete') 

menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About')


def get(): 
    input = entry.get()
    mylist.delete(0,END)
    dict_ = get_list_completions(input)
    i=1

    for sen in dict_:
        mylist.insert(END, f'{i}. {sen["sentence"]}')
        i+=1


entry = Entry(width=40)
button_search = Button(root, text='Search', width=5,command=get)
entry.grid(row=0, column=0) 
button_search.grid(row=0, column=1)
mylist = Listbox(root, width=40) 
mylist.grid(row=1,column=0)
root.mainloop()