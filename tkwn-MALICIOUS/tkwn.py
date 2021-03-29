import tkinter as tk
def start():
    windows = []
    while True:
        windows.append(tk.Toplevel())
        root.update()
root = tk.Tk()
start()
root.mainloop()
