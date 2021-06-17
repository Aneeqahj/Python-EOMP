from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Lotto Machine")
root.resizable("false", "false")
root.config(bg="#835134")
root.geometry("800x400")


class Lotto:
    def __init__(self, root):
        self.details = Label(root, text="Enter any 6 numbers between 1 and 49:", bg="#835134", font=("Arial", 15))
        self.details.place(x=100, y=20)
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
        self.play = Button(root, text="Play", width=15, borderwidth=2, bg="white", command=self.play)
        self.play.place(x=300, y=150)
        self.results = Label(root, text="Results:", bg="#835134", font=("Arial", 15))
        self.results.place(x=350, y=200)
        self.number7 = Entry(root, width=5, state="readonly")
        self.number7.place(x=100, y=250)
        self.number8 = Entry(root, width=5, state="readonly")
        self.number8.place(x=200, y=250)
        self.number9 = Entry(root, width=5, state="readonly")
        self.number9.place(x=300, y=250)
        self.number10 = Entry(root, width=5, state="readonly")
        self.number10.place(x=400, y=250)
        self.number11 = Entry(root, width=5, state="readonly")
        self.number11.place(x=500, y=250)
        self.number12 = Entry(root, width=5, state="readonly")
        self.number12.place(x=600, y=250)
        self.play_again = Button(root, text="Play again", bg="white", borderwidth=2, command=self.playAgain)
        self.play_again.place(x=100, y=300)
        self.claim = Button(root, text="Claim Prize", bg="white", borderwidth=2, command=self.claim)
        self.claim.place(x=350, y=300)
        self.exit = Button(root, text="Exit", bg="white", borderwidth=2, command=self.exit)
        self.exit.place(x=600, y=300)

    def play(self):
        import random
        numbers = []
        while len(numbers) < 6:
            num = random.randint(1, 49)
            if num not in numbers:
                numbers.append(num)
        # return lotto_list

        self.number7.config(state="normal")
        self.number8.config(state="normal")
        self.number9.config(state="normal")
        self.number10.config(state="normal")
        self.number11.config(state="normal")
        self.number12.config(state="normal")
        self.number7.delete(0, END)
        self.number8.delete(0, END)
        self.number9.delete(0, END)
        self.number10.delete(0, END)
        self.number11.delete(0, END)
        self.number12.delete(0, END)

        self.number7.config(state="normal")
        self.number7.insert(0, numbers[0])
        self.number8.config(state="normal")
        self.number8.insert(0, numbers[1])
        self.number9.config(state="normal")
        self.number9.insert(0, numbers[2])
        self.number10.config(state="normal")
        self.number10.insert(0, numbers[3])
        self.number11.config(state="normal")
        self.number11.insert(0, numbers[4])
        self.number12.config(state="normal")
        self.number12.insert(0, numbers[5])

        if self.number1.get() == "" or self.number2.get() == "" or self.number3.get() == "" or self.number4.get() == "" or self.number5.get() == "" or self.number6.get() == "":
            messagebox.showerror("Empty field", "Fill in all fields")
        else:
            numbers = set(numbers)
            entry_numbers = {int(self.number1.get()), int(self.number2.get()), int(self.number3.get()),
                             int(self.number4.get()), int(self.number5.get()), int(self.number6.get())}
            match = numbers.intersection(entry_numbers)
            win = len(match)
            if win == 2:
                messagebox.showinfo("YAY", "You win R20.00")
            elif win == 3:
                messagebox.showinfo("YAY", "You win R100.50")
            elif win == 4:
                messagebox.showinfo("YAY", "You win R2,384.00")
            elif win == 5:
                messagebox.showinfo("YAY", "You win R8,584.00")
            elif win == 6:
                messagebox.showinfo("YAY", "You win R10 000 000.00")
            else:
                messagebox.showinfo("Unlucky", "Try again")

    def claim(self):
        msg_box = messagebox.askquestion("Congratulations", "Are you sure you want to claim?")
        if msg_box == "yes":
            root.destroy()
            import main3
        else:
            messagebox.showinfo("Return", "You will now return")

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                         icon='warning')
        if msg_box == "yes":
            root.destroy()
        else:
            messagebox.showinfo("Return", "You will now return to the App", icon="warning")

    def playAgain(self):
        self.number1.delete(0, END)
        self.number2.delete(0, END)
        self.number3.delete(0, END)
        self.number4.delete(0, END)
        self.number5.delete(0, END)
        self.number6.delete(0, END)
        self.number7.delete(0, END)
        self.number8.delete(0, END)
        self.number9.delete(0, END)
        self.number10.delete(0, END)
        self.number11.delete(0, END)
        self.number12.delete(0, END)


obj = Lotto(root)
root.mainloop()
