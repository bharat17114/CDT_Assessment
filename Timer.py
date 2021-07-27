from tkinter import *
from tkinter.ttk import *
import time


tk=Tk()

progress=Progressbar(tk,orient=HORIZONTAL,length=500,mode='determinate')
progress['value'] = 100

def bar():
    if progress['value'] > 0:
        progress['value'] -=1
        tk.update_idletasks()
        tk.after(50,bar)
    else:
        print("you ran out of time")
    

        
progress.pack()
Button(tk,text='Start',command=bar).pack()
mainloop()
