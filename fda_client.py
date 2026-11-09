import requests

from medication import Medication


FDA_LABEL_URL = "https://api.fda.gov/drug/label.json"

FDA_RECALL_URL = "https://api.fda.gov/drug/enforcement.json"


class FDAClient:

    def __init__(self):

        self.timeout = 15

    def search_medication(self, medication_name):

        search_queries = [
            f'openfda.brand_name:"{medication_name}"',
            f'openfda.generic_name:"{medication_name}"'
        ]

        for query in search_queries:

            try:

                response = requests.get(
                    FDA_LABEL_URL,
                    params={
                        "search": query,
                        "limit": 1
                    },
                    timeout=self.timeout
                )

                if response.status_code == 200:

                    data = response.json()

                    if data.get("results"):

                        return self.process_medication(
                            data["results"][0],
                            medication_name
                        )

            except requests.exceptions.RequestException:

                print("Unable to connect to the FDA database.")

                return None

        print("Medication not found in the FDA database.")

        return None

    def get_field(self, data, field):

        value = data.get(field, ["Information unavailable"])

        if isinstance(value, list):

            return "\n".join(value)

        return str(value)

    def get_recalls(self, medication_name):

        try:

            response = requests.get(
                FDA_RECALL_URL,
                params={
                    "search": f'product_description:"{medication_name}"',
                    "limit": 5
                },
                timeout=self.timeout
            )

            if response.status_code == 200:

                data = response.json()

                recalls = data.get("results", [])

                if not recalls:

                    return "No matching recall records found."

                recall_information = []

                for recall in recalls:

                    details = (
                        f"Reason: {recall.get('reason_for_recall', 'Unavailable')}\n"
                        f"Status: {recall.get('status', 'Unavailable')}\n"
                        f"Date: {recall.get('recall_initiation_date', 'Unavailable')}"
                    )

                    recall_information.append(details)

                return "\n\n".join(recall_information)

            return "Recall information unavailable."

        except requests.exceptions.RequestException:

            return "Unable to retrieve recall information."

    def process_medication(self, data, medication_name):

        uses = self.get_field(
            data,
            "indications_and_usage"
        )

        dosage = self.get_field(
            data,
            "dosage_and_administration"
        )

        side_effects = self.get_field(
            data,
            "adverse_reactions"
        )

        warnings = self.get_field(
            data,
            "warnings"
        )

        recalls = self.get_recalls(medication_name)

        medication = Medication(
            name=medication_name,
            uses=uses,
            dosage=dosage,
            side_effects=side_effects,
            warnings=warnings,
            recalls=recalls
        )

        return medication