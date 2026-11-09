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
