
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
 
DHTSensor = Adafruit_DHT.DHT11
GPIO_Pin = 2
 
try:
    while(1):
        Luftfeuchte, Temperatur = Adafruit_DHT.read_retry(DHTSensor, GPIO_Pin)
        if Luftfeuchte is not None and Temperatur is not None:
            print('Temperatur = {0:0.1f}°C  | rel. Luftfeuchtigkeit = {1:0.1f}%'.format(Temperatur, Luftfeuchte))
        else:
            print('Fehler')
        time.sleep(2)
 
except KeyboardInterrupt:
    GPIO.cleanup()
