import RPi.GPIO as GPIO
import time

led_pin = 8

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)     #경고에 대한 메세지를 얼마나 나타낼것이냐 (경고가 많이 안나옴)
GPIO.setup(led_pin,GPIO.OUT)

for i in range(10):
    GPIO.output(led_pin,1)
    time.sleep(0.1)
    GPIO.output(led_pin,0)
    time.sleep(0.1)

GPIO.cleanup