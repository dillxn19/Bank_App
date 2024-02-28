import tkinter as tk

root = tk.Tk()

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame = tk.Frame(root, bg="blue")  

frame.grid(row=0, column=0, sticky="nsew")

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

button = tk.Button(frame, text="Click Me!")
button.grid(row=0, column=0, sticky="nsew")

root.mainloop()