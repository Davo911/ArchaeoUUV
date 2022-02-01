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
    Voltage = leit.voltage

    #Convert voltage value to TDS value
    tdsValue=(133.42/Voltage*Voltage*Voltage - 255.86*Voltage*Voltage + 857.39*Voltage)*0.5;

    print("PH: " + str(ph.value), str(ph.voltage))
    print("Leit: " + str(tdsValue))
    print("Temp: " + str(temp.value), str(temp.voltage))
