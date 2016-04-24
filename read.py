#!/usr/bin/python
"""
Uses Adafruit DHT library
"""
import sys
import requests
import Adafruit_DHT
from socket import gethostname

url = 'http://your.server/subfolder-maybe/'
sensor = Adafruit_DHT.DHT11
pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
    hostname = gethostname()
    data = {'hostname': hostname, 'temperature': temperature, 'humidity': humidity}
    result = requests.post(url, data=data)
    print result
    print result.text
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print 'Failed reading sensor, will not post'
