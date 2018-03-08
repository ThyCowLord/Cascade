import picamera
import subprocess as x
import os.path


cam = picamera.PiCamera()
try:
  cam.capture('testimageverylongfilenamepleasedeleteafterphotohasbeentaken.jpg')
  cam.start_recording('testimageverylongfilenamepleasedeleteafterphotohasbeentaken.h264')
except Exception as e:
  exit("Something went wrong... The error was: "+e)

x.run("rm testimageverylongfilenamepleasedeleteafterphotohasbeentaken.jpg")
x.run("rm testimageverylongfilenamepleasedeleteafterphotohasbeentaken.mp4")


def picture():
  try:
    cam.start_recording("~/livid.mp4")
    time.sleep(15)
    cam.stop_recording()
    send()
  except Exception as e:
    print("Something went wrong.... "+e)
def send():
  x.run("cp ~/livid.mp4 /var/www/html/livid.mp4")
  x.run("rm ~/livid.mp4")
try:
  picture()
except Exception as e:
  print("Something went wrong... "+e)
  
  
