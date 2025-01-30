import pyautogui
import random
import time
import keyboard
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_random_python_code():
    code_snippets = [
        """import random\nfor _ in range(5):\n    print(random.randint(1, 100))""",
        """def greet(name):\n    return f'Hello, {name}!'\nnames = ['Alice', 'Bob', 'Charlie']\nfor name in names:\n    print(greet(name))""",
        """for i in range(5):\n    print(i)\nprint('Loop finished')""",
        """import math\nnumbers = [4, 9, 16, 25]\nfor num in numbers:\n    print(math.sqrt(num))""",
        """class Dog:\n    def __init__(self, name):\n        self.name = name\n    def bark(self):\n        print(f'{self.name} says woof!')\ndogs = [Dog('Rex'), Dog('Buddy')]\nfor dog in dogs:\n    dog.bark()""",
        """try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')\nfinally:\n    print('Execution finished')""",
        """with open('example.txt', 'w') as f:\n    f.write('Hello, file!')\nwith open('example.txt', 'r') as f:\n    print(f.read())""",
        """import os\nfiles = os.listdir('.')\nfor file in files:\n    print(file)""",
        """def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)\nprint(factorial(5))""",
        """import datetime\nnow = datetime.datetime.now()\nprint(now)\nprint(now.strftime('%Y-%m-%d %H:%M:%S'))"""
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

def is_within_editor_bounds(position, editor_bounds):
    x, y = position
    top_left, bottom_left, top_right, bottom_right = editor_bounds
    return (top_left[0] <= x <= bottom_right[0]) and (top_left[1] <= y <= bottom_right[1])

def perform_random_actions(editor_bounds, line_start_position, line_height):
    # Границы окна редактора
    editor_top_left, editor_bottom_left, editor_top_right, editor_bottom_right = editor_bounds

    # Генерация случайных координат в пределах окна редактора
    random_x = random.randint(editor_top_left[0], editor_bottom_right[0])
    random_y = random.randint(editor_top_left[1], editor_bottom_right[1])

    # Проверка, чтобы координаты не выходили за границы
    random_x = max(editor_top_left[0], min(random_x, editor_bottom_right[0]))
    random_y = max(editor_top_left[1], min(random_y, editor_bottom_right[1]))

    # Генерация случайного Python-кода
    random_code = generate_random_python_code()

    # Список действий
    actions = [
        lambda: human_like_mouse_move(random_x, random_y, 0.5),
        lambda: pyautogui.click() if is_within_editor_bounds((random_x, random_y), editor_bounds) else None,
        lambda: pyautogui.write(random_code, interval=0.1),
        lambda: time.sleep(2),
        lambda: [pyautogui.press('backspace') for _ in range(random.randint(1, len(random_code)))],
        lambda: pyautogui.scroll(random.randint(100, 500)),  # Прокрутка вверх с рандомным значением
        lambda: time.sleep(1),  # Пауза на 1 секунду
        lambda: pyautogui.scroll(random.randint(100, 500) * -1),  # Прокрутка вниз с рандомным значением
        lambda: time.sleep(random.uniform(0.5, 1.5))
    ]

    # Перемешивание списка действий
    random.shuffle(actions)

    # Выполнение действий в случайном порядке
    for action in actions:
        try:
            action_result = action()
            if action_result is not None:
                logging.info("Действие выполнено успешно.")
        except Exception as e:
            logging.error(f"Ошибка при выполнении действия: {e}")

# Флаг для завершения работы скрипта
should_stop = False

def stop_script(e):
    global should_stop
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('q'):
        logging.info("Скрипт остановлен пользователем.")
        should_stop = True

def main():
    # Длительность в секундах для выполнения скрипта (8 часов)
    duration = 8 * 60 * 60
    end_time = time.time() + duration

    # Настройте координаты начальной строки и высоту строки
    line_start_position = (399, 78)  # Пример координат, замените на ваши
    line_height = 20  # Высота строки в пикселях, настройте под ваш VS Code

    # Границы окна редактора
    editor_bounds = (
        (790, 164),  # editor_top_left
        (639, 974),  # editor_bottom_left
        (2724, 178),  # editor_top_right
        (2906, 1104)  # editor_bottom_right
    )

    # Регистрация горячей клавиши
    keyboard.on_press(stop_script)

    current_line = 0
    while time.time() < end_time:
        if should_stop:  # Нажмите 'Ctrl + Q' для выхода
            logging.info("Скрипт остановлен пользователем.")
            break

        # Проверка, находится ли курсор внутри границ редактора
        if not is_within_editor_bounds(pyautogui.position(), editor_bounds):
            logging.info("Курсор вышел за пределы редактора. Скрипт завершен.")
            break

        perform_random_actions(editor_bounds, line_start_position, line_height)

        # Перемещение к следующей строке
        current_line += 1
        # Если достигнута десятая строка, вернуться на первую строку
        if current_line >= 10:
            current_line = 0

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Скрипт завершен.")