from tkinter import *
from functools import partial
import tkinter.ttk as ttk
import keyboard
from TFT import store

picklist = []

tk = Tk()
tk.title('TFTVIK')
tk.geometry('220x220')
tk.resizable(False, False)

champion = open('Champion.txt', 'r', encoding='utf-8').readline()
champion = champion.split(',')

combo = ttk.Combobox(tk, values= champion, state="readonly")
combo.set("챔피언 선택")  
combo.grid(row=0, column=0)

lb = Listbox(tk)
lb.grid()

def start():
    keyboard.add_hotkey('d', store, args=(picklist,))
    keyboard.wait()

def buttonClick1():
    if combo.get() != "챔피언 선택" and combo.get() not in picklist:
        picklist.append(combo.get())
        lb.insert(END, combo.get())
        combo.set("챔피언 선택")

def buttonClick2():
    picklist.remove(picklist[lb.curselection()[0]])
    lb.delete(lb.curselection())

btn1 = Button(tk, text='+', width=5, command=buttonClick1)
btn1.grid(row=0, column=1)
btn2 = Button(tk, text='-', width=5, command=buttonClick2)
btn2.grid(row=1, column=1)

startBtn = Button(tk, text="Start", width= 10, command= start)
startBtn.grid()

tk.mainloop()