import os
import uuid
import pika
import json


def get_unique_image_path(file_path):
    """
    Funkcja generująca unikalną nazwę pliku.
    """
    filename, ext = os.path.splitext(file_path)
    unique_filename = f"{filename}_{uuid.uuid4().hex}{ext}"
    return unique_filename


def send_task_to_queue(image_path, task_id):
    """
    Funkcja wysyłająca zadanie do kolejki RabbitMQ
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("localhost")
    )
    channel = connection.channel()

    channel.queue_declare(queue="task_queue", durable=True)

    task = {"task_id": task_id, "image_path": image_path}

    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=json.dumps(task),
        properties=pika.BasicProperties(
            delivery_mode=2,
        ),
    )
    print(f"Zadanie {task_id} wysłane do kolejki.")
    connection.close()
