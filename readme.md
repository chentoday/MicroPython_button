
# MircoPython - button
#### 📖 [English document](https://github.com/aJantes/MircoPython-button/blob/master/English_Document.md)
![](album/bit.gif)
> 硬件介绍：[BPI:bit(ESP32)](https://github.com/aJantes/introduce-bpi-bit/blob/master/README.md)

# 按键检测

通过按键的 Output 输出和 Input 输入实现目的。


## **按键状态识别**

button 硬件相关函数 [button 模块](https://github.com/aJantes/MircoPython-button/blob/master/source/button.py)。在调用相关函数前，需要先导入对应的库。

## 主要函数

1. `button_a.get_presses()`:

例如： `display.scroll(str(button_a.get_presses()))`  获取按键 A 按下的次数，并将其传递到 `display.sroll` 中。

2. `button_a.is_pressed()`:

用于判断按键 A 是否被按下

---
## button例子
- [button_a.py](https://github.com/aJantes/MircoPython-button/blob/master/example/button_a.py)    - 判断按键 A 按下次数
- [smile_button.py](https://github.com/aJantes/MircoPython-button/blob/master/example/smile_button.py)    - 判断按键 A 是否被按下，从而显示图像
