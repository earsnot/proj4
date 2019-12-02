import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
from machine import i2c

# setting up as slave
slave = I2C('X', freq=400000)
slave.init()

# testing
def choose_mode(mode):
    if mode == 0:
        print('is eco')
    if mode == 1:
        print('is normal')
    if mode == 2:
        print('is sport')

BUTTON_W = 25
BUTTON_H = int(BUTTON_W/2)

m = ThemedTk(className="Start Screen", theme="xpnative")
m.geometry('480x360')

rows = 0
while rows < 50:
    m.rowconfigure(rows, weight=1)
    m.columnconfigure(rows, weight=1)
    rows += 1

nb = ttk.Notebook(m)
nb.grid(row=1, column=0, columnspan='50', rowspan='49', sticky='NESW')

hometab = ttk.Frame(nb)
nb.add(hometab, text='Home')

measurement_tab = ttk.Frame(nb)
nb.add(measurement_tab, text='Measurements')
# displaying SOC

soc = 50
soc_label = ttk.Label(hometab, text=soc)
soc_label.pack()

ttk.Button

# buttons for choosing mode

b1 = ttk.Button(hometab, text='Eco mode', font=h1, command=lambda : choose_mode(0))
b1.pack(anchor='nw', padx=3, pady=2)

b2 = ttk.Button(hometab, text='Normal mode', command=lambda: choose_mode(1))
b2.pack(anchor='nw', padx=3, pady=2)

b3 = ttk.Button(hometab, text='Sport mode', command=lambda: choose_mode(2))
b3.pack(anchor='nw', padx=3, pady=2)

q_butt = tk.PhotoImage(file=r"C:\dev\proj4\gui\modules\resized.png")
lol_butt = tk.PhotoImage(file=r"C:\dev\proj4\gui\modules\lol.png")

quit_button = ttk.Button(hometab, text='Closes application', command=lambda: m.destroy(), image=q_butt)
quit_button.pack(anchor='se', padx=3, pady=3, side="bottom")

lol_button = ttk.Button(hometab, text='Closes application', command=lambda: m.destroy(), image=lol_butt)
lol_button.pack(anchor='n', padx=3, pady=3, side="top")

m.mainloop()

slave.readfrom(master, 8, stop=True)