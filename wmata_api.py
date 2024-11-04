import json
import requests
from flask import Flask
# use the new url
INCIDENTS_URL = "https://jhu-intropython-mod10.replit.app/"
app = Flask(__name__)

# Get incidents by machine type (elevator/escalator)
@app.route("/incidents/<unit_type>", methods=["GET"])

def get_incidents(unit_type):
    # Create an empty list called 'incidents'
    incidents = []
    # Use 'requests' to make a GET request to the WMATA Incidents API
    response = requests.get(INCIDENTS_URL)
    # Retrieve the JSON data from the response
    data = response.json()

    # Check if there are incidents in the response
    if not data.get("ElevatorIncidents"):
        return json.dumps([])  # Return an empty JSON list if no incidents are found

    # Iterate through the JSON response and retrieve all incidents matching 'unit_type'
    for incident in data.get("ElevatorIncidents", []):
        # Check if the incident's unit type matches the requested unit_type
        if incident.get("UnitType").strip().lower() == unit_type.lower():
            # for each incident, create a dictionary containing the 4 fields from the Module 7 API definition
            incident_info = {
                "StationCode": incident.get("StationCode"), # StationCode
                "StationName": incident.get("StationName"), # StationName
                "UnitName": incident.get("UnitName"),       # UnitType
                "UnitType": incident.get("UnitType")        # UnitName
            }
            # Add each incident dictionary object to the 'incidents' list
            incidents.append(incident_info)

    # Return the list of incident dictionaries using json.dumps
    return json.dumps(incidents)

if __name__ == '__main__':
    app.run(debug=True)