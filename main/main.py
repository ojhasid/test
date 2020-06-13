import machine

def start():
    print("Led blinking with 2s delay")
    
    while(1):
        led = machine.Pin(2, Pin.OUT)
        led.high()
        sleep(1)
        led.low()
        sleep(1)
    
