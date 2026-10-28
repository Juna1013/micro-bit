from microbit import display, accelerometer, sleep

while True:
    tilt = accelerometer.get_x()
    x = max(0, min(4, 2 + tilt // 100))

    display.clear()
    display.set_pixel(x, 2, 9)
    sleep(50)