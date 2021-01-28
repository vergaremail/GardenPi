from picamera import PiCamera, Color
from time import sleep
import datetime

camera = PiCamera()

camera.brightness = 50
camera.resolution = (720, 480)
#camera.image_effect = 'watercolor'
camera.image_effect = 'colorbalance'
camera.exposure_mode = 'auto'
camera.awb_mode = 'auto'
camera.rotation = 180

camera.annotate_background = Color('green')
camera.annotate_foreground = Color('white')
camera.annotate_text_size = 32
text = "Grace's GardenPi " + datetime.datetime.now().strftime("%x,%X")
pictureName = "/home/pi/Desktop/gardenpi_files/pictures/Picture_"+datetime.datetime.now().strftime("%m-%d-%y_%X")+".jpg"
f = open("/home/pi/Desktop/gardenpi_files/picturelist.txt","a")
f.write("Picture_"+datetime.datetime.now().strftime("%m-%d-%y_%X")+".jpg\n")
f.close()
camera.annotate_text = text
camera.capture(pictureName)




#camera.start_recording('/home/pi/Desktop/gardenpi_files/pictures/video.h264')
#sleep(5)
#camera.stop_recording()
