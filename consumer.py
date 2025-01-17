import pika
import json
from detector import ObjectDetector
import cv2
import os
from utils import get_unique_image_path


def process_task(ch, method, properties, body):
    task = json.loads(body)
    task_id = task["task_id"]
    image_path = task["image_path"]

    print(f"Przetwarzam zadanie {task_id} - Wczytywanie obrazu z {image_path}")

    model_path = "models/frozen_inference_graph.pb"
    config_path = "models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt"
    detector = ObjectDetector(model_path, config_path)

    img = cv2.imread(image_path)
    if img is None:
        print(f"Zadanie {task_id} nie udało się wczytać obrazu.")
        return

    img, person_count = detector.process_image(img)

    result_directory = "uploads/results"
    if not os.path.exists(result_directory):
        os.makedirs(result_directory)

    processed_image_path = f"uploads/processed_{task_id}.png"
    processed_image_path = get_unique_image_path(processed_image_path)
    cv2.imwrite(processed_image_path, img)

    print(
        f"Zadanie {task_id} zakończone. Liczba wykrytych osób: {person_count}"
    )

    result = {
        "task_id": task_id,
        "person_count": person_count,
        "image_path": processed_image_path,
    }

    with open(f"{result_directory}/{task_id}_result.json", "w") as f:
        json.dump(result, f)

    ch.basic_ack(delivery_tag=method.delivery_tag)


def start_consumer():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("localhost")
    )
    channel = connection.channel()

    channel.queue_declare(queue="task_queue", durable=True)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="task_queue", on_message_callback=process_task)

    print("Czekam na zadania. Aby zakończyć, naciśnij CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    start_consumer()
