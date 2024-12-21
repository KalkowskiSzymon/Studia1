import csv


class Producer:
    def __init__(self, task_file="tasks.csv"):
        self.task_file = task_file

    def add_task_to_file(self, task_description):
        with open(self.task_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([task_description, "pending"])
            # Złamana linia w komunikacie
            print(f"Praca '{task_description}' "
                  "dodana do pliku jako 'pending'.")

    def create_task(self):
        task_description = input(
            "Wpisz opis pracy (lub 'exit' aby zakończyć): "
        )
        if task_description.lower() == "exit":
            return False
        self.add_task_to_file(task_description)
        return True
