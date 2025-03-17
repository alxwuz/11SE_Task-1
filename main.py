import tkinter as tk
from my_module import *

root = tk.Tk()
root.title("Alex's API")
root.config(bg="lightblue")
root.minsize(200, 200)
root.maxsize(300, 300)
root.geometry("250x250+50+50")

welcome = tk.Label(
    text="Alex's Weather Application",
    background="lightblue"
)
welcome.pack()

instructions = tk.Label(
    text="To user this, enter a city of your choice and press the submit button to get the info.", 
    background="lightblue"
)
instructions.pack()

input = tk.Entry(
)
input.pack()

submit_input = tk.Button(
    text="Get Results",
)
submit_input.pack()

root.mainloop()