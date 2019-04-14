import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)


while True:
    input_state = GPIO.input(24)
    if input_state == False:
        print('Botón pulsado')
        GPIO.output(7, True)     
    if input_state == True:
        print('Botón  NO pulsado')
        GPIO.output(7, False)

