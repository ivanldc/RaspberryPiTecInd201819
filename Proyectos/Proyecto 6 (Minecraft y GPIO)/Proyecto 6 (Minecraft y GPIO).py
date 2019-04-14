from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_UP)

avanzar = 0

while True:

    estado_pulsador = GPIO.input(7)

    if estado_pulsador == 0:
        avanzar += 0.1
        while avanzar >= 0.5:
            x, y, z = mc.player.getTilePos()
            mc.player.setTilePos(x+1 ,y,z)
            avanzar = 0
            print("Avanza")
