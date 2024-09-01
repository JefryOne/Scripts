import pyautogui
import random
import string
import time
import keyboard

def generate_random_text(length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

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

    # Генерация случайного текста
    random_text = generate_random_text()

    # Написание текста в VS Code
    pyautogui.write(random_text, interval=0.1)

    # Задержка перед удалением текста
    time.sleep(2)

    # Удаление текста (Backspace по количеству символов в тексте)
    for _ in range(len(random_text)):
        pyautogui.press('backspace')

    # Задержка перед следующим циклом
    time.sleep(random.uniform(0.5, 1.5))

    # Перемещение к следующей строке
    current_line += 1

    # Если достигнута десятая строка, вернуться на первую строку
    if current_line >= 10:
        current_line = 0

            