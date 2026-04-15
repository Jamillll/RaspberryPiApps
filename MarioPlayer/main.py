from machine import Pin
from time import sleep
from pitches import *

while True:
    button0 = Pin(20, Pin.IN)
    button1 = Pin(21, Pin.IN)
    button2 = Pin(22, Pin.IN)

    buzzer = machine.PWM(machine.Pin(18))
    mario = [E7, E7, 0, E7, 0, C7, E7, 0, G7, 0, 0, 0, G6, 0, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0, A6, 0, B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7, G7, 0, E7, 0,C7, D7, B6, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0, A6, 0, B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7, G7, 0, E7, 0,C7, D7, B6, 0, 0]

    # Infinite loop until power button is turned on
    while True:
        if button2.value() == 0:
            print("Powering On")
            for i in range(0, 12):
                Pin(i + 2, Pin.OUT).on()
                if abs(i * 400) != 0:
                    buzzer.freq(abs(i * 400))
                    buzzer.duty_u16(19660)
                sleep(0.1)
            buzzer.duty_u16(0)  
            break

    running = True
    playing = False
    note = 0
    while running:
        #Button to start music playing
        if button0.value() == 0:
            playing = not playing
        
        #Power Off button
        if button2.value() == 0:
            for i in range(11, -1, -1):
                Pin(i + 2, Pin.OUT).off()
                if abs(i * 400) != 0:
                    buzzer.freq(abs(i * 400))
                    buzzer.duty_u16(19660)
                sleep(0.1)
            buzzer.duty_u16(0)  
            print("Shutting Down")
            running = False
            playing = False
         
        #Music playing logic
        if playing:
            if note >= 79:
                note = 0
            else:
                note += 1
                
            frequencyLED = Pin(int(((mario[note] / 5000) * 10) + 2), Pin.OUT)
            if mario[note] == 0:
                buzzer.duty_u16(0)            # 0% duty cycle
            else:
                buzzer.freq(mario[note])                # set frequency (notes)
                buzzer.duty_u16(19660)        # 30% duty cycle
                frequencyLED.off()
            sleep(0.15)
            frequencyLED.on()
