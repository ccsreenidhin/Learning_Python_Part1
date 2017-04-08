from Tkinter import *

root = Tk()

img = PhotoImage(file="C:\hh\python-512.gif")

h1 = """ Python Login form"""

txt = """New user!! Sign up here"""

#w = Label(root, justify = CENTER, text = h1, fg = "yellow", font = "Times 30 bold").pack(side = "right")
w1 = Label(root, justify = LEFT, compound = LEFT, padx = 20,pady = 40, text = txt, fg ="darkgreen",bg="grey", font = "Verdana 15 bold italic" , image =img).pack(side="left")

root.mainloop()
