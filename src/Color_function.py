import time
import smbus

class color_sensor():
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.bus.write_byte_data(0x29, 0x80, 0x03)
        self.bus.write_byte_data(0x29, 0x81, 0x00)
        self.bus.write_byte_data(0x29, 0x83, 0xFF)
        self.bus.write_byte_data(0x29, 0x8F, 0x00)
        self.data = self.bus.read_i2c_block_data(0x29, 0x94, 8)
        
    def get_value(self):
        cData = self.data[1] * 256 + self.data[0]
        return cData


if __name__ == "__main__":
    color = color_sensor()
    while True:
        data = color.get_value()
        print(data)
        time.sleep(0.1)
