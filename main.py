import config
import picamera
import subprocess
import os.path

cam = picamera.PiCamera()
try:
  cam.capture('testimageverylongfilenamepleasedeleteafterphotohasbeentaken.jpg')
  cam.start_recording('testimageverylongfilenamepleasedeleteafterphotohasbeentaken.h264')
except Exception as e:
  exit("Something went wrong... The error was: "+e)

subprocess.run("rm testimageverylongfilenamepleasedeleteafterphotohasbeentaken.jpg")
subprocess.run("rm testimageverylongfilenamepleasedeleteafterphotohasbeentaken.h264")


def picture():
  try:
    cam.capture(config.path)
    
  
  
