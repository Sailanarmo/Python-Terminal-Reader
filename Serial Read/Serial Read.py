import serial, time

satData = open("satData.txt", "w")
arduino = serial.Serial('COM6', 9600, timeout=.1)
time.sleep(1)



data = 'o'
while True:
    data = arduino.readline()
    print data.rstrip('\n')
    satData.write(data)

satData.close()