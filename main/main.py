from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
print('Should do something')
while True:
  led.value(not led.value())
  sleep(0.5)
