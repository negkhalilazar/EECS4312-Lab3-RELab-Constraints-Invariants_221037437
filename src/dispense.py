from datetime import date
MAX_DOSES = {"aspirin": 4000, "ibuprofen": 3200}
class DispenseEvent:
    """
    Represents a single medication dispensing event for a patient.

    """
    

    # TODO Task 3: Encode and enforce input constraints (e.g., valid dose, quantity, identifiers)
    def __init__(self, patient_id, medication, dose_mg, quantity, event_date=None):
        """
        Initialize a new DispenseEvent.

        Args:
            patient_id: Unique identifier for the patient receiving medication.
            medication: Name or identifier of the medication being dispensed.
            dose_mg: Dose per unit in milligrams. Must be a positive number.
            quantity: Number of units dispensed. Must be a positive integer.

        """
        
        "Assuming patient ID and medication is string, also assuming hard coded max dosages allowed for medication"
        if not isinstance(patient_id, str) or not patient_id:
            raise ValueError("patient_id must be a non-empty string")
        if not isinstance(medication, str) or not medication:
            raise ValueError("medication must be a non-empty string")
        if dose_mg <= 0:
            raise ValueError("dose must be positive")
        if not isinstance(quantity, int):
            raise ValueError("quantity must be integer")
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        if event_date and not isinstance(event_date, date):
            raise ValueError("even_date must be a date object")
        "after checking the above"
        if dose_mg * quantity > MAX_DOSES.get(medication, float('inf')): 
            raise ValueError("dose exceeds maximum allowed")
        self.date = event_date
        self.patient_id = patient_id
        self.medication = medication
        self.dose_mg = dose_mg
        self.quantity = quantity
    # TODO Task 4: Define and check system invariants 
    @staticmethod
    def invariant_holds(existing_events, new_event):
        """
        Check whether adding a new dispense event preserves all system invariants.

        Args:
            existing_events: Iterable of previously recorded DispenseEvent objects.
            new_event: The proposed DispenseEvent to validate.

        Returns:
            bool: True if all invariants hold after adding new_event; False otherwise.
            
        """
        key = (new_event.patient_id, new_event.medication, new_event.date)
        for event in existing_events:
            if (event.patient_id, event.medication, event.date) == key:
                return False
        return True
