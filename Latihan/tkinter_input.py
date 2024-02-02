import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

windows = tkinter.Tk()
windows.configure(bg="white")
windows.geometry("250x200")
windows.resizable(False, False)
windows.title("Python Input Testing")

# VARIABLE
inputSomething = tkinter.StringVar()

# FRAME
inputFrame = ttk.Frame(windows)
inputFrame.pack(padx=10, pady=10, fill="x", expand=True)

# OBJECT

# label
inputLabel = ttk.Label(inputFrame, text="Input Something")
inputLabel.pack(padx=10, pady=5, fill="x", expand=True)

# entry
inputEntry = ttk.Entry(inputFrame, textvariable=inputSomething)
inputEntry.pack(padx=10, pady=10, fill="x", expand=True)


# button
def buttonCommand():
    inputMessage = f"YOUR INPUT =>  {inputSomething.get()}"
    showinfo(message=inputMessage)


inputButton = ttk.Button(inputFrame, text="Input!", command=buttonCommand)
inputButton.pack(pady=5)

windows.mainloop()
