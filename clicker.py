import pyautogui
import time


def click_mouse(x, y, clicks, interval=0.1):
    """
    Функция для клика по координатам x, y заданное количество раз с интервалом.

    :param x: Координата X для клика
    :param y: Координата Y для клика
    :param clicks: Количество кликов
    :param interval: Интервал между кликами (по умолчанию 0.1 секунды)
    """
    for _ in range(clicks):
        pyautogui.click(x, y)
        time.sleep(interval)


if __name__ == "__main__":
    # Задание координат и количества кликов
    x = 1063  # Координата X
    y = 592  # Координата Y
    clicks = 1000000  # Количество кликов
    interval = 0.001  # Интервал между кликами в секундах

    # Задержка перед началом выполнения скрипта (чтобы успеть перейти в нужное место)
    print("Скрипт начнет работу через 5 секунд...")
    time.sleep(5)

    # Выполнение кликов
    click_mouse(x, y, clicks, interval)

    print("Клики завершены.")
