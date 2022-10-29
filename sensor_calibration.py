from machine import ADC, Pin
import utime

soil = ADC(Pin(26)) #Sensor pin

min_value=0 #minimum value that can be put out by the sensor
max_value=65535 #maximum value that can be put out by the sensor

while True:
    print(str(soil.read_u16()) # print out the adc value
    utime.sleep(1)
    
    