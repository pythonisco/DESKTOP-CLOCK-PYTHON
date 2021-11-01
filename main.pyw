# making imports
from tkinter import *
from tkinter.ttk import *
from time import strftime

# configuring the app
app = Tk()
app.geometry("600x500+0+650")
app.overrideredirect(True)
app.wm_attributes('-transparentcolor','black')
app.config(bg="black")

# making a function
def clock():
    st = strftime('%H:%M:%S')
    label.config(text = st)
    label.after(1000, clock)

# I have styled these labels according to my liking, you may do the same to yours as well
label = Label(app, font = ('times new roman', 90),
            background = 'black',
            foreground = 'white')

label.pack()
clock()
app.mainloop()