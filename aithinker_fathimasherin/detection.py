



import cv2

# Load the pre-trained face detection classifierface_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Open the webcam

cap = cv2.VideoCapture(0)

# Loop through the frames from the webcamwhile True:

    # Read a frame from the webcam    ret, frame = cap.read()

    # Convert the frame to grayscale

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the detected faces

    for (x, y, w, h) in faces:        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame

    cv2.imshow('Face Detection', frame)

    # Check for key press to exit    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

# Release the webcam and destroy all windows

cap.release()cv2.destroyAllWindows()




