import tkinter as tk
import random

window = tk.Tk()
window.title("Dice")
window.columnconfigure(0, weight=1, minsize=50)
window.rowconfigure([0, 1], minsize=50, weight=1)
window.geometry("240x120+600+550")
window.resizable(False, False)
favicon = "favicon.ico"
window.iconbitmap(default=favicon)

def rand():
    lbl_result["text"] = str(random.randint(0, 6))


btn_roll = tk.Button(master=window, relief=tk.RAISED,  text="Roll", borderwidth=5, command=rand)
btn_roll.grid(row=0, column=0, sticky="nsew")

lbl_result = tk.Label(text="0")
lbl_result.grid(row = 1, column=0)


window.mainloop()


