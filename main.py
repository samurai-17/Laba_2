import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def convert(value, from_unit, in_unit):
    """Функция конвертации, использует вложенные словари"""
    convertions = \
        {
            'length':
                {
                    'm': 1.0,
                    'cm': 100.0,
                    'mm': 1000.0,
                    'km': 0.001,
                },
            'mass':
                {
                    'kg': 1.0,
                    'g': 1000,
                    'mg': 10**6,
                }
        }

    for category, units in convertions.items():
        if from_unit in units and in_unit in units:
            return value * (units[in_unit] / units[from_unit])
    raise ValueError("Невозможно выполнить конвертацию, т.к. элементы относятся к разным категориям")


def performance():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        in_unit = combo_in.get()
        if not from_unit or not in_unit:
            raise ValueError("Выберите две единицы измерения")
        res = convert(value, from_unit, in_unit)
        result_label.config(text=f"Результат: {res} {in_unit}")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))


# Создание окна
root = tk.Tk()
root.title("Конвертер единиц")
root.geometry("250x350")

# Создание надписи над полем
tk.Label(root, text="Введите значение:").pack()

# Создание поля для значения
entry_value = tk.Entry(root)
entry_value.pack()

# Создание двух выпадающих списков
tk.Label(root, text="Из:").pack(pady=(20, 0))
combo_from = ttk.Combobox(root, values=['m', 'cm', 'mm', 'km', 'kg', 'g', 'mg'])
combo_from.pack()

tk.Label(root, text="В:").pack(pady=(20, 0))
combo_in = ttk.Combobox(root, values=['m', 'cm', 'mm', 'km', 'kg', 'g', 'mg'])
combo_in.pack()

# Создание кнопки
button = tk.Button(root, text="Конвертировать", font=30, command=performance)
button.pack(pady=(20, 0))

# Создание финальной строки
result_label = tk.Label(root, text="Результат:")
result_label.pack(pady=(20, 0))

# Запуск приложения
root.mainloop()
