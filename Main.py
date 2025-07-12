import cv2
Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
Start the webcam
camera = cv2.VideoCapture(0)
while True:
# Capture each frame
ret, frame = camera.read()
if not ret:
break
# Convert to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
# Draw rectangles around detected faces
for (x, y, w, h) in faces:
cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Show the output
cv2.imshow('Video', frame)
# Exit on 'q' key press
if cv2.waitKey(1) & 0xFF == ord('q'):
break
Release the camera and close windows
camera.release()
cv2.destroyAllWindows()
