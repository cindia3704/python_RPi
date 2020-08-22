# 박예솔, 김지수
# 1일차 과제 1번
# 동작감지센서와 LED를 이용하여 동작 감지 제작

import RPi.GPIO as GPIO
import time

sensor = 4
led_pin = 8

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)     #경고에 대한 메세지를 얼마나 나타낼것이냐 (경고가 많이 안나옴)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(led_pin,GPIO.OUT)

print("Detect Ready...")
time.sleep(3)

try:
    while True:
        if GPIO.input(sensor) == 1:
            print("Detect!")
            GPIO.output(led_pin,1)
            time.sleep(1)
        if GPIO.input(sensor) == 0:
            GPIO.output(led_pin,0)
            time.sleep(0.2)         

except KeyboardInterrupt:
    print("STOP BY USER")
    GPIO.output(led_pin,0)
    GPIO.cleanup