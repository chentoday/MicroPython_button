
# Document

- 前提准备：[第一次使用必看](https://github.com/aJantes/Initialize-the-board/blob/master/readme.md)
- 硬件介绍：[BPI:bit(ESP32)](https://github.com/aJantes/introduce-bpi-bit/blob/master/readme.md)
- 编程工具：[pycharm](https://github.com/aJantes/use-pycharm/blob/master/readme.md)

## 面板按键检测

首先，要知道两个概念， Output 输出是表示从设备输出到外围，Input 输入是处理设备过程中接受到的一些信息

那么在板子上最明显的输入便是二个按钮，灯板左右两个 A 和 B 按键，现在通过这两个按键学习面板按键检测
- [button_a.py](https://github.com/aJantes/to-control-the-button/blob/master/button_a.py)

## 处理事件

如果想要板子去响应一个按钮按压事件，那么就需要用 if 进行判断按钮是否按压，而且这个判断方法建议放在一个死循环中。


- [smile_button.py](https://github.com/aJantes/to-control-the-button/blob/master/smile_button.py)
