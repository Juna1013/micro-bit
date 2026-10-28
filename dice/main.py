from microbit import display, accelerometer, sleep
import random

# 振るまでは「-」を表示
display.show("-")

while True:
    if accelerometer.was_gesture("shake"):
        # 一瞬消して、振り直したことが分かるようにする
        display.clear()
        sleep(150)

        # 1~6からランダムに選んで表示
        number = random.randint(1, 6)
        display.show(str(number))

        sleep(500)

    sleep(20)