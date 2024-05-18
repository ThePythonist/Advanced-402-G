import tkinter

window = tkinter.Tk()

window.title("Some Window")
window.geometry("320x500")
window.configure(background="#c54619", )


def show_message():
    message.config(text="Button Clicked!", bg="white")


message = tkinter.Label(window, text="", background="#c54619")
message.pack()
btn = tkinter.Button(window, text="Submit", command=show_message).pack(anchor="s")

window.mainloop()
