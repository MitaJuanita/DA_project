import json
import glob
import logging

# If you plan to configure an actual FHIR client, you might need something like:
# from fhirclient import client  
# from fhirclient import client

from fhirclient.models.patient import Patient
from fhirclient.models.bundle import Bundle
from fhirclient.models.diagnosticreport import DiagnosticReport
from fhirclient.models.encounter import Encounter
from fhirclient.models.condition import Condition
# from fhirclient.models.observation import Observation  # Uncomment if you need Observations

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("fhir_validation.log"),
        logging.StreamHandler()
    ]
)

def load_fhir_resource(file_path):
    """
    Loads a JSON file and returns it as a Python dict.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def validate_resource(resource):
    """
    Given a Python dict representing a FHIR resource, instantiate the appropriate
    fhirclient model and call .is_valid(). Returns True/False.
    """
    resource_type = resource.get("resourceType")

    # If resourceType is missing, automatically fail
    if not resource_type:
        logging.error("Resource has no resourceType field.")
        return False

    try:
        if resource_type == "Patient":
            return Patient(resource).is_valid()
        elif resource_type == "Bundle":
            bundle = Bundle(resource)
            for entry in bundle.entry:
                if not validate_resource(entry.resource):
                    return False
            return True
        elif resource_type == "DiagnosticReport":
            return DiagnosticReport(resource).is_valid()
        elif resource_type == "Encounter":
            return Encounter(resource).is_valid()
        elif resource_type == "Condition":
            return Condition(resource).is_valid()
        # elif resource_type == "Observation":
        #     return Observation(resource).is_valid()
        else:
            logging.warning(f"Unknown or unhandled resource type: {resource_type}")
            return False
    except Exception as e:
        logging.error(f"Error validating resource of type {resource_type}: {e}")
        return False

# Adjust the path as needed
json_files = glob.glob("tests/synthea_sample_data_fhir_latest/*.json")

for file in json_files:
    resource = load_fhir_resource(file)
    is_valid = validate_resource(resource)
    logging.info(f"File: {file}, ResourceType: {resource.get('resourceType')} -> is_valid: {is_valid}")
