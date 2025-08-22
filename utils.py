import cv2
import mysql.connector

def draw_boundray(img, classifier, scaleFactor, minimumneighbors, color, text, clf):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_image, scaleFactor, minimumneighbors)

    coord = []

    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        id, predict = clf.predict(gray_image[y:y + h, x:x + w])
        confidence = int((100 * (1 - predict / 300)))

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="face_recognizer"
        )
        my_cursor = conn.cursor()

        my_cursor.execute("select Std_name from student where Std_Id=" + str(id))
        n = "+".join(my_cursor.fetchone())

        my_cursor.execute("select `Roll No.` from student where Std_Id=" + str(id))
        r = "+".join(my_cursor.fetchone())

        my_cursor.execute("select Dep from student where Std_Id=" + str(id))
        d = "+".join(my_cursor.fetchone())

        if confidence > 77:
            cv2.putText(img, f"Roll No.:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            cv2.putText(img, f"Std_name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            cv2.putText(img, f"Dep:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

        coord = [x, y, w, h]

    return coord
