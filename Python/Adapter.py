class ExternalMedicalSystem:
    def get_child_medical_history(self, child_id: str):
        # Симуляція зовнішньої медичної системи
        return {
            "vaccinations": ["BCG", "Polio"],
            "allergies": ["Nuts"],
            "chronic_conditions": []
        }

class MedicalRecordAdapter:
    def __init__(self, external_system: ExternalMedicalSystem):
        self._external_system = external_system

    def get_medical_records(self, child_id: str):
        external_records = self._external_system.get_child_medical_history(child_id)
        return {
            "vaccinations": external_records.get("vaccinations", []),
            "allergies": external_records.get("allergies", []),
            "chronic_conditions": external_records.get("chronic_conditions", [])
        }