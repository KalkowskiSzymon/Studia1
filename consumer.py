import csv
import time


class Consumer:
    def __init__(self, task_file="tasks.csv"):
        self.task_file = task_file

    def read_tasks_from_file(self):
        tasks = []
        try:
            with open(self.task_file, mode="r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    tasks.append(row)
        except FileNotFoundError:
            print("Plik z zadaniami nie istnieje. Tworzymy nowy.")
        return tasks

    def write_tasks_to_file(self, tasks):
        with open(self.task_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(tasks)

    def process_task(self):
        tasks = self.read_tasks_from_file()
        for i, task in enumerate(tasks):
            description, status = task
            if status == "pending":
                print(f"Zadanie '{description}'w trakcie realizacji")
                tasks[i][1] = "in_progress"
                self.write_tasks_to_file(tasks)
                time.sleep(30)
                print(f"Zadanie '{description}' zostało wykonane!")
                tasks[i][1] = "done"
                self.write_tasks_to_file(tasks)
                break

    def consume(self):
        while True:
            tasks = self.read_tasks_from_file()
            pending_tasks = [task for task in tasks if task[1] == "pending"]

            if pending_tasks:
                self.process_task()
            else:
                time.sleep(5)
