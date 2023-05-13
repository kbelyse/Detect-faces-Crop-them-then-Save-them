import cv2

image_path = 'C:\\Users\\KB\\Pictures\\Saved Pictures\\Ruger.jpg'
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cascade_path = 'C:\\Users\\KB\\Pictures\\Saved Pictures\\haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for i, (x, y, w, h) in enumerate(faces):

    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)

    face = image[y:y + h, x:x + w]

    face_filename = f'face{i}.jpg'
    cv2.imwrite(face_filename, face)
    print(f"Saved {face_filename}")

cv2.imshow("Detected Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
