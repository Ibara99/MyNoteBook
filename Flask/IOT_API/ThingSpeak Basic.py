######################################################
'''
This code takes values calulated and puts them into a variable called f which consists of an baseURL which is specific for your project
since it is defined by the api_key. The variable f is the link including the new value that inserts a new measurment point to your 
thingspeak channel. the f.read() command opens this link and the f.close command closes it. The variable that is transmitted can be
changed as you want to. In this case it calculates Fibonnaci Numbers.
'''

'''
import sys
#import RPi.GPIO as GPIO
from time import sleep
from urllib.request import urlopen

a = 0
b = 1
c = 0
baseURL = 'http://api.thingspeak.com/update?api_key=UXU3MH6Y6FSRHFGZ&field1='
arg2 = '&field2='
while(a < 1000):
	print (a)
	f = urlopen(baseURL +str(a)+arg2+str(b**2))
	f.read()
	f.close()
	sleep(5)
	c = a
	a = a + b
	b = c 	
print ("Program has ended")
'''
#Credit : https://www.instructables.com/id/Basic-Thingspeak-Introduction-Using-Python/


#########################################
'''
This is how to read data from thingspeak; A BASIC
'''
#import sys
#import RPi.GPIO as GPIO
#from time import sleep
from urllib.request import urlopen
import json

# define url per field;
public_url = 'https://api.thingspeak.com/channels/1023062/fields/1/last.json' #or you could use .json instead
private_url = 'https://api.thingspeak.com/channels/1023062/fields/1.json?api_key=IT7X6X01UZ3DJR0T&results=1' #result menunjukkan berapa data TERAKHIR
#or use feed to get all field
feed_url = 'https://api.thingspeak.com/channels/1023062/feeds/last.json'
#you can change it later
f = urlopen(public_url)
y = json.loads(f.read())
print(y['field1'])
