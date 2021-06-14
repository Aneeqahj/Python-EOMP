from tkinter import *  # Aneeqah Jones, Class 1
from tkinter import messagebox
from playsound import playsound

root = Tk()
root.resizable("false", "false")
root.geometry("600x400")
root.config(bg="lime")
root.title("Lotto Machine")


class Info:
    def __init__(self, root):
        self.details = Label(root, text="Fill in the details below:", bg="lime", font=("Arial", 15))
        self.details.place(x=220, y=20)
        self.name = Label(root, text="Name:", bg="lime")
        self.name.place(x=100, y=100)
        self.name_ent = Entry(root)
        self.name_ent.place(x=200, y=100)
        self.email = Label(root, text="Email:", bg="lime")
        self.email.place(x=100, y=150)
        self.email_ent = Entry(root)
        self.email_ent.place(x=200, y=150)
        self.id = Label(root, text="ID number:", bg="lime")
        self.id.place(x=100, y=200)
        self.id_ent = Entry(root)
        self.id_ent.place(x=200, y=200)
        self.verify = Button(root, text="Verify", bg="lightyellow", borderwidth=2, command=self.verify)
        self.verify.place(x=100, y=300)
        self.exit = Button(root, text="Exit", bg="lightyellow", borderwidth=2, command=self.exit)
        self.exit.place(x=300, y=300)
        self.clear = Button(root, text="Clear", bg="lightyellow", borderwidth=2, command=self.clear)
        self.clear.place(x=200, y=300)

    def verify(self):
        name = self.name_ent.get()
        email = self.email_ent.get()
        id =self.id_ent.get()

        if len(id) != 13:
            messagebox.showerror("Error", "Please enter correct ID number")

        elif name == " ":
            messagebox.showerror("Error", "Enter correct details")

        elif email == " ":
            messagebox.showerror("Error", "Enter correct details")

        else:
            root.destroy()
            import main2

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                         icon='warning')
        if msg_box == "yes":
            root.destroy()
        else:
            messagebox.showinfo("Return", "You will now return to the App", icon="warning")

    def clear(self):
        self.name_ent.delete(0, END)
        self.email_ent.delete(0, END)
        self.id_ent.delete(0, END)


obj = Info(root)
root.mainloop()
