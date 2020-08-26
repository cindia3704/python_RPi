import cv2
from time import sleep
import requests
import io
import json
import os
import random

# Yesol & Jisu's Code
import picamera
import time

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(5)
    camera.capture('capture.jpg')
    camera.stop_preview()

sleep(2)
resim = "capture.jpg"
img = cv2.imread(resim)
print("Picture is Detected")

api = img

# Ocr
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", api, [1, 90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api,
                       files={resim: file_bytes},
                       data={"apikey": "helloworld",
                             "language": "eng"})

result = result.content.decode()
print(result)
result = json.loads(result)

parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")
print(text_detected)

print("Text is writing to file...")
f = open("text_detected.txt", "a+")
f.write(text_detected)
f.close()
print("Operation is successful")

cv2.imshow("Img", img)
cv2.waitKey(0)
os.remove(resim)
