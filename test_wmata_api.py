from wmata_api import app
import json
import unittest

class WMATATest(unittest.TestCase):
    # Ensure both endpoints return a 200 HTTP code
    def test_http_success(self):
        escalator_response = app.test_client().get('/incidents/escalator').status_code
        elevator_response = app.test_client().get('/incidents/elevator').status_code
        # Assert that the response code of 'incidents/escalator' returns a 200 code
        self.assertEqual(escalator_response, 200, "Expected 200 HTTP status for escalator endpoint")
        # Assert that the response code of 'incidents/elevator' returns a 200 code
        self.assertEqual(elevator_response, 200, "Expected 200 HTTP status for elevator endpoint")

    # Ensure all returned incidents have the 4 required fields
    def test_required_fields(self):
        required_fields = ["StationCode", "StationName", "UnitName", "UnitType"]
        response = app.test_client().get('/incidents/escalator')
        json_response = json.loads(response.data.decode())
        # For each incident in the JSON response, assert that each of the required fields is present in the response
        for incident in json_response:
            for field in required_fields:
                self.assertIn(field, incident, f"Expected field '{field}' in escalator response")

    # Ensure all entries returned by the /incidents/escalator endpoint have a UnitType of "ESCALATOR"
    def test_escalators(self):
        response = app.test_client().get('/incidents/escalator')
        json_response = json.loads(response.data.decode())
        # For each incident in the JSON response, assert that the 'UnitType' is "ESCALATOR"
        for incident in json_response:
            self.assertEqual(incident["UnitType"], "ESCALATOR", "Expected UnitType 'ESCALATOR' in escalator response")

    # Ensure all entries returned by the /incidents/elevator endpoint have a UnitType of "ELEVATOR"
    def test_elevators(self):
        response = app.test_client().get('/incidents/elevator')
        json_response = json.loads(response.data.decode())
        # For each incident in the JSON response, assert that the 'UnitType' is "ELEVATOR"
        for incident in json_response:
            self.assertEqual(incident["UnitType"], "ELEVATOR", "Expected UnitType 'ELEVATOR' in elevator response")

if __name__ == "__main__":
    unittest.main()