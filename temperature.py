import tkinter as tk

window = tk.Tk()
window.geometry("240x120")
window.resizable(False, False)
window.title("Temp Convert")
window.iconbitmap("favicon.ico")

def conversion():
    fahrenheit = ent_temp.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = str(round(celsius, 2))


ent_temp = tk.Entry(master=window, width=10)
ent_temp.grid(row=0, column=0, padx=(10,0), pady=10, sticky="e")

lbl_f = tk.Label(master=window, text="\N{DEGREE FAHRENHEIT}")
lbl_f.grid(row=0, column=1, padx=(2,0), sticky="w")

lbl_c = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
lbl_c.grid(row=0, column=4, padx=(2,0), sticky="w")


btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", width=3, command=conversion)
btn_convert.grid(row=0, column=2, padx=(10,0))

lbl_result = tk.Label(master=window, relief=tk.SUNKEN, borderwidth=2, width=10)
lbl_result.grid(row=0, column=3, padx=(8,0))



window.mainloop()