from flask import Flask, Response
import cv2
import os
app = Flask(__name__)

#os.environ["QT_QPA_PLATFORM"] = "wayland"

video = cv2.VideoCapture(0)
video2 = cv2.VideoCapture(1)

'''

#HOGCV = cv2.HOGDescriptor()
#HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())



def detect(frame):
    bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)

    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1

    cv2.putText(frame, 'Status : Detecting ', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('output', frame)

    return frame
'''

@app.route('/')
def index():
    return "Default Message"

def gen(video):
    while True:
        success, image = video.read()

        # people detection
        #image = detect(image)

        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()

        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2')
def video_feed2():
    global video2
    return Response(gen(video2),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True)


