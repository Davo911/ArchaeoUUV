import spidev #import the SPI library for RB Pi 4 B board
import time #import the Timing library for RB Pi 4 B board
from urllib.parse import urlparse
import subprocess
import os

AMT22_NOP = 0 #command to read the position of the encoder
#AMT22_NOP = hex("00A00000")
AMT22_NOP = 0x00
AMT22_RESET = 0x60
AMT22_ZERO = 0x70
AMT22_READ_TURNS = 0xA0

NEWLINE = 0x0A
TAB = 0x09
spi = spidev.SpiDev() #create the spi object
spi.open(0, 0) #SPI port 0, CS 0
speed_hz=500000 #setting the speed in hz
delay_us=3 #setting the delay in microseconds


calibturns=255
calibtotat=6518
while True:
  #result=spi.xfer2([AMT22_NOP, AMT22_NOP],speed_hz,delay_us)
  #test=((result[0] & 0b111111) << 8) + result[1]
  #print(test)
  result=spi.xfer2([AMT22_NOP, AMT22_READ_TURNS, AMT22_NOP, AMT22_NOP],speed_hz,delay_us)
  rotation=((result[0] & 0b111111) << 8) + result[1] # 0 - 16383 Pro umdrehung
  turns=result[3]
  print(rotation)
  print(turns)

  lenght=(((calibturns-turns)*16383)-rotation+calibtotat)/370
  #print(lenght)
  if lenght<0:
     lenght=0
  #o=subprocess.run(["curl http://192.168.2.2:6040/mavlink/vehicles/1/components/1/messages/AHRS2/message/altitude"])
  url="http://192.168.2.2:6040/mavlink/vehicles/1/components/1/messages/AHRS2/message/altitude"
  depth= subprocess.run(["curl", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  url="http://192.168.2.2:6040/mavlink/vehicles/1/components/1/messages/VFR_HUD/message/heading"
  result = subprocess.run(["curl", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  #print(result.stdout)
  compass= subprocess.run(["curl", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  print("Tiefe")
  print(depth.stdout)
  print("Kompass")
  print(compass.stdout)
  #print(result.stderr)
  #result[1] = result[1] << 8 
  #result[1] = result[0] + result[1]
  #  result2=spi.xfer2([AMT22_NOP, AMT22_READ_TURNS, AMT22_NOP, AMT22_NOP],speed_hz,delay_us) 
  #result3=spi.xfer2([AMT22_NOP, AMT22_RESET],speed_hz,delay_us) 
  #result4=spi.xfer2([AMT22_NOP, AMT22_ZERO],speed_hz,delay_us) 
  #strings = [str(integer) for integer in result] #converting the list into an integer
  #a_string = "".join(strings)
  #an_integer = int(a_string)
  #print(hex(an_integer)) #print the integer in hex format
  #print(result) # Good enough for now
  #  print(result2)
  #  print(result3)
  # print(result4)
  os.system("clear")
  time.sleep(0.2)
  #currentPosition = spi.xfer2(AMT22_NOP, encoder, false) << 8;
  #print(currentPosition)
  #time.sleep(0.5)
