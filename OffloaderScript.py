import serial
import time
import io
arduino = serial.Serial(timeout=1)
arduino.baudrate = 9600
arduino.port = "COM11"
time.sleep(2)
arduino.open()

while 1:
    arduino.write(str.encode(input("enter something to echo:")))
    arduino.flush()
    echo = arduino.readline()
    echo = str(echo).replace("b'", '').replace("'","")
    print(echo.strip())
