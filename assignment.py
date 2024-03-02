import tkinter as tk

window = tk.Tk()
window.title("HW")
window.geometry("320x240")
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1 , 2], minsize=50, weight=1)


def addition():
    amount = int(lbl_value["text"])
    lbl_value["text"] = str(amount+1)

def subtraction():
    amount = int(lbl_value["text"])
    lbl_value["text"] = str(amount - 1)

btn_minus = tk.Button(master=window, text="-", command=subtraction)
btn_minus.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_add = tk.Button(master=window, text="+", command=addition)
btn_add.grid(row=0, column=2, sticky="nsew")


window.mainloop()