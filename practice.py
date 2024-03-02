import tkinter as tk

window = tk.Tk()
window.title("App")
window.config(background="black", highlightbackground="black", highlightcolor="black")


# ?FRAME FOR FORM
frame_form = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=4)
frame_form.pack()


# !another method for DRY principles

labels = [
    "First Name",
    "Last Name",
    "Address Line 1",
    "Address Line 2",
    "City",
    "Country"
]

for i, text in enumerate(labels):
    label = tk.Label(master=frame_form, text=text)
    entry = tk.Entry(master=frame_form, width=40)

    label.grid(row = i, column = 0, sticky="e")
    entry.grid(row = i, column = 1)
    frame_form.columnconfigure(i, weight=1, minsize=10)
    frame_form.rowconfigure(i, weight=1, minsize=10)




# # !label and input field for first name

# lbl_first_name = tk.Label(frame_form,  text="First Name")
# ent_first_name = tk.Entry(frame_form, width=30)

# lbl_first_name.grid(column=0, row=0, sticky="e")
# ent_first_name.grid(column=1, row=0)

# # !label and input field for last name

# lbl_last_name = tk.Label(master=frame_form, text="Last Name")
# ent_last_name = tk.Entry(master=frame_form, width=30)

# lbl_last_name.grid(row=1, column=0, sticky="e")
# ent_last_name.grid(row=1, column=1)

# # !label and input fields for Address Line 1

# lbl_address1 = tk.Label(master=frame_form, text="Address Line 1")
# ent_address1 = tk.Entry(master=frame_form, width=30)

# lbl_address1.grid(row=2, column=0, sticky="e")
# ent_address1.grid(row=2, column=1)

# # !label and input fields for Address Line 2

# lbl_address2 = tk.Label(master=frame_form, text="Address Line 2")
# ent_address2 = tk.Entry(master=frame_form, width=30)

# lbl_address2.grid(row=3, column=0, sticky="e")
# ent_address2.grid(row=3, column=1)

# # !label and input fields for City

# lbl_city = tk.Label(master=frame_form, text="City")
# ent_city = tk.Entry(master=frame_form, width=30)

# lbl_city.grid(row=4, column=0, sticky="e", padx=1)
# ent_city.grid(row=4, column=1)

# # !label for Country

# lbl_country = tk.Label(master=frame_form, text="Country")
# ent_country = tk.Entry(master=frame_form, width=30)

# lbl_country.grid(row=5, column=0, sticky="e")
# ent_country.grid(row=5, column=1)

# ?frame for buttons

btn_frame = tk.Frame(master=window, relief=tk.RAISED)
btn_frame.pack(fill=tk.X, ipadx=5, ipady=5)

# !button for Clear

clr = tk.Button(master=btn_frame, relief=tk.RAISED, text="Clear", width=8)
submit = tk.Button(master=btn_frame, relief=tk.RAISED, text="Submit", width=8)

btn_frame.columnconfigure(0, weight=1)

submit.pack(side=tk.RIGHT, ipadx=20, padx=5)
clr.pack(side=tk.RIGHT, padx=5)


 







tk.mainloop()