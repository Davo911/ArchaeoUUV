import board
import busio
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

ph = AnalogIn(ads, ADS.P0)
leit = AnalogIn(ads, ADS.P1)
temp = AnalogIn(ads, ADS.P2)

while(True):
    time.sleep(1)
    print("PH: " + str(ph.value), str(ph.voltage))
    print("Leit: " + str(leit.value), str(leit.voltage))
    print("Temp: " + str(temp.value), str(temp.voltage))
