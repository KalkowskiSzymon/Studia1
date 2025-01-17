import os
import uuid
import pika
import json
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from detector import ObjectDetector
import cv2
from utils import (
    get_unique_image_path,
    send_task_to_queue,
)  # Zaimportowanie funkcji

# Załaduj zmienne środowiskowe z pliku .env
load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

model_path = os.getenv("MODEL_PATH")
config_path = os.getenv("CONFIG_PATH")


@app.route("/detect/url", methods=["GET"])
def detect_url():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Brak URL"}), 400

    task_id = str(uuid.uuid4())  # Unikalne ID zadania
    detector = ObjectDetector(model_path, config_path)
    img, person_count = detector.detect_objects(url, save_image=True)
    img_path = os.path.join(
        app.config["UPLOAD_FOLDER"], f"{task_id}_processed_image.png"
    )
    img_path = get_unique_image_path(img_path)
    cv2.imwrite(img_path, img)

    send_task_to_queue(img_path, task_id)

    return (
        jsonify({"task_id": task_id, "message": "Zadanie dodane do kolejki"}),
        202,
    )


@app.route("/detect/local", methods=["GET"])
def detect_local():
    image_path = request.args.get("image_path")
    if not image_path:
        return jsonify({"error": "Brak ścieżki do obrazu"}), 400
    if not os.path.exists(image_path):
        return jsonify({"error": "Plik nie istnieje"}), 404

    task_id = str(uuid.uuid4())
    detector = ObjectDetector(model_path, config_path)
    img = cv2.imread(image_path)
    if img is None:
        return jsonify({"error": "Nie udało się wczytać obrazu"}), 500
    img, person_count = detector.process_image(img)
    processed_image_path = os.path.join(
        app.config["UPLOAD_FOLDER"], f"{task_id}_processed_local_image.png"
    )
    processed_image_path = get_unique_image_path(processed_image_path)
    cv2.imwrite(processed_image_path, img)

    send_task_to_queue(processed_image_path, task_id)

    return (
        jsonify({"task_id": task_id, "message": "Zadanie dodane do kolejki"}),
        202,
    )


@app.route("/detect/upload", methods=["POST"])
def detect_upload():
    if "file" not in request.files:
        return jsonify({"error": "Brak pliku w żądaniu"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Brak pliku"}), 400
    if not file or not file.filename.lower().endswith(
        (".png", ".jpg", ".jpeg")
    ):
        return jsonify({"error": "Przesłany plik nie jest obrazem"}), 400

    task_id = str(uuid.uuid4())  # Unikalne ID zadania
    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"], f"{task_id}_{file.filename}"
    )
    file_path = get_unique_image_path(file_path)
    file.save(file_path)

    # Wyślij zadanie do RabbitMQ
    send_task_to_queue(file_path, task_id)

    return (
        jsonify({"task_id": task_id, "message": "Zadanie dodane do kolejki"}),
        202,
    )


@app.route("/check_task/<task_id>", methods=["GET"])
def check_task_status(task_id):
    result_path = f"uploads/results/{task_id}_result.json"

    if not os.path.exists(result_path):
        return (
            jsonify(
                {"error": "Zadanie w trakcie przetwarzania lub nie istnieje"}
            ),
            404,
        )

    with open(result_path, "r") as f:
        result = json.load(f)

    return jsonify(result)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
