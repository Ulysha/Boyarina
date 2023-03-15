import RPi.GPIO as gpio
import sys

dac=[2, 22]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
p = gpio.PWM(2, 1000)

try:
    while (True):
        duty_cycle = input()
        if duty_cycle == 'q':
            break;
        duty_cycle = int(duty_cycle)
        p.start(duty_cycle)
        

finally:
    p.stop()
    gpio.output(dac, 0)
    gpio.cleanup(dac)