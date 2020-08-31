#Transfer the code on the micro:bit chip through uFlash Antenna.py

from microbit import *
import utime
import radio

#temperature rescale after calibration
def rescaleTemp(temp):
    T_actual = 0.888*temp - 0.635
    return round(T_actual)

emptySign = Image('00000:'
                '00000:'
                '00000:'
                '00000:'
                '00000')

#Switch radio on
radio.on()
display.scroll("ON")

while True:
    messageIn = radio.receive()
    if messageIn == "MEASURE":
        tempActual = rescaleTemp(temperature())
        lightLevel = display.read_light_level()
        messageOut = str(tempActual) + ',' + str(lightLevel)
        radio.send(messageOut)
        for loop in range(3):
            display.show(Image.ARROW_N)
            utime.sleep_ms(125)
            display.show(emptySign)
            utime.sleep_ms(125)