import pyautogui
import random
import time

# Пример случайного движения мыши
for _ in range(10):
    x = random.randint(0, 1920)  # Замените на разрешение вашего экрана
    y = random.randint(0, 1080)
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 1))
    time.sleep(random.uniform(0.5, 2))
