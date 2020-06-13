from machine import Pin
import time
import usocket
import os
import gc
import machine

def start():
    
    print("Starting program 1s delay")
    led = Pin(2,Pin.OUT)

    while(1):
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)

start()
