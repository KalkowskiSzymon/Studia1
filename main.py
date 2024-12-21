import time
import threading
from producer import Producer
from consumer import Consumer


def main():
    task_file = "tasks.csv"

    producer = Producer(task_file)
    consumer = Consumer(task_file)

    consumer_thread = threading.Thread(target=consumer.consume)
    consumer_thread.daemon = True
    consumer_thread.start()

    while True:
        if not producer.create_task():
            break
        time.sleep(1)


if __name__ == "__main__":
    main()
