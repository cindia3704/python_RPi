import lcddriver
import RPi.GPIO as GPIO
import time

sensor = 4
led_pin = 8

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)     #경고에 대한 메세지를 얼마나 나타낼것이냐 (경고가 많이 안나옴)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(led_pin,GPIO.OUT)
print("Detect Ready...")
time.sleep(3)

p=GPIO.PWM(18,100)      # 전압의 세기를 바꾸는게 pwm
Frq=[263,294,330]   #도레미파솔라시
speed=0.5

#p.start(10)     #대기상태에 대한 pwm넣어줘야함 

display=lcddriver.lcd()

try:
    if GPIO.input(sensor) == 1:
        print("Detect!")            
        for i in range(0,10):
            GPIO.output(led_pin,1)
            time.sleep(0.1)
            i+=1
        display.lcd_display_string('Welcome!',1)
        display.lcd_display_string('To SMART HOME',1)
        p.start(10)
            # for fr in Frq:
            #     p.ChangeFrequency(fr)
            #     time.sleep(speed)
            # p.stop()    
        display.lcd_clear()
        time.sleep(1)
    if GPIO.input(sensor) == 0:
        #GPIO.output(led_pin,0)
        print('not detect')
        display.lcd_clear()
        time.sleep(1) 


except KeyboardInterrupt:
    print("GoodBye")
    display.lcd_clear()
    GPIO.cleanup
    p.stop()