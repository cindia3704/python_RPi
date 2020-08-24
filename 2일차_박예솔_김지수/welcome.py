import lcddriver
import RPi.GPIO as GPIO
import time

sensor = 4
led_pin = 8

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)     #경고에 대한 메세지를 얼마나 나타낼것이냐 (경고가 많이 안나옴)
GPIO.setup(sensor,GPIO.IN)
#GPIO.setup(18,GPIO.OUT)
GPIO.setup(led_pin,GPIO.OUT)
print("Detect Ready...")
time.sleep(3)

# p=GPIO.PWM(18,100)      # 전압의 세기를 바꾸는게 pwm
# Frq=[263,294,330]   #도레미파솔라시
# speed=0.5

#p.start(10)     #대기상태에 대한 pwm넣어줘야함 

display=lcddriver.lcd()

notHome=True
try:
    while notHome:
        if GPIO.input(sensor) == 1:
            notHome=False
            print("Detect!")
            display.lcd_display_string('Welcome to',1)
            display.lcd_display_string('SMART HOME',2)
            #p.start(10)
            for i in range(0,10):
                GPIO.output(led_pin,1)
                time.sleep(0.1)
                i+=1
            time.sleep(1)
        if GPIO.input(sensor) == 0:
            print('not detect')
            display.lcd_clear()
            time.sleep(1) 
            GPIO.output(led_pin,0)
            time.sleep(0.1)
    time.sleep(3) 
    display.lcd_clear()
    GPIO.output(led_pin,0)
    time.sleep(0.1)

except KeyboardInterrupt:
    print("GoodBye")
    display.lcd_clear()
    GPIO.cleanup
    #p.stop()