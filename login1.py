from tkinter import *
import tkinter as tk
from tkinter import tk
l=[['mukesh','m123'],['tapan','tapi123'],['dinky','']]
def login():
    uname=unam.get()
    pwd=passw.get()
    for u in 
root=tk.Tk()
frame=Frame(root)
l1=tk.Label(root,text="enter username")
unam=tk.Entry(root)
l2=tk.Label(root,text="password")
passw=tk.Entry(root,show="*")
b1=tk.Button(root,text="login",command=login).grid(row=2,column=0)
l1.pack()
unam.pack()
l2.pack()
passw.pack()
b1.pack()
frame.pack()
root.mainloop()
