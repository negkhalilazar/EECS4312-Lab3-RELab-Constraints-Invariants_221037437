# Contains requirement-driven tests for the dispensing subsystem.
# TODO: create at least 3 test cases
import pytest
from datetime import date
from dispense import DispenseEvent
# from dispense import DispenseEvent, MAX_DOSES

def test_invalid_inputs():
    #Inv patient
    with pytest.raises(ValueError):
        DispenseEvent("", "aspirin", 100, 1)
    #Inv med
    with pytest.raises(ValueError):
        DispenseEvent("patient1", "", 100, 1)
    #Inv dose
    with pytest.raises(ValueError):
        DispenseEvent("patient1", "aspirin", 0, 1)
    #zero quantity
    with pytest.raises(ValueError):
        DispenseEvent("patient1", "aspirin", 100, 0)
    #non-integer quantity
    with pytest.raises(ValueError):
        DispenseEvent("patient1", "aspirin", 100, 1.5)
def test_invariant():
    today = date.today()
    existing_events = [DispenseEvent("patient1", "aspirin", 100, 1, today)]
    repeat_event = DispenseEvent("patient1", "aspirin", 200, 1, today)
    assert not DispenseEvent.invariant_holds(existing_events, repeat_event)
def test_max_dose():
    with pytest.raises(ValueError):
        DispenseEvent("patient1", "ibuprofen", 800, 6)

