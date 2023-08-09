import tkinter as tk
from tkinter import ttk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        history_text.insert(tk.END, f"{expression} = {result}\n")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Hata")

def clear_history():
    history_text.delete(1.0, tk.END)

# Hesap Makinesi Penceresi
calculator = tk.Tk()
calculator.title("Üst Düzey Hesap Makinesi")

# Girdi Alanı
entry = ttk.Entry(calculator, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

# Hesap Makinesi Tuşları
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2),
    ('-', 1, 3), ('*', 2, 3), ('/', 3, 3), ('=', 4, 3),
]

for (text, row, col) in buttons:
    button = ttk.Button(calculator, text=text, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, sticky="nsew")

# Temizle Butonu
clear_button = ttk.Button(calculator, text="C", command=button_clear)
clear_button.grid(row=5, column=0, columnspan=2, sticky="nsew")

# Hesapla Butonu
equal_button = ttk.Button(calculator, text="=", command=button_equal)
equal_button.grid(row=5, column=2, columnspan=2, sticky="nsew")

# Geçmiş İşlemler
history_label = tk.Label(calculator, text="Geçmiş İşlemler:")
history_label.grid(row=6, column=0, columnspan=4, sticky="w")

history_text = tk.Text(calculator, height=5, font=('Arial', 12))
history_text.grid(row=7, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

# Geçmişi Temizle Butonu
clear_history_button = ttk.Button(calculator, text="Geçmişi Temizle", command=clear_history)
clear_history_button.grid(row=8, column=0, columnspan=4, pady=5, sticky="nsew")

# Buton boyutlarını ayarla
for i in range(5):
    calculator.grid_rowconfigure(i, weight=1)
    calculator.grid_columnconfigure(i, weight=1)

# Tkinter penceresini başlat
calculator.mainloop()
