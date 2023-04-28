# imports
import requests
import os
import json
import vobject
import serial
from time import sleep
from icalendar import Calendar, Event
from dotenv.main import load_dotenv


# env variables
load_dotenv()
token = os.environ['TOKEN']
myPort = os.envrion['PORT']


# sends data to arduino via serial
def arduino_serial(dataArr, port):
    arduino = serial.Serial(port, 9600)
    sleep(5)
    for data in dataArr:
        arduino.write(bytes(data, 'utf-8'))
        sleep(3)


# formats ics link for opening
def format_ics(link):
    return 'https://ufl.instructure.co' + link[29:len(link)]


# canvas API fetch
url = 'https://canvas.instructure.com/api/v1/courses?access_token=' + token
response = requests.get(url)
JSON = response.json()
arr3Obj = JSON[2]
icsLink = arr3Obj.get('calendar').get('ics')
print("ICS LINK BELOW:")
print(icsLink)
formattedIcs = format_ics(icsLink)
print("FORMATTED ICS LINK BELOW:")
print(formattedIcs)


# open ics download from ics link
r = requests.get(formattedIcs, allow_redirects=True)
open('link.ics', 'wb').write(r.content)

# read ics data
data = open('link.ics').read()
cal = vobject.readOne(data)


# pull student assignment data
gcal = Calendar.from_ical(data)
for component in gcal.walk():
    if component.name == "VEVENT":
        print(component.get('summary'))
        courseList.append(component.get('summary'))


# send student data to arduino
courseList = []
arduino_serial(courseList, myPort)
