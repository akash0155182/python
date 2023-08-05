import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.geometry("300x300")
def res():
    .
    

l1=tk.Label(root,text="enter the first no:",fg="green",font=("Cambria",15)).place(x=10,y=10)
t1=tk.Entry().place(x=170,y=20)
l2=tk.Label(root,text="enter the second no:",fg="green",font=("Cambria",15)).place(x=10,y=40)
t2=tk.Entry().place(x=190,y=50)
plus=tk.Button(root,text="+",fg="black",bg="blue",font=("Cambria",20),command=).place(x=10,y=80)
minus=tk.Button(root,text="-",fg="black",bg="blue",font=("Cambria",20)).place(x=60,y=80)
mul=tk.Button(root,text="*",fg="black",bg="blue",font=("Cambria",20)).place(x=110,y=80)
Div=tk.Button(root,text="/",fg="black",bg="blue",font=("Cambria",20)).place(x=160,y=80)

root.mainloop()