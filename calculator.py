# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 13:01:45 2024

@author: Madhumitha
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("330x535")
root.title("CALCULATOR")

def print_text(text):
    txt.insert(tk.END, text)
def evaluate():
    result = eval(txt.get())
    txt.delete(0, tk.END)
    txt.insert(tk.END, result)
def clear():
    txt.delete(0, tk.END)
def erase():
    result= txt.get()
    txt.delete(0, tk.END)
    txt.insert(tk.END, result[:-1])

txt = tk.Entry(root, width=35,font=("Arial Black",10))
txt.grid(column=0, row=0, columnspan=5)

btn1 = tk.Button(root, text="C", width=8, height=5, bg='orange',font=("Arial Black",10), command=clear)
btn1.grid(column=0, row=1)
btn2 = tk.Button(root, text="←", width=8, height=5, bg='orange',font=("Arial Black",10), command=erase)
btn2.grid(column=1, row=1)
btn3 = tk.Button(root, text="%", width=8, height=5, bg='orange',font=("Arial Black",10),command=lambda: print_text("%"))
btn3.grid(column=2, row=1)
btn4 = tk.Button(root, text="/", width=8, height=5, bg='orange',font=("Arial Black",10), command=lambda: print_text("/"))
btn4.grid(column=3, row=1)

btn1 = tk.Button(root, text="7", width=8, height=5, bg='blue', font=("Arial Black",10),command=lambda: print_text("7"))
btn1.grid(column=0, row=2)
btn2 = tk.Button(root, text="8", width=8, height=5, bg='blue', font=("Arial Black",10),command=lambda: print_text("8"))
btn2.grid(column=1, row=2)
btn3 = tk.Button(root, text="9", width=8, height=5, bg='blue',font=("Arial Black",10), command=lambda: print_text("9"))
btn3.grid(column=2, row=2)
btn4 = tk.Button(root, text="-", width=8, height=5, bg='orange',font=("Arial Black",10), command=lambda: print_text("-"))
btn4.grid(column=3, row=2)

btn5 = tk.Button(root, text="4", width=8, height=5, bg='blue',font=("Arial Black",10),command=lambda: print_text("4"))
btn5.grid(column=0, row=3)
btn6 = tk.Button(root, text="5", width=8, height=5, bg='blue',font=("Arial Black",10),command=lambda: print_text("5"))
btn6.grid(column=1, row=3)
btn7 = tk.Button(root, text="6", width=8, height=5, bg='blue',font=("Arial Black",10),command=lambda: print_text("6"))
btn7.grid(column=2, row=3)
btn8 = tk.Button(root, text="*", width=8, height=5, bg='orange',font=("Arial Black",10),command=lambda: print_text("*"))
btn8.grid(column=3, row=3)

btn9 = tk.Button(root, text="1", width=8, height=5, bg='blue',font=("Arial Black",10),command=lambda: print_text("1"))
btn9.grid(column=0, row=4)
btn10 = tk.Button(root, text="2", width=8, height=5,bg='blue',font=("Arial Black",10), command=lambda: print_text("2"))
btn10.grid(column=1, row=4)
btn11 = tk.Button(root, text="3", width=8, height=5, bg='blue',font=("Arial Black",10),command=lambda: print_text("3"))
btn11.grid(column=2, row=4)
btn12 = tk.Button(root, text="+", width=8, height=5, bg='orange',font=("Arial Black",10),command=lambda: print_text("+"))
btn12.grid(column=3, row=4)

btn13 = tk.Button(root, text="00", width=8, height=5, bg='blue',font=("Arial Black",10),command=lambda: print_text("00"))
btn13.grid(column=0, row=5)
btn14 = tk.Button(root, text="0", width=8, height=5, bg='blue',font=("Arial Black",10),command=lambda: print_text("0"))
btn14.grid(column=1, row=5)
btn15 = tk.Button(root, text=".", width=8, height=5, bg='blue',font=("Arial Black",10),command=lambda: print_text("."))
btn15.grid(column=2, row=5)
btn16 = tk.Button(root, text="=", width=8, height=5, bg='orange',font=("Arial Black",10),command=evaluate)
btn16.grid(column=3, row=5)

root.mainloop()