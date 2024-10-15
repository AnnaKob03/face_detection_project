import cv2
import os

def detect_faces(image_path: str):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  # загрузка каскадного классификатора для обнаружения лиц
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # изображение -> оттенки серого для лучшего обнаружения лиц
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # обнаружение
    faces_count = len(faces)

    if faces_count == 1:
        print(f"Найдено {faces_count} лицо")
    elif 2 <= faces_count <= 4:
        print(f"Найдено {faces_count} лица")
    else:
        print(f"Найдено {faces_count} лиц")

    for (x, y, w, h) in faces:  # рисуем прямоугольники вокруг лиц
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Получаем путь к папке, где находится сам скрипт
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Формируем путь к выходному файлу
    output_path = os.path.join(script_directory, 'output_faces.jpg')
    
    cv2.imwrite(output_path, img)
    print(f"Изображение с результатом сохранено в {output_path}")

if __name__ == "__main__":
    image_path = 'image.jpg'
    detect_faces(image_path)
