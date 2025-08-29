import tkinter as t
import random as r

def p(c):
    o=["Rock", "Paper", "Scissors"]
    d=r.choice(o)
    l1.config(text=f"Your Choice: {c}")
    l2.config(text=f"Computer's Choice: {d}")
    if c==d:
        v.set("It's a Tie!")
    elif (c=="Rock" and d=="Scissors") or (c=="Paper" and d=="Rock") or (c=="Scissors" and d=="Paper"):
        v.set("You Win! 🎉")
    else:
        v.set("Computer Wins! 💻")

w=t.Tk()
w.title("Rock Paper Scissors")
w.geometry("400x300")
w.resizable(False, False)

h=t.Label(w, text="Rock, Paper, Scissors", font=("Arial", 16, "bold"))
h.pack(pady=10)

f=t.Frame(w)
f.pack(pady=10)

b1=t.Button(f, text="Rock", width=12, command=lambda: p("Rock"))
b1.grid(row=0, column=0, padx=5)

b2=t.Button(f, text="Paper", width=12, command=lambda: p("Paper"))
b2.grid(row=0, column=1, padx=5)

b3=t.Button(f, text="Scissors", width=12, command=lambda: p("Scissors"))
b3.grid(row=0, column=2, padx=5)

l1=t.Label(w, text="Your Choice: None", font=("Arial", 12))
l1.pack(pady=5)

l2=t.Label(w, text="Computer's Choice: None", font=("Arial", 12))
l2.pack(pady=5)

v=t.StringVar()
l3=t.Label(w, textvariable=v, font=("Arial", 14, "bold"), fg="blue")
l3.pack(pady=10)

b4=t.Button(w, text="Exit", width=10, command=w.destroy)
b4.pack(pady=10)

w.mainloop()
