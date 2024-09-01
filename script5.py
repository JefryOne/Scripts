import pyautogui
import random
import string
import time
import keyboard

def generate_random_text(length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

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
    pyautogui.moveTo(line_start_position[0], line_start_position[1] + current_line * line_height)
    pyautogui.click()

    # Задержка для обеспечения того, что курсор находится в нужной строке
    time.sleep(0.5)

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
    time.sleep(2)

    # Перемещение к следующей строке
    current_line += 1

    # Если достигнута сотая строка, вернуться на первую строку
    if current_line >= 100:
        current_line = 0