import json
import glob
import logging
from datetime import datetime

# Configure logging file to track output
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("fhir_light_validation.log"),
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

def validate_patient(resource):
    errors = []
    warnings = []

    # Validate gender
    if resource.get("gender") not in ["male", "female", "other", "unknown"]:
        errors.append("Invalid gender")

    # Validate birthDate
    birth_date = resource.get("birthDate")
    if birth_date:
        try:
            datetime.strptime(birth_date, "%Y-%m-%d")
        except ValueError:
            errors.append("Invalid birthDate format")

    return errors, warnings

def validate_encounter(resource):
    errors = []
    warnings = []

    # Validate subject reference
    if not resource.get("subject") or not resource["subject"].get("reference"):
        errors.append("Missing subject reference")

    # Validate period
    period = resource.get("period")
    if period:
        start = period.get("start")
        end = period.get("end")
        if start and end:
            try:
                start_date = datetime.fromisoformat(start)
                end_date = datetime.fromisoformat(end)
                if start_date > end_date:
                    errors.append("period.start is after period.end")
            except ValueError:
                errors.append("Invalid period date format")

    return errors, warnings

def validate_bundle(resource):
    errors = []
    warnings = []

    entries = resource.get("entry", [])
    for entry in entries:
        subres = entry.get("resource")
        if subres:
            e, w = validate_resource(subres)
            errors.extend(e)
            warnings.extend(w)

    return errors, warnings

def validate_resource(resource):
    resource_type = resource.get("resourceType")
    if not resource_type:
        return ["Resource has no resourceType field"], []

    if resource_type == "Patient":
        return validate_patient(resource)
    elif resource_type == "Encounter":
        return validate_encounter(resource)
    elif resource_type == "Bundle":
        return validate_bundle(resource)
    else:
        return [], ["Resource type not specifically validated"]

# Adjust the path as needed
json_files = glob.glob("tests/synthea_sample_data_fhir_latest/*.json")

total_resources = 0
passed_resources = 0
failed_resources = 0

for file in json_files:
    resource = load_fhir_resource(file)
    total_resources += 1
    errors, warnings = validate_resource(resource)
    if errors:
        failed_resources += 1
        logging.error(f"Resource {total_resources} (type={resource.get('resourceType')}) => {len(errors)} errors, {len(warnings)} warnings")
        for error in errors:
            logging.error(f"  Error: {error}")
        for warning in warnings:
            logging.warning(f"  Warning: {warning}")
    else:
        passed_resources += 1
        logging.info(f"Resource {total_resources} (type={resource.get('resourceType')}) => {len(errors)} errors, {len(warnings)} warnings")
        for warning in warnings:
            logging.warning(f"  Warning: {warning}")

logging.info(f"Summary: {passed_resources} resources passed, {failed_resources} resources failed out of {total_resources} total resources")