import tkinter as tk
from tkinter import font

# Создайте основное окно
root = tk.Tk()
root.title("Лого")

# Создайте объект Canvas
canvas = tk.Canvas(root, width=300, height=200, bg="white")

# Нарисуйте имя "Ali" на Canvas
text_font = font.Font(family="Arial", size=40, weight="bold")
canvas.create_text(150, 100, text="Ali", font=text_font, fill="blue")

# Добавьте Canvas на главное окно
canvas.pack()

# Запустите главный цикл обработки событий
root.mainloop()
