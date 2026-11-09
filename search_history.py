import json
import os

from datetime import datetime


HISTORY_FILE = "search_history.json"


class SearchHistory:

    def __init__(self):

        self.history_file = HISTORY_FILE

        if not os.path.exists(self.history_file):

            self.save_history([])

    def save_history(self, history):

        try:

            with open(self.history_file, "w") as file:

                json.dump(history, file, indent=4)

        except OSError as error:

            print(f"Error saving search history: {error}")

    def get_history(self):

        try:

            with open(self.history_file, "r") as file:

                return json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):

            return []

    def add_search(self, medication_name):

        history = self.get_history()

        search_record = {
            "medication": medication_name,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        history.insert(0, search_record)

        self.save_history(history)

    def clear_history(self):

        self.save_history([])

        print("Search history cleared successfully.")