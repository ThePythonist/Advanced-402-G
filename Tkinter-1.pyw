import tkinter

window = tkinter.Tk()
window.title("My Window")
window.geometry("500x500")

window.resizable(width=False, height=False)
window.configure(background="#9b0027")


def report():
     print("clicked submit button")


# mylabel = tkinter.Label(window, text="Welcome").pack(anchor="n", side="right")

mylabel = tkinter.Label(window, text="Welcome", bg="khaki",fg="black").pack(fill="x", expand=False)

#mybutton = tkinter.Button(window, text="Submit", command=report).pack()

window.mainloop()
