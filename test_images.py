import pika
import os
import json


image_directory = "test_images"

queue_name = "task_queue"
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue=queue_name, durable=True)

for image_name in os.listdir(image_directory):
    image_path = os.path.join(image_directory, image_name)
    if os.path.isfile(image_path):
        task_id = image_name.split(".")[0]
        message = {"task_id": task_id, "image_path": image_path}

        channel.basic_publish(
            exchange="",
            routing_key=queue_name,
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2),
        )
        print(f"Wysłano zadanie dla obrazu: {image_name}")

connection.close()
print("Wszystkie obrazy zostały wysłane do kolejki.")
