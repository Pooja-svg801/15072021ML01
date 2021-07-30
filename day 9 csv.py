import tkinter as tk
import csv
app = tk.Tk(__name__)
app.title('Form')
app.geometry('300x200')

name = tk.Variable(app)
name.set('')

email = tk.Variable(app)
email.set('')

mobilenumber = tk.Variable(app)
mobilenumber.set('')

tk.Label(app, text = 'Name',\
         font=('Arial',14),
         bg='black',fg='white'
         ).place(x=0,y=0)
tk.Entry(app, textvariable = name,\
         font=('Arial',10)
         ).place(x=70,y=0)

tk.Label(app, text = 'Email',\
         font=('Arial',12),
         bg='black',fg='white'
         ).place(x=0,y=30)
tk.Entry(app, textvariable = email,\
         font=('Arial',10)
         ).place(x=70,y=30)

tk.Label(app, text = 'Mobile',\
         font=('Arial',12),
         bg='black',fg='white'
         ).place(x=0,y=60)
tk.Entry(app, textvariable = mobilenumber,\
         font=('Arial',10)
         ).place(x=70,y=60)


def file_entry(name,email,mobilenumber):
    with open("data_form.csv","a") as f:
        datawriter =csv.writer(f)
        datawriter.writerow(['name','email','mobilenumber'])
        f.close()

def result():
    Name=name.get()
    Email=email.get()
    Mobile=mobilenumber.get()
    file_entry(Name,Email,Mobile)
    print("Submitted Successfully")
    name.set('')
    email.set('')
    mobilenumber.set('')

tk.Button(app,text="Submit",command=result).place(x=100,y=160)
         

app.mainloop() 
