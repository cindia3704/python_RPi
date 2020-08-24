from flask import Flask, request
from flask import render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

LED_PIN = 8
SERVO_PIN = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

p=GPIO.PWM(18,100)
Frq=[263,294,330] 
speed=0.5

servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)

@app.route("/")
def hello():
    return render_template("index.html")
    return "SMART HOME"

@app.route("/led/on")
def led_on():
    try:
        GPIO.output(LED_PIN, 1)
        return "ok"
    except expression as identifier:
        return "fail"

@app.route("/led/off")
def led_off():
    try:
        GPIO.output(LED_PIN, 0)
        return "ok"
    except expression as identifier:
        return "fail"

@app.route("/window/on")
def window_on():
    try:
        p.start(10) 
        for fr in Frq:
            p.ChangeFrequency(fr)
            time.sleep(speed)
        servo.ChangeDutyCycle(12.5) #180
        p.stop()
        return "ok"
    except expression as identifier:
        return "fail"

@app.route("/window/off")
def window_off():
    try:
        servo.ChangeDutyCycle(7.5) #180
        return "ok"
    except expression as identifier:
        return "fail"

@app.route("/gpio/cleanup")
def gpio_cleanup():
    servo.stop()
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
    return "GPIO CLEAN UP"

if __name__ == "__main__":
    app.run(host="192.168.0.8") # local host