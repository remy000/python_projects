from tkinter import *
from time import *

def update():
    time_string=strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    
    day_string=strftime("%A")
    day_label.config(text=day_string)
    
    date_string=strftime("%B %d,%Y")
    date_label.config(text=date_string)
    
    time_label.after(1000,update)


 
    
window= Tk()
time_label=Label(window, font=('consolas', 50,'bold'), fg='white', bg='#000080')
time_label.pack()

day_label=Label(window, font=('consolas', 25 ,'bold'), fg='white', bg='#000080')
day_label.pack()

date_label=Label(window, font=('Arial', 35,'bold'), fg='white', bg='#000080')
date_label.pack()

update()

window.mainloop()