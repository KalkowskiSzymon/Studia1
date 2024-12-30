import csv
import time

FILE_NAME = "tasks.csv"


def read_tasks():
    try:
        with open(FILE_NAME, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []


def update_task_status(task_id, new_status):
    tasks = read_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            break
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "status"])
        writer.writeheader()
        writer.writerows(tasks)


def process_task(task):
    print(f"Processing task {task['id']}...")
    time.sleep(30)
    update_task_status(task["id"], "done")
    print(f"Task {task['id']} is done.")


if __name__ == "__main__":
    while True:
        tasks = read_tasks()
        pending_tasks = [task for task in tasks if task["status"] == "pending"]

        if pending_tasks:
            task_to_process = pending_tasks[0]
            update_task_status(task_to_process["id"], "in_progress")
            process_task(task_to_process)
        else:
            print("No tasks to process. Checking again in 5 seconds.")

        time.sleep(5)
