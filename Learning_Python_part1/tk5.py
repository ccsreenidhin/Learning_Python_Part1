import Tkinter as tk

counter = 5

def counter_label(label):
    def count():
        global counter
        counter+=1
        label.config(text = str(counter))
        label.after(1000, count)
    count()


top = tk.Tk()

top.title("counter")
label =tk.Label(top, fg ="darkgreen")
label.config(text ="0")
label.pack()

#counter_label(label)

button =tk.Button(top, text = 'Stop', width =25, command = top.destroy)

button.pack()
top.mainloop()
