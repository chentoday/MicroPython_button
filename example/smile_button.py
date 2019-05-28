from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        display.clear()


# 此时可以按下按键 A 显示一张笑脸