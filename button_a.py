from microbit import *

while(True):
    sleep(2000)
    display.scroll(str(button_a.get_presses()))

# `sleep()`可以让板子暂停些许时间，暂停的时间为方块数字的毫秒
# `button_a` 对象允许你通过 `get_presses()` 获取一个时间内被按的次数
# `get_presses()` 获取到了值，将其传递到 display.sroll 中，这个方法只能接受字符型，所以需要通过 `str` 函数将**整型**转换成**字符串**
