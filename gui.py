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
    command=get_entry_value,
    relief=tk.RAISED
)

entry = tk.Entry(
    fg="yellow",
    bg="black",
    width=20,
)

for i in range(4, 7):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        lb1 = tk.Label(master=frame, text=f"Row: {i}\n Column: {j}")
        lb1.grid(row=0, column=0)
        



label.grid(row=1, column=0, columnspan=1)
entry.grid(row=2, column=0, columnspan=1, pady=10)
button.grid(row=3, column=0, columnspan=1, pady=10)


# Start the tkinter event loop
window.mainloop()
