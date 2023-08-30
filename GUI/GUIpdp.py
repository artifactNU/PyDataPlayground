import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import tkinter as tk
import numpy as np

def plot():
    ax.clear()
    x = np.random.randint(0, 100, 100)
    y = np.random.randint(0, 100, 100)
    ax.scatter(x, y) #.plot(x, y) for line plot
    canvas.draw()

# Initialize Tkinter
root = tk.Tk()
fig, ax = plt.subplots()

# Tkinter Application
frame = tk.Frame(root)
label = tk.Label(master=frame, text="Hello World!")
label.config(font=("Courier", 32))
label.pack()

canvas = FigureCanvasTkAgg(fig, master = frame)
canvas.get_tk_widget().pack()

toolbar = NavigationToolbar2Tk(canvas, frame, pack_toolbar=False)
toolbar.update()
toolbar.pack(anchor="w", fill="x")

frame.pack()

tk.Button(master=root, text="Plot", command=plot).pack()

root.mainloop()