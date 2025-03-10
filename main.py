import tkinter as tk

root = tk.Tk()
root.title("Alex's API Application")
root.config(bg="darkblue")
root.minsize(200, 200)
root.maxsize(300, 300)
root.geometry("250x250+50+50")

def test():
    print('the button worked, good job (thanks for all your credit card info)')

levin = tk.Label(root, text="levin is sigma")
levin.pack()

gullible = tk.Label(root, text="Look under me")
gullible.pack()

test = tk.Button(root, text="click here for 100% on ASE", command=test)
test.pack()

tk.Label(root, text="Enter your input:").pack(anchor="w", padx=75)
API_input = tk.Entry(root)
API_input.pack()

root.mainloop()