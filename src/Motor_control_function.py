import pigpio

pi = pigpio.pi()

def mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def constrain(x, out_min, out_max):
    return out_min if x < out_min else out_max if x > out_max else x

class Motor_control():
    def __init__(self, FWD_pin, BWD_pin, EN_pin, Servo_pin):
        self.FWD_pin = FWD_pin
        self.BWD_pin = BWD_pin
        self.EN_pin = EN_pin
        self.Servo_pin = Servo_pin
        pi.set_mode(self.FWD_pin, pigpio.OUTPUT)
        pi.set_mode(self.BWD_pin, pigpio.OUTPUT)
        pi.set_mode(self.EN_pin, pigpio.OUTPUT)
        pi.set_mode(self.Servo_pin, pigpio.OUTPUT)
    def DC(self, power):
        if power == 0:
            pi.write(self.FWD_pin, pigpio.LOW)
            pi.write(self.BWD_pin, pigpio.LOW)
            pi.set_PWM_dutycycle(self.EN_pin, 0)
        elif power > 0:
            pi.write(self.FWD_pin, pigpio.HIGH)
            pi.write(self.BWD_pin, pigpio.LOW)
            pi.set_PWM_dutycycle(self.EN_pin, constrain(mapping(power, 0, 100, 0, 255), 0, 255))
        else:
            pi.write(self.FWD_pin, pigpio.LOW)
            pi.write(self.BWD_pin, pigpio.HIGH)
            value = mapping(abs(power), 0, 100, 0, 255)
            pi.set_PWM_dutycycle(self.EN_pin, constrain(mapping(abs(power), 0, 100, 0, 255), 0, 255))
    def Servo(self, turn_angle):
        self.angle = turn_angle+38
        duty = constrain(mapping(self.angle, 0, 180, 500, 2500), 500, 2500)
        pi.set_servo_pulsewidth(self.Servo_pin, duty)
    def ServoStop(self):
        pi.write(self.Servo_pin, pigpio.LOW)
        
if __name__ == "__main__":
    import time
    MotorRun = Motor_control(24, 23, 25, 12)
    MotorRun.Servo(35)
    time.sleep(2)
    MotorRun.ServoStop()
