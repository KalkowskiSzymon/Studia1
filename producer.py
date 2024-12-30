import csv
import uuid
import time

FILE_NAME = "tasks.csv"


def create_task():
    task_id = str(uuid.uuid4())
    return {"id": task_id, "status": "pending"}


def write_task_to_file(task):
    try:
        with open(FILE_NAME, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "status"])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(task)
            print(
                f"Task {task['id']} has been created with status: {task['status']}"
            )
    except Exception as e:
        print(f"Error writing task to file: {e}")


if __name__ == "__main__":
    while True:
        task = create_task()
        write_task_to_file(task)
        time.sleep(10)
