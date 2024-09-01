import pyautogui
import random
import string
import time

# Функция для генерации случайного текста
def generate_random_text(length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

# Длительность в секундах для выполнения скрипта (8 часов)
duration = 8 * 60 * 60
end_time = time.time() + duration

while time.time() < end_time:
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
    time.sleep
