import tkinter

window = tkinter.Tk()
window.minsize(width=500, height=300)

input = tkinter.Entry()
input.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(row=1, column=0)

solution = tkinter.Label(text="0")
solution.grid(row=1, column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)


def convert():
    miles = int(input.get())
    km = miles * 1.609344
    solution.config(text=f"{km}")


calculate = tkinter.Button(text="Calculate", command=convert)
calculate.grid(row=2, column=1)

window.mainloop()
