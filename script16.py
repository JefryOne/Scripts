"""import pyautogui
import time

# Прокрутка вниз
pyautogui.scroll(-300)  # Прокрутка на 300 единиц вниз
time.sleep(1)

# Прокрутка вверх
pyautogui.scroll(500)  # Прокрутка на 300 единиц вверх
time.sleep(1)  # Пауза на 1 секунду """


import pyautogui
import time
import random

# Прокрутка вверх с рандомным значением
scroll_amount_up = random.randint(100, 500)  # Случайное значение от 100 до 500
pyautogui.scroll(scroll_amount_up)
time.sleep(1)  # Пауза на 1 секунду

# Прокрутка вниз с рандомным значением
scroll_amount_down = random.randint(100, 500) * -1  # Случайное значение от -100 до -500
pyautogui.scroll(scroll_amount_down)



        lambda: pyautogui.scroll(random.randint(100, 500)),  # Прокрутка вверх с рандомным значением
        lambda: time.sleep(1),  # Пауза на 1 секунду
        lambda: pyautogui.scroll(random.randint(100, 500) * -1),  # Прокрутка вниз с рандомным значением
        lambda: time.sleep(random.uniform(0.5, 1.5))