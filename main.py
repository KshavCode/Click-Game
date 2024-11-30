import tkinter as tk
import random

root = tk.Tk()
root.geometry("550x550")
root.title("Click Game")
root.resizable(False, False)

score = 0
timer = 0
pause_game = False

def change():
    global score
    score += 1
    label1.config(text=f"Score : {score}")
    clickButton.place(x=random.randint(20, 450), y=random.randint(20, 450))

def update_timer():
    global timer, pause_game
    if not pause_game:
        timer += 1
        label2.config(text=f"Time : {timer}")
        root.after(1000, update_timer)

def key_press(e):
    global pause_game
    if not pause_game:
        pause_game = True
        clickButton.config(state="disabled")
        open_input_window()

def open_input_window():
    win = tk.Toplevel(root)
    win.geometry("400x100")
    win.title("Submit Score")
    win.resizable(False, False)

    def submit():
        username = entry1.get()
        print(f"{username} scored {score} in {timer} seconds.")
        win.destroy()

    label3 = tk.Label(win, text="Username :", font="Arial 13")
    entry1 = tk.Entry(win, font="Arial 13 bold", width=20)
    button1 = tk.Button(win, text="Submit", font="Arial 13 bold", bg="lightblue", command=submit)

    label3.place(x=10, y=10)
    entry1.place(x=110, y=10)
    button1.place(x=10, y=50)

label1 = tk.Label(root, text="Score : 0", font="Verdana 16")
label2 = tk.Label(root, text="Time : 0", font="Verdana 16")
clickButton = tk.Button(root, text="Click Me!", font="Garamond 13 bold", width=10, bg="lightgreen", command=change)

label1.place(x=200, y=5)
label2.place(x=200, y=35)   
clickButton.place(x=random.randint(70, 400), y=random.randint(70, 400))

root.after(1000, update_timer)
root.bind("<KeyPress>", key_press)

root.mainloop()
