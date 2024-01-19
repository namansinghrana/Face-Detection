import cv2

face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)  # Use 0 for default camera, or provide the path to a video file

while True:
    ret, video_data = video_cap.read()

    if not ret:
        print("Error: Couldn't read video frame.")
        break

    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (255,0, 0), 2)

    cv2.imshow("video_live", video_data)

    if cv2.waitKey(10) == ord("q"):
        break

video_cap.release()
cv2.destroyAllWindows()
