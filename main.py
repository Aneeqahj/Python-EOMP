from tkinter import *  # Aneeqah Jones, Class 1
from tkinter import messagebox
from playsound import playsound
from datetime import *
import rsaidnumber
from validate_email import validate_email
from dateutil.relativedelta import relativedelta

root = Tk()
root.resizable("false", "false")
root.geometry("600x400")  # size of the window
root.config(bg="#835134")  # background colour of the window
root.title("Lotto Machine")  # Title of the window


class Info:  # created a class called info
    def __init__(self, root):  # defining all the details within the window
        self.details = Label(root, text="Fill in the details below:", bg="#835134", font=("Arial", 15))  # creating a
        # label
        self.details.place(x=220, y=20)  # placing the label
        self.name = Label(root, text="Name:", bg="#835134")
        self.name.place(x=100, y=100)
        self.name_ent = Entry(root)  # creating an entry box for for details to be entered
        self.name_ent.place(x=200, y=100)
        self.email = Label(root, text="Email:", bg="#835134")
        self.email.place(x=100, y=150)
        self.email_ent = Entry(root)
        self.email_ent.place(x=200, y=150)
        self.id = Label(root, text="ID number:", bg="#835134")
        self.id.place(x=100, y=200)
        self.id_ent = Entry(root)
        self.id_ent.place(x=200, y=200)
        self.verify = Button(root, text="Verify", bg="white", borderwidth=2, command=self.verify)  # creating a button
        # to verify information that was entered
        self.verify.place(x=100, y=300)
        self.exit = Button(root, text="Exit", bg="white", borderwidth=2, command=self.exit)
        self.exit.place(x=300, y=300)
        self.clear = Button(root, text="Clear", bg="white",
                            borderwidth=2, command=self.clear)
        self.clear.place(x=200, y=300)

    def add_to_file(self, text_to_add):  # defining a textfile to store details entered in on the first window
        import json

        text_to_add = json.dumps(text_to_add)

        with open("Database.txt", "a+") as database_file:
            database_file.write(text_to_add)

    def age(self, id):  # defining age for calculation
        today = date.today()
        dob = id.date_of_birth
        difference = relativedelta(today, dob)
        age = difference.years
        return age

    def verify(self): # defining verify button for first window's details

        name = self.name_ent.get()
        email = self.email_ent.get()
        id = self.id_ent.get()

        if name == " ": # creating if statements for incorrect details
            messagebox.showerror("Error", "Enter correct details")
        else:
            if email == " ":
                messagebox.showerror("Error", "Enter correct email")
            else:
                if not validate_email(email):
                    messagebox.showerror("Error", "Enter correct Email")
                else:
                    if len(id) != 13: # if the id is not 13 digits show an error
                        messagebox.showerror("Error", "Please enter correct ID number")

                    elif len(id) == 13: # if ID is 13 digits accept
                        id = rsaidnumber.parse(id)
                        id.valid

                        player_id = name[:3] + str(id)[:6] # creating a player id to save to the textfile, first 3
                        # letters of users name and fisrt 6 numbers of their id

                        self.age(id)
                        if int(self.age(id)) >= 18: # checking if the user is over 18 or not
                            player = { # details to save to the textfile
                                "name": name,
                                "email": email,
                                "id number": str(id),
                                "player id": player_id
                            }
                            self.add_to_file(player)
                            messagebox.showinfo("Yay!!", "Let's play") # if user is 18 or over they can play
                            playsound("correct answer sound effect free.mp3")
                            root.destroy() # once users age is checked and is over 18 this window will close and the
                            # second window will open
                            import main2

                        else:
                            messagebox.showerror("Error", "Too young, try again")

    def exit(self): # defining the exit button
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                         icon='warning')
        if msg_box == "yes":
            root.destroy()
        else:
            messagebox.showinfo("Return", "You will now return to the App", icon="warning")

    def clear(self):  # defining the clear button
        self.name_ent.delete(0, END)
        self.email_ent.delete(0, END)
        self.id_ent.delete(0, END)


obj = Info(root)
root.mainloop()
