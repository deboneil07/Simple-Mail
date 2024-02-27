import tkinter as tk

window = tk.Tk()
window.title("Console")

def get_entry_value():
    entry_text = entry.get()
    print("the value: ", entry_text)


label = tk.Label(
    text="""
    Console Print
    """,
    foreground='#1BF60D',
    background='black',
    width=60,
    height=10
)

button = tk.Button(
    text="Print value",
    width=20,
    height=2,
    bg="black",
    fg="blue",
    command=get_entry_value
)

entry = tk.Entry(
    fg="yellow",
    bg="black",
    width=20,
)

label.pack()

entry.pack()
button.pack()

# Start the tkinter event loop
window.mainloop()
