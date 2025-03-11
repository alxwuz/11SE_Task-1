import tkinter as tk

root = tk.Tk()
root.title("Alex's API")
root.config(bg="lightblue")
root.minsize(200, 200)
root.maxsize(300, 300)
root.geometry("250x250+50+50")

welcome = tk.Label(
    text="Welcome to my API Application",
    background="lightblue"
)
welcome.pack()

enter_city = tk.Label(
    text="Enter your chosen city:", 
    background="lightblue"
)
enter_city.pack()

input = tk.Text(
    font="Helvetica",
    height="1",
    width="20"
)
input.pack()

submit_input = tk.Button(
    text="Get Results",
)
submit_input.pack()

root.mainloop()