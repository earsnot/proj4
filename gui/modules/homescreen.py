import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

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

m = ThemedTk(className="Start Screen", theme="equilux")
m.geometry('800x600')

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

b1 = tk.Button(hometab, text='Eco mode', command=lambda : choose_mode(0))
b1.pack(anchor='nw', padx=3, pady=2)
b2 = tk.Button(hometab, text='Normal mode', command=lambda: choose_mode(1))
b2.pack(anchor='nw', padx=3, pady=2)
b3 = tk.Button(hometab, text='Sport mode', command=lambda: choose_mode(2))
b3.pack(anchor='nw', padx=3, pady=2)
print(b1.pack_info())
m.mainloop()

