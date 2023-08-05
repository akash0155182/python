import tkinter as tk
from tkinter import messagebox
var = ""  
A = 0  
operator = ""  
   
def one_is_clicked():  
    global var  
    var = var + "1"  
    the_data.set(var)  
   
def two_is_clicked():  
    global var  
    var = var + "2"  
    the_data.set(var)  

def three_is_clicked():  
    global var  
    var = var + "3"  
    the_data.set(var)  
  
def four_is_clicked():  
    global var  
    var = var + "4"  
    the_data.set(var)  

def five_is_clicked():  
    global var  
    var = var + "5"  
    the_data.set(var)  
  
def six_is_clicked():  
    global var  
    var = var + "6"  
    the_data.set(var)  
   
def seven_is_clicked():  
    global var  
    var = var + "7"  
    the_data.set(var)  
  
def eight_is_clicked():  
    global var  
    var = var + "8"  
    the_data.set(var)  
  
def nine_is_clicked():  
    global var  
    var = var + "9"  
    the_data.set(var)  
   
def zero_is_clicked():  
    global var  
    var = var + "0"  
    the_data.set(var)  
    
def add_is_clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "+"  
    var = var + "+"  
    the_data.set(var)  
    
def Sub_is_clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "-"  
    var = var + "-"  
    the_data.set(var)  
   
def Mul_is_clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "*"  
    var = var + "*"  
    the_data.set(var)

def Div_is_clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "/"  
    var = var + "/"  
    the_data.set(var) 

def Equal_is_clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "="  
    var = var + "="  
    the_data.set(var)  
  
def AC_is_clicked():  
    global A  
    global var  
    global operator  
    var = ""  
    A = 0  
    operator = ""  
    the_data.set(var)  
  
def result():  
    global A  
    global operator  
    global var  
    var2 = var  
    if operator == "+":  
        a = float((var2.split("+")[1]))  
        x = A + a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "-":  
        a = float((var2.split("-")[1]))  
        x = A - a  
        the_data.set(a=x)  
        var = str(x)  
    elif operator == "*":  
        a = float((var2.split("*")[1]))  
        x = A * a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "/":  
        a = float((var2.split("/")[1]))  
        if a == 0:  
            messagebox.showerror("Division by 0 Not Allowed.")  
            A == ""  
            var = ""  
            the_data.set(var)  
        else:  
            x = float(A/a)  
            the_data.set(x)  
            var = str(x)  
root=tk.Tk()
root.geometry("320x500+400+400")
root.resizable(0,0)    
the_data = tk.StringVar()  
guiLabel = tk.Label( root,text = "Label",anchor = tk.SE,font = ("Cambria Math", 20),textvariable = the_data,background = "#ffffff",fg = "#000000") 
guiLabel.pack(expand = True, fill = "both") 

frameOne = tk.Frame(root, bg = "#000000")  
frameOne.pack(expand = True, fill = "both")

frameTwo = tk.Frame(root, bg = "#000000")  
frameTwo.pack(expand = True, fill = "both")  
  
frameThree = tk.Frame(root, bg = "#000000")  
frameThree.pack(expand = True, fill = "both")  
  
frameFour = tk.Frame(root, bg = "#000000")  
frameFour.pack(expand = True, fill = "both") 

one=tk.Button(frameOne,text="1",font=("Cambria",22),relief = tk.GROOVE,border=0,fg="green",command=one_is_clicked)
two=tk.Button(frameOne,text="2",font=("Cambria",22),relief = tk.GROOVE,border=0,fg="green",command=two_is_clicked)
three=tk.Button(frameOne,text="3",font=("Cambria",22),relief = tk.GROOVE,border=0,fg="green",command=three_is_clicked)
ac=tk.Button(frameOne,text="AC",font=("Cambria",22),relief = tk.GROOVE,border=0,fg="green",command=AC_is_clicked)
four=tk.Button(frameTwo,text="4",font=("Cambria",22),relief = tk.GROOVE,border=0,fg="green",command=four_is_clicked)
five=tk.Button(frameTwo,text="5",font=("Cambria",22),relief = tk.GROOVE,border=0,fg="green",command=five_is_clicked)
six=tk.Button(frameTwo,text="6",font=("Cambria",22),relief = tk.GROOVE,border=0,fg="green",command=six_is_clicked)
plus=tk.Button(frameTwo,text="+",font=("Cambria",22),relief = tk.GROOVE,border=0,fg="green",command=add_is_clicked)
seven=tk.Button(frameThree,text="7",font=("Cambria",22),relief = tk.GROOVE,border=0,fg="green",command=seven_is_clicked)
eight=tk.Button(frameThree,text="8",font=("Cambria",22),relief = tk.GROOVE,border=0,fg="green",command=eight_is_clicked)
nine=tk.Button(frameThree,text="9",font=("Cambria",22),relief = tk.GROOVE,border=0,fg="green",command=nine_is_clicked)
minus=tk.Button(frameThree,text="-",font=("Cambria",22),relief = tk.GROOVE,border=0,fg="green",command=Sub_is_clicked)
zero=tk.Button(frameFour,text="0",font=("Cambria",22),relief = tk.GROOVE,border=0,fg="green",command=zero_is_clicked)
mul=tk.Button(frameFour,text="*",font=("Cambria",22),relief = tk.GROOVE,border=0,fg="green",command=Mul_is_clicked)
div=tk.Button(frameFour,text="/",font=("Cambria",22),relief = tk.GROOVE,border=0,fg="green",command=Div_is_clicked)
equal=tk.Button(frameFour,text="=",font=("Cambria",22),relief = tk.GROOVE,border=0,fg="green",command=result)
one.pack(side = tk.LEFT, expand = True, fill = "both")  
two.pack(side = tk.LEFT, expand = True, fill = "both")  
three.pack(side = tk.LEFT, expand = True, fill = "both")  
ac.pack(side = tk.LEFT, expand = True, fill = "both")
four.pack(side = tk.LEFT, expand = True, fill = "both")
five.pack(side = tk.LEFT, expand = True, fill = "both")
six.pack(side = tk.LEFT, expand = True, fill = "both")
plus.pack(side = tk.LEFT, expand = True, fill = "both")
seven.pack(side = tk.LEFT, expand = True, fill = "both")
eight.pack(side = tk.LEFT, expand = True, fill = "both")
nine.pack(side = tk.LEFT, expand = True, fill = "both")
minus.pack(side = tk.LEFT, expand = True, fill = "both")
zero.pack(side = tk.LEFT, expand = True, fill = "both")
mul.pack(side = tk.LEFT, expand = True, fill = "both")
div.pack(side = tk.LEFT, expand = True, fill = "both")
equal.pack(side = tk.LEFT, expand = True, fill = "both")
 
root.mainloop()