# Automatic Plant Watering System

![Circuit](https://user-images.githubusercontent.com/90843436/198832746-de757784-c96c-4fa1-ac33-293d97efa5e6.png)
The aim of the project is, as the name suggests, to create an automatic plant watering sysytem. This is one of the classic microcontroller project ideas. You will find many such projects, and this is just one more.
And also by the way, please use capacitive soil moisture sensor, not resistive soil moisture sensor. Because they suck! They corrode, they are unstable and are also kind of toxic. And check out this [video](https://youtu.be/IGP38bz-K48) to make sure you have a good sensor.

## Requirements:-
  - RaspberryPi Pico (with micropython)
  - Capacitive Moisture sensor
  - 16x2 LCD display
  - Mini motor for pumping water (mini water pump)
  - 5k ohm resistor
  - NPN Transistor
  - Rectifier Diode
  - Some jumper wires
  + I have used breadboard power adapter with 12V input for both the Pico and the breadboard which powers the motor

## Usage:-
Flash the pico with the appropriate micropython file. Then use Thonny to put lcd_api.py, pico_12c_lcd.py and main.py into the Pico. Also, use sensor_calibration.py for calibration. I will explain it in the next section. Then use the image as a reference or us ethe schematic representation image to wire up the components. Make sure wires and components are fit and tight.
Get a beaker filled with water and put the motor in. For demonstaration purposes you can have two pots with dry and wet soil. Place the sensor inside different pots and watch the result. It will be displayed on the LCD display too. But if you want to _actually_ use it, use the no-lcd.py file instead of the main.py. Be sure to rename it as main.py and remove the original from the Pico. In this way, you can just plug it & leave it.

### Calibration:- For the calibration of the capacitive moisture sensor, run the sensor_calibration.py. Remember, the ADC value will be greater if the moisture is less and vice-versa. Run the code with the sensor in open air or in dry soil and note down the highest value and assign it to max_value in the main.py. Run the code again but eith the sensor in water. Be sure to keep the electronics out of the water. Now note down the lowest value and assign it to min_value in the main.py. Calibration complete!
