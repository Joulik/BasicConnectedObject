# Control script - Run on computer
# coding: utf-8
import serial, time
import tkinter as tk
import serial.tools.list_ports

#get device comport could be any like COM3 COM13 ...
comport_test=[comport.device for comport in serial.tools.list_ports.comports()]
print(comport_test)
port=comport_test[0]
baud = 115200
sPort = serial.Serial(port) #open serial port
sPort.baudrate = baud

ListTemp = []

#request temperature value from port
def measurement_request():
    sPort.write(b'measurement')
    data = sPort.readline()
    print(data)
    #data = int(data[0:2])
    #temp_text = "{0}°C"
    #print(temp_text.format(data))
    #text_temperature.set(str(data))
    #text_temperature.set("Temperature: "+str(data))
    #print(str(data)+"°C") #alternative method
    #ListTemp.append(data)
    #print(ListTemp)
   
def quit():
    sPort.close()
    my_window.destroy()
 
# Main window
my_window = tk.Tk()
 
my_window.title("Title")
my_window.geometry("300x200")
 
# Button to get measurement
button_measurement = tk.Button(my_window, text="Start measurement", command=measurement_request)
button_measurement.grid(row=1, column=0, padx=5, pady=5)

# Label to display temperature value
data = tk.StringVar()
#text_temperature.set("Temperature:")
#label_temperature = tk.Label(my_window, textvariable=text_temperature , bg="grey")
label_temperature = tk.Label(my_window, textvariable=data , bg="grey")
label_temperature.grid(row=1, column=1, padx=5, pady=5)

# Exit button
button_exit = tk.Button(my_window, text="Exit", command=quit)
button_exit.grid(row=3,column=0, padx=5, pady=5)
 
my_window.mainloop()