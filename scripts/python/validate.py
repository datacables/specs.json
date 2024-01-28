import jsonschema
import json

# Define the schema
schema = json.load(open("../../specs/v1/master.schema.json"))

# Define the JSON data
data = json.load(open("../../examples/sample.json"))

print("Schema: ", schema)
print("Data: ", data)

# Validate the data
try:
    jsonschema.validate(instance=data, schema=schema)
    print("JSON data is valid")
except jsonschema.exceptions.ValidationError as ve:
    print("JSON data is invalid", ve)
