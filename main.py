from tkinter import *  # Aneeqah Jones, Class 1
from tkinter import messagebox
from playsound import playsound
from datetime import *
import rsaidnumber
from validate_email import validate_email
from dateutil.relativedelta import relativedelta
import uuid

root = Tk()
root.resizable("false", "false")
root.geometry("600x400")
root.config(bg="#835134")
root.title("Lotto Machine")


class Info:
    def __init__(self, root):
        self.details = Label(root, text="Fill in the details below:", bg="#835134", font=("Arial", 15))
        self.details.place(x=220, y=20)
        self.name = Label(root, text="Name:", bg="#835134")
        self.name.place(x=100, y=100)
        self.name_ent = Entry(root)
        self.name_ent.place(x=200, y=100)
        self.email = Label(root, text="Email:", bg="#835134")
        self.email.place(x=100, y=150)
        self.email_ent = Entry(root)
        self.email_ent.place(x=200, y=150)
        self.id = Label(root, text="ID number:", bg="#835134")
        self.id.place(x=100, y=200)
        self.id_ent = Entry(root)
        self.id_ent.place(x=200, y=200)
        self.verify = Button(root, text="Verify", bg="#CB9B7C", borderwidth=2, command=self.verify)
        self.verify.place(x=100, y=300)
        self.exit = Button(root, text="Exit", bg="#CB9B7C", borderwidth=2, command=self.exit)
        self.exit.place(x=300, y=300)
        self.clear = Button(root, text="Clear", bg="#CB9B7C", borderwidth=2, command=self.clear)
        self.clear.place(x=200, y=300)

    def add_to_file(self, text_to_add):
        import json

        text_to_add = json.dumps(text_to_add)

        with open("Database.txt", "a+") as database_file:
            database_file.write(text_to_add)

    def age(self, id):
        today = date.today()
        dob = id.date_of_birth
        difference = relativedelta(today, dob)
        age = difference.years
        return age

    def verify(self):

        name = self.name_ent.get()
        email = self.email_ent.get()
        id = self.id_ent.get()

        if name == " ":
            messagebox.showerror("Error", "Enter correct details")
        else:
            if email == " ":
                messagebox.showerror("Error", "Enter correct email")
            else:
                if not validate_email(email):
                    messagebox.showerror("Error", "Enter correct Email")
                else:
                    if len(id) != 13:
                        messagebox.showerror("Error", "Please enter correct ID number")
                    elif len(id) == 13:
                        id = rsaidnumber.parse(id)
                        id.valid

                        self.age(id)
                        if int(self.age(id)) >= 18:
                            player = {
                                "name": name,
                                "email": email,
                                "id number": str(id)
                            }
                            self.add_to_file(player)
                            messagebox.showinfo("Yay!!", "Let's play")
                            playsound("correct answer sound effect free.mp3")
                            root.destroy()
                            import main2

                        else:
                            messagebox.showerror("Error", "Too young, try again")

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
