from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry('600x600')
root.title('Covid Vaccine Registration Form')
root.config(background='#ffffff')

fn = StringVar()
ln = StringVar()
age = StringVar()
var = StringVar()
contact_no = StringVar()
email_id = StringVar()
var_c1 = 'Cold'
var_c2 = 'Fever'
var_c3 = 'Cough'
var_c4 = 'Headache'
radio_var = StringVar()


def printent():
    first = fn.get()
    second = ln.get()
    dob1 = age.get()
    contact = contact_no.get()
    email = email_id.get()
    var1 = var.get()
    var3 = var_c1
    var3 = var_c2 
    var3 = var_c3
    var3 = var_c4
    var4  = radio_var.get()

    print(f'The full name is {first} {second}')
    print(f'Your age is {dob1}')
    print(f'Your gender is {var4}')
    print(f'Your country is {var1}')
    print(f'You selected symptoms is {var3}')
    print(f'Number registered: {contact}')
    print(f'Email registered: {email}')
    tkinter.messagebox.showinfo('User has successfully signed up!')


heading = Label(root, text='Covid Vaccine Registration', relief=SOLID, width=30, font='arial 19 bold', fg='#b30047', bg='#ffffff')
heading.place(x=90, y=10)

fname = Label(root, text="Name :",width=20,font=("bold", 10),bg='#ffffff')
fname.place(x=100,y=70)
efname = Entry(root,textvar=fn)
efname.place(x=300,y=70)

date = Label(root, text="Age :",width=20,font=("bold", 10),bg='#ffffff')
date.place(x=100,y=120)
edob = Entry(root,textvar=age)
edob.place(x=300,y=120)

Gender = Label(root, text="Gender :",width=20,font=("bold", 10),bg='#ffffff')
Gender.place(x=93,y=170)
r1=Radiobutton(root, text="Male", variable=radio_var, value="Male").place(x=300,y=170)  
r2=Radiobutton(root, text="Female", variable=radio_var, value="Female").place(x=360,y=170) 

Country = Label(root, text="Country :",width=20,font=("bold", 10),bg='#ffffff')
Country.place(x=95,y=220)
List=["Nepal","India",'America','China',"Canada",'Japan','South Africa']
droplist=OptionMenu(root,var,*List)
var.set("Select Country")
droplist.config(width=15)
droplist.place(x=300,y=220)

lname = Label(root, text="Address :",width=20,font=("bold", 10),bg='#ffffff')
lname.place(x=100,y=270)
elname = Entry(root,textvar=ln)
elname.place(x=300,y=270)

Lang = Label(root, text="Symptoms :",width=20,font=("bold", 10),bg='#ffffff')
Lang.place(x=100,y=320)
c1 = Checkbutton(root, text="Cold", variable=var_c1).place(x=300,y=320)  
c2 = Checkbutton(root, text="Fever", variable=var_c2).place(x=360,y=320)  
c3 = Checkbutton(root, text='Cough', variable=var_c3).place(x =420, y=320)
c4 = Checkbutton(root, text='Headache', variable=var_c4).place(x =490, y=320)

contactno = Label(root, text="Contact No :",width=20,font=("bold", 10),bg='#ffffff')
contactno.place(x=100,y=370)
econtactno = Entry(root,textvar=fn)
econtactno.place(x=300,y=370)

mailid = Label(root, text="Email Id :",width=20,font=("bold", 10),bg='#ffffff')
mailid.place(x=100,y=420)
emailid = Entry(root,textvar=fn)
emailid.place(x=300,y=420)

Submit=Button(root, text='Submit',width=12,bg='#4b4d4a',fg='white',command=printent).place(x=150,y=500)
quit=Button(root, text='Quit',width=12,bg='#4b4d4a',fg='white',command=exit).place(x=320,y=500)
root.mainloop()