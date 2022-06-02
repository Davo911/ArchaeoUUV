
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
from flask import Flask
import logging

DHTSensor = Adafruit_DHT.DHT11
GPIO_Pin = 2

#log = "~/temp.log"
#logging.basicConfig(filename=log,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
app = Flask(__name__)

@app.route('/')
def index():
    try:

        with open(r"/sys/class/thermal/thermal_zone0/temp") as File:
            CPUTemp = str(float(File.readline())/1000)

        Luftfeuchte, Temperatur = Adafruit_DHT.read_retry(DHTSensor, GPIO_Pin)
        if Luftfeuchte is None or Temperatur is None:
            print('Fehler')
        sensor_data = "Temperatur-CPU = "+CPUTemp+"°C<br/>" + 'Temperatur-Sensor = ' + str(Temperatur)+"°C<br/>" + 'Humidity = ' + str(Luftfeuchte) + "%<br/>"
        print(sensor_data.replace("<br/>","\n"))
        print("-----")
        #logging.info('Log Entry Here.')
        return sensor_data
 
    except KeyboardInterrupt:
        GPIO.cleanup()

        
    
app.run(debug=True, port=80, host='0.0.0.0')
