from microbit import display, Image, sleep

while True:
    light = display.read_light_level()

    if light < 50:
        display.show(Image.HEART)
    else:
        display.clear()

    sleep(100)