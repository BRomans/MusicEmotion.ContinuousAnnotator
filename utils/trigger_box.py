from serial import Serial, SerialException
import time


class TriggerBox(Serial):

    def __init__(self, serial_port, baudrate):
        super().__init__()
        self.port = serial_port
        self.baudrate = baudrate
        self.test_port()
        self.open()

    def test_port(self):
        try:
            self.open()
            print(self.port + " available")
            self.close()

        except SerialException:
            print(self.port + " NOT available")

    def test_available_ports(self):
        for ns in range(6):
            try:
                self.port = "COM" + str(ns + 1)
                self.open()
                print("COM" + str(ns + 1) + " available")
                self.close()

            except SerialException:
                print("COM" + str(ns + 1) + " NOT available")

    def write_trigger(self, trigger):
        print("Sending trigger: ", trigger)
        self.write(trigger.encode('utf-8'))

    def set_port(self, port):
        self.port = port

    def set_baudrate(self, baudrate):
        self.baudrate = baudrate




box = TriggerBox("COM9", 9600)
box.write_trigger('t')
time.sleep(1)
box.write_trigger('s')
time.sleep(1)
box.write_trigger('z')
time.sleep(1)
box.close()
