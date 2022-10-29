from machine import ADC, Pin
import utime
##############################################################################
soil = ADC(Pin(26)) #Sensor pin
motor = Pin(21, Pin.OUT) #Motor pin(connected to the middle pin of transistor)
min_value=28650 #min value obtained during calibration
max_value=45550 #max value obtained during calibration
LED = Pin(25, Pin.OUT) #Onboard LED
##############################################################################
while True:
    moisture = (max_value-soil.read_u16())*100/(max_value-min_value) #Reads value and converts it to percentage
    percent = str("%.1f" % moisture) #Removes some numbers to make the percentage have only 1 post-decimal digit
    if int(percent)>100: #Sometimes, the percentage will go above 100 or below 0. This will correct for it
        percent = "100.0"
    if int(percent)<0:
        percent = "0.0"
    #------------------------------------------------------------------------#
    print(f"Percentage: {percent}%    Value: {str(soil.read_u16())}") #Prints the percentage and ADC value
    #------------------------------------------------------------------------#
    if int(percent)<50: #Turns the motor on if the percentage is less that 50 and turns it off if above 50. Feel free to change the value
        motor.value(1)
    else:
        motor.value(0)
    #------------------------------------------------------------------------#
    utime.sleep(3) #Refresh rate, increse for faster readings and vice-versa
