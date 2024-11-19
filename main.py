import tkinter as tk
from tkinter import ttk


# Создание окна
root = tk.Tk()
root.title("Конвертер единиц")
root.geometry("300x400")

# Создание надписи над полем
tk.Label(root, text="Введите значение:").pack()

# Создание поля для значения
entry_value = tk.Entry(root)
entry_value.pack()

# Создание двух выпадающих списков
tk.Label(root, text="Из:").pack(pady=(20, 0))
combo_from = ttk.Combobox(root)
combo_from.pack()

tk.Label(root, text="В:").pack(pady=(20, 0))
combo_in = ttk.Combobox(root)
combo_in.pack()

# Создание кнопки
button = tk.Button(root, text="Конвертировать", font=30)
button.pack(pady=(20, 0))

# Создание финальной строки
result_label = tk.Label(root, text="Результат:")
result_label.pack(pady=(20, 0))

# Запуск приложения
root.mainloop()
