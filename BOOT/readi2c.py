import board
import busio
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import numpy as np
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)


ph = AnalogIn(ads, ADS.P0)
leit = AnalogIn(ads, ADS.P1)
temp = AnalogIn(ads, ADS.P2)
tmpArr = []
counter = 0
temperature = 20

while(True):
    time.sleep(0.004)
    Voltage = leit.voltage
    # if 30 values collected 0,004*30 = 0,12s
    if(counter >= 30):
        # calulate stuff
        avgVolt = np.median(tmpArr)
        compensationCoefficient = 1.0 + 0.02 * (temperature - 25.0)
        compensationVolatge = avgVolt / compensationCoefficient;           
        tdsComp = (133.42 * compensationVolatge * compensationVolatge * compensationVolatge - 255.86 * compensationVolatge * compensationVolatge + 857.39 * compensationVolatge) * 0.5
        print("complicated tds: "+str(tdsComp))
        tmpArr.clear()

    tmpArr.append(leit.value)

    

    #Convert voltage value to TDS value
    tdsValue=(133.42/Voltage*Voltage*Voltage - 255.86*Voltage*Voltage + 857.39*Voltage)*0.5

    print("PH: " + str(ph.value), str(ph.voltage))
    print("Leit: " + str(tdsValue))
    print("Temp: " + str(temp.value), str(temp.voltage))
    counter+=1