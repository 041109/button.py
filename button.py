from tkinter import*
window = Tk()
window.geometry("200x500")
window.title("Button.py")
button = Button(window,text="Click here",background="red",bd=5,activebackground="white",activeforeground="green",command=window.destroy)
button.pack()

window.mainloop()

