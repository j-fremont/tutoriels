# -*- coding: utf-8 -*-

from picamera2 import Picamera2, Preview
from datetime import datetime
from time import sleep
from gpiozero import MotionSensor, LED
from signal import pause
from time import sleep

pir = MotionSensor(4)

def picture():
	camera = Picamera2();
	camera_config =	camera.create_preview_configuration() 
	camera.configure(camera_config)
	camera.start_preview(Preview.DRM)
	camera.start()
	name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_") + 'image.jpg'
	camera.capture_file('./' + name)
	camera.stop_preview()
	camera.close()
	sleep(10)

pir.when_motion = picture

pause()

