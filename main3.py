import json
import ssl
from tkinter import *
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

window = Tk()
window.title("Lotto Machine")  # window title
window.config(bg="#835134")  # window background
window.resizable("false", "false")  # so you cant make the window bigger
window.geometry("600x400")  # window size
variable = StringVar(window)  # for options menu


class Details:
    variable.set("Select")  # options menu

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
        self.enter = Button(root, text="Enter", bg="white", borderwidth=2, command=self.enter)
        self.enter.place(x=100, y=250)
        self.exit = Button(root, text="Exit", bg="white", borderwidth=2, command=self.exit)
        self.exit.place(x=500, y=250)
        self.con_lbl = Label(root, text="If you wish to convert to another currency, click the button below:",
                             bg="#835134", font=("Arial", 12))
        self.con_lbl.place(x=50, y=300)
        self.convert = Button(root, text="Convert", bg="white", borderwidth=2, width=10, command=self.convert)
        self.convert.place(x=250, y=350)

    def enter(self):
        acc = self.acc_ent.get()
        bank = self.bank_ent.get()
        with open("Database.txt", "r", encoding="utf-8-sig", errors="ignore") as file:  # to pull information from
            # textfile
            info = json.load(file, strict=False)
            print(info)

        try:
            num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
            if acc == "":
                raise ValueError
            elif acc in num_list:
                raise ValueError
            if bank == "":
                raise ValueError
            else:
                int(self.bank_ent.get())
                messagebox.showinfo("COOL!", "Details are correct")
            if variable.get() == "Select":
                raise ValueError
            else:
                self.email()
            # elif variable.get() == "FNB":
            #     messagebox.showinfo("COOL!", "Details are correct")
            # elif variable.get() == "Absa":
            #     messagebox.showinfo("COOL!", "Details are correct")
            # elif variable.get() == "Nedbank":
            #     messagebox.showinfo("COOL!", "Details are correct")
            # elif variable.get() == "Standard bank":
            #     messagebox.showinfo("COOL!", "Details are correct")
        except ValueError:
            messagebox.showerror("ERROR", "Enter all fields")

    def email(self):
        import json
        with open("Database.txt", "r", encoding="utf-8-sig", errors="ignore") as file:
            info = json.load(file, strict=False)
            name = info["name"]
            sender_email = "aneeqahlotto@gmail.com"
            receiver_email = info["email"]
            print(receiver_email)
            password = "lotto2021"

            message = MIMEMultipart("alternative")
            message["Subject"] = "Lotto Winner"
            message["From"] = sender_email
            message["To"] = ", ".join(receiver_email)

            email_message = "Hi " + name + " you have won " + " with lotto " + "it will be transferred to your bank " \
                                                                               "account" \
                            + " soon " + "\n" + "\n" + \
                            "Thanks for playing"
            text = MIMEText(email_message)
            message.attach(text)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())

    def convert(self):
        msg_box = messagebox.askquestion("Convert?", "You sure you want to covert?")
        if msg_box == "yes":
            window.destroy()
            import main4
        else:
            messagebox.showinfo("Return", "You will now return.")

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()
        else:
            messagebox.showinfo("Return", "You will now return to the App", icon="warning")


obj = Details(window)
window.mainloop()
