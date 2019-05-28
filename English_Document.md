
# MircoPython - button
#### 📖 [English document](https://github.com/aJantes/MircoPython-button/blob/master/README.md)
![](album/bit.gif)
> Hardware introduction：[BPI:bit(ESP32)](https://github.com/aJantes/introduce-bpi-bit/blob/master/README.md)

# Keystroke detection

The purpose is achieved through the Output output and Input input of keys.


## **Key State Recognition**

Button hardware correlation function [button modular](https://github.com/aJantes/MircoPython-button/blob/master/source/button.py).Before calling related functions, you need to import the corresponding libraries.

## Main functions

1. `button_a.get_presses()`:

For example： `display.scroll(str(button_a.get_presses()))`  Gets the number of times the key A is pressed and passes it to `display.sroll`.

2. `button_a.is_pressed()`:

Used to determine whether key A is pressed or not.

---
## button Example
- [button_a.py](https://github.com/aJantes/MircoPython-button/blob/master/example/button_a.py)    - Judge key A press next number
- [smile_button.py](https://github.com/aJantes/MircoPython-button/blob/master/example/smile_button.py)    - Determine whether key A is pressed to display the image
