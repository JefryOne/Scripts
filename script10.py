import pyautogui
import random
import time
import keyboard

def generate_random_python_code():
    code_snippets = [
        """import random
for _ in range(5):
    print(random.randint(1, 100))""",
        """def greet(name):
    return f'Hello, {name}!'
names = ['Alice', 'Bob', 'Charlie']
for name in names:
    print(greet(name))""",
        """for i in range(5):
    print(i)
print('Loop finished')""",
        """import math
numbers = [4, 9, 16, 25]
for num in numbers:
    print(math.sqrt(num))""",
        """class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f'{self.name} says woof!')
dogs = [Dog('Rex'), Dog('Buddy')]
for dog in dogs:
    dog.bark()""",
        """try:
    x = 1 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')
finally:
    print('Execution finished')""",
        """with open('example.txt', 'w') as f:
    f.write('Hello, file!')
with open('example.txt', 'r') as f:
    print(f.read())""",
        """import os
files = os.listdir('.')
for file in files:
    print(file)""",
        """def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))""",
        """import datetime
now = datetime.datetime.now()
print(now)
print(now.strftime('%Y-%m-%d %H:%M:%S'))"""
    ]
    return random.choice(code_snippets)

def human_like_mouse_move(x, y, duration):
    start_x, start_y = pyautogui.position()
    steps = int(duration * 100)
    
    for i in range(steps):
        current_x = start_x + (x - start_x) * (i / steps) + random.uniform(-1, 1)
        current_y = start_y + (y - start_y) * (i / steps) + random.uniform(-1, 1)
        pyautogui.moveTo(current_x, current_y)
        time.sleep(duration / steps)

# Длительность в секундах для выполнения скрипта (8 часов)
duration = 8 * 60 * 60
end_time = time.time() + duration

# Настройте координаты начальной строки и высоту строки
line_start_position = (399, 78)  # Пример координат, замените на ваши
line_height = 20  # Высота строки в пикселях, настройте под ваш VS Code

current_line = 0

while time.time() < end_time:
    if keyboard.is_pressed('q'):  # Нажмите 'q' для выхода
        print("Скрипт остановлен пользователем.")
        break

    # Переместить курсор на текущую строку и кликнуть
    human_like_mouse_move(line_start_position[0], line_start_position[1] + current_line * line_height, 0.5)
    pyautogui.click()

    # Генерация случайного Python-кода
    random_code = generate_random_python_code()

    # Написание кода в VS Code
    pyautogui.write(random_code, interval=0.1)

    # Задержка перед удалением кода
    time.sleep(2)

    # Удаление кода (Backspace по количеству символов в коде)
    for _ in range(len(random_code)):
        pyautogui.press('backspace')

    # Задержка перед следующим циклом
    time.sleep(random.uniform(0.5, 1.5))

    # Перемещение к следующей строке
    current_line += 1

    # Если достигнута десятая строка, вернуться на первую строку
    if current_line >= 10:
        current_line = 0
