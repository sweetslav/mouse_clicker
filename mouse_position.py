import pyautogui
import time


def display_mouse_position():
    """
    Функция для отображения текущих координат мыши.
    """
    try:
        while True:
            x, y = pyautogui.position()
            print(f'Координаты мыши: X={x}, Y={y}', end='\r')
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('\nПрограмма завершена.')


if __name__ == "__main__":
    print('Нажмите Ctrl+C для завершения.')
    display_mouse_position()
