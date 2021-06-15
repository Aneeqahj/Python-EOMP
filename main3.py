from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Lotto Machine")
root.config(bg="#835134")
root.resizable("false", "false")
root.geometry("600x400")
variable = StringVar(root)


class Details:
    variable.set("Select")

    def __init__(self, root):
        self.congrats = Label(root, text="Congratulations! Enter details:", bg="#835134", font=("Arial", 15))
        self.congrats.place(x=200, y=20)
        self.acc = Label(root, text="Account holder name:", bg="#835134")
        self.acc.place(x=100, y=100)
        self.acc_ent = Entry(root)
        self.acc_ent.place(x=300, y=100)
        self.bank = Label(root, text="Bank account number:", bg="#835134")
        self.bank.place(x=100, y=150)
        self.bank_ent = Entry(root)
        self.bank_ent.place(x=300, y=150)
        self.bank_opt = Label(root, text="Choose Bank:", bg="#835134")
        self.bank_opt.place(x=100, y=200)
        self.option = OptionMenu(root, variable, "FNB", "Absa", "Nedbank", "Standard bank")
        self.option.place(x=300, y=200)
        self.enter = Button(root, text="Enter", bg="#CB9B7C", borderwidth=2)
        self.enter.place(x=100, y=250)
        self.exit = Button(root, text="Exit", bg="#CB9B7C", borderwidth=2, command=self.exit)
        self.exit.place(x=500, y=250)
        self.con_lbl = Label(root, text="If you wish to convert to another currency, click the button below:",
                             bg="#835134", font=("Arial", 12))
        self.con_lbl.place(x=50, y=300)
        self.convert = Button(root, text="Convert", bg="#CB9B7C", borderwidth=2, width=10)
        self.convert.place(x=250, y=350)

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                         icon='warning')
        if msg_box == "yes":
            root.destroy()
        else:
            messagebox.showinfo("Return", "You will now return to the App", icon="warning")


obj = Details(root)
root.mainloop()
