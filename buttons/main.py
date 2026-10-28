from microbit import display, Image, button_a, button_b, sleep

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.SAD)
    else:
        display.show(Image.HEART)

    sleep(20)