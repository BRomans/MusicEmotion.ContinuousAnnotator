import serial
ser = serial.Serial()

for ns in range(6):
    try:
        ser.port = "COM" + str(ns+1)
        ser.open()
        print("COM" + str(ns+1) + " available")
        ser.close()

    except serial.SerialException:
        print("COM" + str(ns+1) + " NOT available")