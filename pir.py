import RPi.GPIO as GPIO
import time, datetime
import pygame, sys
from pygame.locals import *
import pygame.camera
import smtplib
import paho.mqtt.client as paho


broker="192.168.0.160"
port=1883


def on_publish(client,userdata,result):
    print("data published \n")
pass



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)



pir=7
dateString = '%Y-%m-%d-%H-%M-%S'


GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir,GPIO.IN)
time.sleep(5) #SETTING UP THE SENSOR
print("SENSOR is READY")
y=0
while 2>1:
	x=GPIO.input(pir)
	#print(x)
	if x==1 and y==0:
		print('Motion detected')
		GPIO.output(5,0)
		client1= paho.Client("control1")                           
		client1.on_publish = on_publish                         
		client1.connect(broker,port)                             
		ret= client1.publish("monitor/intrusion","Motion Detected")

		y=1
	elif x==0 and y==1:
		print('Motion Stopped')
		y=0
		GPIO.output(5,1)

		
	time.sleep(1) #SETTING UP THE SENSOR

GPIO.cleanup()

