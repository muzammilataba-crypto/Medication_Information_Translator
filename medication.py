class Medication:

    def __init__(
        self,
        name,
        uses="Information unavailable",
        dosage="Information unavailable",
        side_effects="Information unavailable",
        warnings="Information unavailable",
        recalls="Information unavailable"
    ):


        self.name = name
        self.uses = uses
        self.dosage = dosage
        self.side_effects = side_effects
        self.warnings = warnings
        self.recalls = recalls

    def get_information(self):


        return {
            "Medication Name": self.name,
            "Uses": self.uses,
            "Dosage and Instructions": self.dosage,
            "Side Effects": self.side_effects,
            "Warnings and Precautions": self.warnings,
            "FDA Recalls": self.recalls
        }

    def display_information(self):

        information = self.get_information()

        for category, details in information.items():

            print(f"\n{category}:")
            print(details)