from tkinter import*
from tkinter.ttk import*
window = Tk()
window.geometry("200x200")
window.title("Progress Bar")

progress = Progressbar(window,orient=HORIZONTAL,length=150)
def bar():
    import time
    progress["value"]=10
    window.update_idletasks()
    time.sleep(1)

    progress["value"]=20
    window.update_idletasks()
    time.sleep(1)

    progress["value"]=30
    window.update_idletasks()
    time.sleep(1)

    progress["value"]=40
    window.update_idletasks()
    time.sleep(1)

    progress["value"]=50
    window.update_idletasks()
    time.sleep(1)



progress.pack(pady=20)

button=Button(window,text="Progress",command=bar)
button.pack(pady=20)

# adding a spinbox
w = Spinbox(window,from_=0,to = 10,increment=0.5,format = "%00.3f")
w.pack(pady=1)















window.mainloop()