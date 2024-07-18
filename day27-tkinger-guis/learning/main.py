import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)


def button_clicked():
    my_label.config(text=input.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(row=0, column=2)

input = tkinter.Entry()
input.grid(row=2, column=3)

window.mainloop()
