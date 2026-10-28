from microbit import display, compass, Image, button_a, sleep

# 方位センサーを校正する
compass.calibrate()
sleep(500)

while True:
    # Aボタンで校正をやり直す
    if button_a.was_pressed():
        compass.calibrate()
        sleep(500)

    # 方位から、北を指す時計の針を選ぶ
    heading = compass.heading()
    needle = ((15 - heading) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])

    sleep(100)