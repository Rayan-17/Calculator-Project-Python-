import tkinter as tk

def click(event):
    global screen_value
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen_value.get())
            screen_value.set(result)
        except Exception as e:
            screen_value.set("Error")
    elif text == "C":
        screen_value.set("")
    else:
        screen_value.set(screen_value.get() + text)

# Create main application window
root = tk.Tk()
root.title("Calculator") 
root.geometry("300x400")

# Screen to display input and output
screen_value = tk.StringVar()
screen = tk.Entry(root, textvar=screen_value, font="Arial 20", bd=10, insertwidth=4, justify="right")
screen.pack(fill="both", ipadx=8)

# Buttons
buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", "=", "/"],
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)
    for button in row:
        b = tk.Button(frame, text=button, font="Arial 18", padx=10, pady=10)
        b.pack(side="left", fill="both", expand=True)
        b.bind("<Button-1>", click)

root.mainloop()
