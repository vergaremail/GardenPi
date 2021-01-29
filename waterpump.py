#Welcome to Edward's Garden Pi program
#Change the duration of pump 1 and pump 2 here to the amount of water needed
#Duration is counted per second

pump1_duration = 8
pump2_duration = 2

#-------------------------------------------------------------------------------------------------------------------------------------------

#!/usr/bin/python

import gpiozero
import time
import datetime

# Relay GPIO Pin Assignment
relayPin1 = 17
relayPin2 = 27
relayPin3 = 22
relayPin4 = 23
relayPin5 = 24
relayPin6 = 25
relayPin7 = 5
relayPin8 = 6

interval = 2

relay1 = gpiozero.OutputDevice(relayPin1, active_high=False, initial_value=False)
relay2 = gpiozero.OutputDevice(relayPin2, active_high=False, initial_value=False)
relay3 = gpiozero.OutputDevice(relayPin3, active_high=False, initial_value=False)
relay4 = gpiozero.OutputDevice(relayPin4, active_high=False, initial_value=False)
relay5 = gpiozero.OutputDevice(relayPin5, active_high=False, initial_value=False)
relay6 = gpiozero.OutputDevice(relayPin6, active_high=False, initial_value=False)
relay7 = gpiozero.OutputDevice(relayPin7, active_high=False, initial_value=False)
relay8 = gpiozero.OutputDevice(relayPin8, active_high=False, initial_value=False)

# Turn off all relays 1 to 8 all at the same time
def allOffOnce():
    relay1.off()
    relay2.off()
    relay3.off()
    relay4.off()
    relay5.off()
    relay6.off()
    relay7.off()
    relay8.off()

# Turn On pumps
def pump1On():
    relay1.on()
    time.sleep(pump1_duration)
    relay1.off()
    f = open("/home/pi/Desktop/gardenpi_files/pumprecord.csv","a")
    f.write(datetime.datetime.now().strftime('%d %m %Y %H %M %S,')+"Pump 1,"+str(pump1_duration)+"\n")
    f.close()
   
    
def pump2On():
    relay2.on()
    time.sleep(pump2_duration)
    relay2.off()
    f = open("/home/pi/Desktop/gardenpi_files/pumprecord.csv","a")
    f.write(datetime.datetime.now().strftime('%d %m %Y %H %M %S,')+"Pump 2,"+str(pump2_duration)+"\n")
    f.close()


def rest():
    time.sleep(interval)

allOffOnce()
pump1On()
rest()
pump2On()