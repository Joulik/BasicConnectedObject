#Transfer the code on the micro:bit chip through uFlash Antenna.py

from microbit import *
import radio
import utime

emptySign = Image('00000:'
                '00000:'
                '00000:'
                '00000:'
                '00000')

crossSign = Image('90009:'
               '09090:'
               '00900:'
               '09090:'
               '90009')

uart.init(baudrate=115200)
radio.on()

while True:
    if uart.any():
        msg_bytes = uart.read()
        if msg_bytes == b'measurement':
            radio.send("MEASURE")
            messageIn = radio.receive()
            if messageIn is None:
                messageIn='Null,Null'
                display.show(crossSign)
                utime.sleep_ms(500)
                display.show(emptySign)
                utime.sleep_ms(10)
                print(messageIn)
            else:
                for loop in range(3):
                    display.show(Image.ARROW_S)
                    utime.sleep_ms(125)
                    display.show(emptySign)
                    utime.sleep_ms(125)
                #display.scroll(messageIn)
                print(messageIn)
        else:
            if msg_bytes == b'11':
                display.set_pixel(1, 1, 9)
            else:
                msg_str = str(msg_bytes, 'UTF-8')
                display.scroll(msg_str)
    sleep(1000)

    