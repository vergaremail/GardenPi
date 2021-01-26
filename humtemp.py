import Adafruit_DHT
import datetime

sensorpin = 4

class getHumTemp:
    def __init__(self):
        self.H,self.T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, sensorpin)

def Sensor():
    return getHumTemp()

A = Sensor()
H = A.H
T = A.T

f = open("humidityandtemp.txt","a")
f.write(datetime.datetime.now().strftime("%x,%X,")+"{0:0.1f},{1:0.1f}".format(T, H)+"\n")
f.close()