class Medication:
    def __init__(
            self,
            name'
            uses = "Information Unavailable",
            dosage = "Information unavailable",
            side_effects = "Information Unavailable",
            Warnings = "Information Unavailable",
            recalls = "Information unavailable"
            ):

        
        self.name = name
        self.uses = self.uses
        self.dosage = self.dosage
        self.side_effects = self.side_effects
        self.warnings = Warning
        self.recalls = self.recalls
        
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
