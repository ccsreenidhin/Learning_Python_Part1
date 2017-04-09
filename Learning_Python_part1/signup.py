from Tkinter import *

window = Tk()

label1 =Label(window, text="Username")
label2 =Label(window, text="Password")
label3 =Label(window, text="Re-enter Password")
label4 =Label(window, text="Type the above text here")

entry1 =Entry(window)
entry2 =Entry(window, show="*")
entry3 =Entry(window, show="*")
entry4 =Entry(window)

label1.grid(row = 0, sticky = E)
label2.grid(row = 2, sticky = E)
label3.grid(row = 4, sticky = E)
label4.grid(row = 8, column = 1)

entry1.grid(row=0, column=1)
entry2.grid(row=2, column=1)
entry3.grid(row=4, column=1)
entry3.grid(row=10, column=1)

cap= PhotoImage(file="C:\hh\captcha.gif")
Label4 =Label(window, image=cap).grid(row=6, column =1)

frsh = PhotoImage(file="C:\hh\ew.gif")
rebtn= Button(window, image=frsh)
rebtn.grid(row =6, column = 2)

logbtn = Button(window, text= "Submit")
logbtn.grid(columnspan= 2)


window.mainloop()
