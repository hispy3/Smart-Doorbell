import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import RPi.GPIO as GPIO
import picamera as c
import time as t

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

num=0

cred=credentials.Certificate("/home/pi/Desktop/martdoorbell.json")
firebase_admin.initialize_app(cred,{"storageBucket":"martdoorbell.appspot.com"})
bucket = storage.bucket("martdoorbell.appspot.com")

try:
    t.sleep(2)
    while True:
        if GPIO.input(23):
            GPIO.output(24,1)
            GPIO.output(18,1)
            t.sleep(0.5)
            GPIO.output(24,0)
            GPIO.output(18,0)
            print("MOTION detected....")
            camera=c.PiCamera()
            camera.start_preview()
            t.sleep(3)
            camera.capture('image.jpg')
            camera.stop_preview()
            camera.vflip=True
            camera.hflip=True
            camera.brightness=60
            num=num+1
            image_url='/home/pi/Desktop/smart_doorbell/image.jpg'
            blob=bucket.blob('image'+str(num)+'.jpg')
            blob.upload_from_filename(image_url)
            t.sleep(2)
            print('round'+str(num))
except:
    GPIO.cleanup()
    
    
    
