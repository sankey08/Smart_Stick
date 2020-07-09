import sys
import urllib
from time import sleep
import _thread
import RPi.GPIO as GPIO
import time
import requests
import json
import pygame


#url = 'https://extreme-ip-lookup.com/json/'
#r = requests.get(url)
#data = json.loads(r.content.decode())

# Enter Your API key here
#myAPI = 'UE87NNYWHNEDCIOG'
# URL where we will send the data, Don't change it
#baseURL = 'https://thingspeak.com/channels/867142/api_keys=%s' % myAPI

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.setwarnings(False)

GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO_BUZZER = 20

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_BUZZER, GPIO.OUT)

GPIO.output(GPIO_TRIGGER, False)
GPIO.output(GPIO_BUZZER, False)

keepRunning = True
distance = 0

def measureDistance():
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(0.5)
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        start = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        stop = time.time()

    elapsed = stop - start
    distance = (elapsed * 34300) / 2
    return distance
    distance = dht.read_retry(dht.DHT22, 23)
    distance = DHT22_data()
    conn = urllib2.urlopen(baseURL + (distance))



def playSound(threadName, delay):
    keepRunning
    distance
    while keepRunning:
         if distance <= 60:
            #while pygame.mixer.music.get_busy() == True:
            #   continue
            pygame.mixer.init()
            pygame.mixer.music.load('file2.mp3')
            GPIO.output(GPIO_BUZZER, True)
            pygame.mixer.music.play(0, 0.0)
            time.sleep(delay)
            time.sleep(0.01 * distance)
            GPIO.output(GPIO_BUZZER, False)
            time.sleep(0.05 * distance)
            time.sleep(delay)
            
            #if distance <= 60:
                
                #pygame.mixer.music.play(-1, 0.0)
                #time.sleep(delay)
            
            if GPIO.input(channel):
                    print ("Water Detected!")
            else:
                    print ("Water Not Detected!")
                
try:
    distance = measureDistance()
    _thread.start_new_thread(playSound, ("BuzzerThread1", 0.01))
    while True:
        print ("Measured Distance = %f cm" % distance)
        time.sleep(0.1)
        distance = measureDistance()
        
    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
    GPIO.add_event_callback(channel, callback)
    conn.close()
    while True:
            time.sleep(1)
except:
    keepRunning = False
    time.sleep(1)
    GPIO.cleanup()

