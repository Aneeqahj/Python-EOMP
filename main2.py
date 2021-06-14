from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Lotto Machine")
root.resizable("false", "false")
root.config(bg="lime")
root.geometry("800x400")


class Lotto:
    def __init__(self, root):
        self.details = Label(root, text="Enter any 6 numbers between 1 and 49:", bg="lime", font=("Arial", 15))
        self.details.place(x=100, y=20)
        self.player = Label(root, text="Player ID:", bg="lime")
        self.player.place(x=500, y=20)
        self.player_ent = Entry(root, bg="lime")
        self.player_ent.place(x=600, y=20)
        self.number1 = Entry(root, width=5)
        self.number1.place(x=100, y=100)
        self.number2 = Entry(root, width=5)
        self.number2.place(x=200, y=100)
        self.number3 = Entry(root, width=5)
        self.number3.place(x=300, y=100)
        self.number4 = Entry(root, width=5)
        self.number4.place(x=400, y=100)
        self.number5 = Entry(root, width=5)
        self.number5.place(x=500, y=100)
        self.number6 = Entry(root, width=5)
        self.number6.place(x=600, y=100)
        self.play = Button(root, text="Play", width=15, borderwidth=2, bg="lightyellow")
        self.play.place(x=300, y=150)
        self.results = Label(root, text="Results:", bg="lime", font=("Arial", 15))
        self.results.place(x=350, y=200)
        self.number7 = Entry(root, width=5)
        self.number7.place(x=100, y=250)
        self.number8 = Entry(root, width=5)
        self.number8.place(x=200, y=250)
        self.number9 = Entry(root, width=5)
        self.number9.place(x=300, y=250)
        self.number10 = Entry(root, width=5)
        self.number10.place(x=400, y=250)
        self.number11 = Entry(root, width=5)
        self.number11.place(x=500, y=250)
        self.number12 = Entry(root, width=5)
        self.number12.place(x=600, y=250)
        self.play_again = Button(root, text="Play again", bg="lightyellow", borderwidth=2)
        self.play_again.place(x=100, y=300)
        self.claim = Button(root, text="Claim Prize", bg="lightyellow", borderwidth=2)
        self.claim.place(x=350, y=300)
        self.exit = Button(root, text="Exit", bg="lightyellow", borderwidth=2, command=self.exit)
        self.exit.place(x=600, y=300)

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                         icon='warning')
        if msg_box == "yes":
            root.destroy()
        else:
            messagebox.showinfo("Return", "You will now return to the App", icon="warning")


obj = Lotto(root)
root.mainloop()
