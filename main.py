import tkinter as tk

# Создание окна
root = tk.Tk()
root.title("Конвертер единиц")
root.geometry("500x600")

# Создание кнопки
button = tk.Button(root, text="Конвертировать", font=30)
button.pack(side="bottom", pady=60)

# Запуск приложения
root.mainloop()
