# PythonBasicConnectedObject

Two BBC micro:bit boards are involved; one that plays the role of probe that collects temperature and light level data and the other that plays the role of the antenna, which communicates between computer and probe.

Three codes are involved:
1. Control.py whose role is to send requests for measurement and store the collected data in a CSV file.
2. Antenna.py, which should be transferred on the antenna micro:bit board. Its role is to communicate bewteen probe and computer.
3. Probe.py, which should be transferred on the probe micro:bit board. Its role is to perform measurement and send them to the antenna.

The antenna micro:bit board is plugged to the computer through a USB port. The probe micro:bit board has a power supply so it can be moved around freely.

Probe.py and Antenna.py are transferred to the respective micro:bit through uFlash Probe.py and uFlash Antenna.py in the python shell.

Control.py sends requests to antenna, which in turn sends requests to probe. Probe performs measurements and sends the data to antenna, which communicates it to Control.py.

![principle image](https://raw.githubusercontent.com/Joulik/BasicConnectedObject/dfd940bf1be9d92dfdb97ed11df002be13d3eef1/Principle.jpg)

