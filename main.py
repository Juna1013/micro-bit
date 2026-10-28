from microbit import display, microphone, sleep

while True:
    # 音の大きさを読み取る（0~255）
    level = microphone.sound_level()

    # LEDの棒の高さに変換する（0~5段）
    height = min(5, level // 40)
    display.clear()

    # 下から順にLEDを点灯する
    for y in range(5 - height, 5):
        for x in range(5):
            display.set_pixel(x, y, 9)

    print(level)
    sleep(100)