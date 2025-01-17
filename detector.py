import cv2 as cv
import requests
import numpy as np


class ObjectDetector:
    def __init__(self, model_path, config_path):
        print("Wczytuję model...")
        self.net = cv.dnn.readNetFromTensorflow(model_path, config_path)
        print("Model wczytany pomyślnie.")

    def detect_objects(self, url, save_image=False):
        try:
            print(f"Pobieram obraz z URL: {url}")
            response = requests.get(url)
            img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
            img = cv.imdecode(img_array, cv.IMREAD_COLOR)
            if img is None:
                print("Błąd: Obraz nie został poprawnie pobrany z URL.")
                return [], 0
            print("Obraz został pobrany pomyślnie.")
            return self.process_image(img, save_image)
        except Exception as e:
            print(f"Zdarzył się błąd przy pobieraniu obrazu: {e}")
            return [], 0

    def process_image(self, img, save_image=False):
        rows = img.shape[0]
        cols = img.shape[1]
        print(f"Rozmiar obrazu: {rows}x{cols}")
        blob = cv.dnn.blobFromImage(
            img,
            1.0,
            (300, 300),
            (127.5, 127.5, 127.5),
            swapRB=True,
            crop=False,
        )
        self.net.setInput(blob)
        detections = self.net.forward()
        threshold = 0.5
        person_count = 0
        for i in range(detections.shape[2]):
            score = detections[0, 0, i, 2]
            if score > threshold:
                person_count += 1
                box = detections[0, 0, i, 3:7] * np.array(
                    [cols, rows, cols, rows]
                )
                (x, y, right, bottom) = box.astype("int")
                cv.rectangle(
                    img, (x, y), (right, bottom), (125, 255, 51), thickness=2
                )
        print(f"Liczba wykrytych osób: {person_count}")
        return img, person_count
