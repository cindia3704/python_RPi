import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

DETECT = 5

SERVO_PIN = 12
TRGI = 23
ECHO = 24
print("Distance measurement with Ultrasonic")

GPIO.setup(TRGI, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# set servo strength
servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)

GPIO.output(TRGI, False)
print("Waiting for sensor to settle")
time.sleep(2)

try:
    while True:
        GPIO.output(TRGI, True)
        time.sleep(0.00001)
        GPIO.output(TRGI, False)
        while GPIO.input(ECHO) == 0:
            start = time.time()
        while GPIO.input(ECHO) == 1:
            stop = time.time()
        check_time = stop - start
        distance = check_time*34300/2
        print("Distance : %.1f cm" %distance)

        if distance < DETECT :
            servo.ChangeDutyCycle(7.5)  #90
            time.sleep(1)
            servo.ChangeDutyCycle(12.5) #180
            time.sleep(1)
        else:
            time.sleep(0.4)

except KeyboardInterrupt:
    print("Measuremenet stopped by User")
    servo.stop()
    GPIO.cleanup()