# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM);
GPIO.setup(17, GPIO.OUT);

led = GPIO.PWM(17, 200);
led.start(0);

while True:
	led.ChangeDutyCycle(100);
	sleep(1);
	led.ChangeDutyCycle(0);
	sleep(1);

