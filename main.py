from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from machine import ADC, Pin, I2C
import utime
##############################################################################
soil = ADC(Pin(26)) #Sensor pin
motor = Pin(21, Pin.OUT) #Motor pin(connected to the middle pin of transistor)
min_value=28650 #min value obtained during calibration
max_value=45550 #max value obtained during calibration
LED = Pin(25, Pin.OUT) #Onboard LED
#----------------------------------------------------------------------------#
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000) #Pin(0) is connected to SDA and Pin(1) is connected to SCL of LCD
try: #sometimes, there will be a loose connection of LCD pins. If that happens, the LED will turn on and you can fix it
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
except:
    LED.value(1)
    utime.sleep(1)
    LED.value(0)   
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
        motor_stat = "ON"
    else:
        motor.value(0)
        motor_stat = "OFF"
    #------------------------------------------------------------------------#
    lcd.clear() #clears the screen, prints percentage and motor status on the screen
    lcd.move_to(0,0)
    lcd.putstr(f"Moist %: {percent}%")
    lcd.move_to(0,1)
    lcd.putstr(f"Motor stat: {motor_stat}")
    #------------------------------------------------------------------------#
    utime.sleep(3) #Refresh rate, increse for faster readings and vice-versa
