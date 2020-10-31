from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
import os
import tkinter as tk
import random
from tkinter import messagebox
def showimage():
    fln=filedialog.askopenfilename(initialdir=r"C:\Users\AZMI\anaconda3\lib\tkinter\__init__.py",title='select image',filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("ALL Files","*.*")))
    img=Image.open(fln)
    img.thumbnail((350,350))
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image=img
    
def reset():
    global words1,answers1,num11
    num1=random.randrange(0,3,1)
    lbl1.configure(text=words[num1])
    e5.delete(0,END)

def check_answer():
    global words1,answers1,num1
    var=e5.get()
    if var==answers1[num1]:
        messagebox.showinfo("SUCCESS","THIS IS A CORRECT ANSWER")
        reset()
    else:
        messagebox.showerror("ERROR","THIS IS A WRONG  ANSWER")
        e5.delete(0,END)
        
def default():
    global words,answers,num
    lbl1.configure(text=words[num])  
    
def reset_1():
    global words2,words3,answers2,num2
    num2=random.randrange(0,11,1)
    lbl11.configure(text=words1[num2])
    lbl13.configure(text=words2[num2])
    e6.delete(0,END)

def check_answers_1():
    global words2,words3,answers2,num2
    var=e6.get()
    if var==answers2[num2]:
        messagebox.showinfo("SUCCESS","THIS IS A CORRECT ANSWER")
        reset_1()
    else:
        messagebox.showerror("ERROR","THIS IS A WRONG  ANSWER")
        e6.delete(0,END)
        
def defaults():
    global words,answers,num
    lbl11.configure(text=words1[num2]) 
    lbl13.configure(text=words2[num2])
    
    

    
root=Tk()
lbl=Label(root)
lbl.pack()



frm=Frame(root,bd=20,bg='violet')
frm.pack(side=tk.RIGHT,ipadx=10,pady=0)

frm2=Frame(root,bd=20,bg='violet')
frm2.pack(side=tk.BOTTOM,ipadx=50,pady=40)

frm3=Frame(root,bd=20,bg='violet')
frm3.pack(side=tk.TOP,ipadx=50,pady=0)


lbl8=Label(frm,text='EASY TO LEARN',bg='violet',fg='black',font=("Verdana",25,'bold'))
lbl8.pack(side=TOP)

btn=Button(frm,text='LEARNING WITH CARTOON',command=showimage,bg="green", fg="black",font=("Modern Love",18,'bold'))
btn.pack(side=tk.LEFT)
btn2=Button(frm,text='exit',bg="blue", fg="white",command=lambda:exit(),font='40')
btn2.pack(side=tk.LEFT,padx=10,pady=15)


answers1=['ONE','TWO','3']
words=['NOE','WTO','THREE']
num1=random.randrange(0,3,1)

answers2=['3','5','7','13','9','4','8','14','30','50','18']
words1=['1','2','3','6','4','2','5','7','8','20','25','12']
words2=['2','3','4','7','5','2','3','7','6','10','25','6']
num2=random.randrange(0,3,1)



 
lbl1=Label(frm2,text='GUESS THE SPELLING OF NUMBERS',bg='violet',fg='black',font=("Verdana",20,'bold'))
lbl1.pack(side=TOP)
lbl1=Label(frm2,text="xyz",bg='black',fg='red',font=("Verdana",15,'bold'))
lbl1.pack(side=TOP,pady=10)

e5=Entry(frm2,font=('Verdana',15,'bold'),bg='powder blue')
e5.pack(side=tk.TOP,ipadx=30,pady=10)
lb15=Label(frm2,text="GIVE YOUR ANSWER",font=("Verdana",10,'italic'),bg='yellow')
lb15.pack()

btn3=Button(frm2,text='check',command=check_answer,bg="green", fg="black",font='20',relief=RAISED,width=10)
btn3.pack(side=tk.LEFT,padx=85)
btn4=Button(frm2,text='RESET',bg="blue", fg="#EB9694",command=reset,font='20',width=10)
btn4.pack(side=tk.TOP)


frm3=Frame(root,bd=20,bg='violet')
frm3.pack(side=tk.TOP,ipadx=50,pady=0)

lbl11=Label(frm3,text="xyz",bg='black',fg='red',font=("Verdana",15,'bold'))
lbl11.pack(side=TOP,pady=10)

lbl12=Label(frm3,text="+",bg='black',fg='red',font=("Verdana",15,'bold'))
lbl12.pack(side=TOP,pady=10)

lbl13=Label(frm3,text="xyz",bg='black',fg='red',font=("Verdana",15,'bold'))
lbl13.pack(side=TOP,pady=10)

e6=Entry(frm3,font=('Verdana',13,'bold'),bg='powder blue')
e6.pack(side=tk.TOP,ipadx=20,pady=5)
lb14=Label(frm3,text="GIVE YOUR ANSWER",font=("Verdana",10,'italic'),bg='yellow')
lb14.pack()
btn6=Button(frm3,text='check',command=check_answers_1,bg="green", fg="black",font='20',relief=RAISED,width=10)
btn6.pack(side=tk.LEFT,padx=40)
btn7=Button(frm3,text='RESET',bg="blue", fg="#EB9694",command=reset_1,font='20',width=10)
btn7.pack(side=tk.TOP,pady=15)
  

default()

defaults()    
    
root.title=('iamge browser')
root.geometry("170x200+30+30") 
root.configure(bg='pink')


root.mainloop()











     
        
    

    
    





