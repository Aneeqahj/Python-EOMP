from tkinter import *
import requests
from tkinter import messagebox

root = Tk()
root.title("Lotto Machine")
root.resizable("false", "false")
root.geometry("600x500")
root.config(bg="#835134")

# All the imports


value = IntVar()

# Retrieving the information from an external JSON file as a source of reference
information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/ZAR')
information_json = information.json()

conversion_rate = information_json['conversion_rates']
# print(conversion_rate)


# Creating a label and entry for the results
value_label = Label(root, text="Value")
value_label.config(bg="#835134")
value_label.pack()

value_entry = Entry(root, textvariable=value, width=40)
value_entry.config(bg="white")
value_entry.pack()

# Creating the FROM (Standard value is ZAR)
from_label = Label(root, text="From: ZAR")
from_label.config(bg="#835134")
from_label.pack()

# Doing the Conversion of the data with its loop
convert = Label(root, text="To:")
convert.config(bg="#835134")
convert.pack()

convert_list = Listbox(root, width=20)
for i in conversion_rate.keys():
    convert_list.insert(END, str(i))
convert_list.pack()

convert_label = Label(root, text="Converted to: ")
convert_label.config(bg="#835134")
convert_label.pack()


def convert_curr():
    num = float(value_entry.get())
    ans = num * information_json['conversion_rates'][convert_list.get(ACTIVE)]
    convert_label['text'] = round(ans, 2)


convert_btn = Button(root, command=convert_curr, text="Convert", width=20, borderwidth=2)
convert_btn.config(bg="white")
convert_btn.pack()


def exit():
    msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                     icon='warning')
    if msg_box == "yes":
        root.destroy()
    else:
        messagebox.showinfo("Return", "You will now return to the App", icon="warning")


exit_btn = Button(root, command=exit, text="Exit", borderwidth=2, bg="white", width=20)
exit_btn.place(x=205, y=350)


def back():
    msg_box = messagebox.askquestion("Return", "You will now return to bank details")

    if msg_box == "yes":
        root.destroy()
        import main3
    else:
        messagebox.showinfo("Return", "You will remain on this page")


back_btn = Button(root, command=back, text="Back", borderwidth=2, bg="white", width=20)
back_btn.place(x=205, y=410)

root.mainloop()
root.mainloop()
