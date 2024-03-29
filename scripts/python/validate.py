import json
import os

import jsonschema
import referencing
import referencing.retrieval
import requests
from referencing import Registry
from referencing.typing import URI

RESOLVE_LOCALLY = True
schema_file = "../../specs/v1/master.schema.json"
json_file = "../../examples/sample.cable.json"

@referencing.retrieval.to_cached_resource()
def mno_retreiver(url):
    if RESOLVE_LOCALLY is True and url.startswith("https://standards.mnoforms.com/"):
        url = url.replace("https://standards.mnoforms.com/", "http://standards.mnoforms.local/")

    resp = requests.get(url)
    return resp.text


# Define the schema
base_dir = os.path.dirname(os.path.abspath(__file__))

schema = json.load(open(os.path.join(base_dir, schema_file)))
data = json.load(open(os.path.join(base_dir, json_file)))

# remove the $schema key from the data to avoid validation error
data.pop("$schema", None)

print("Schema: ", schema)
print("Data: ", data)

try:
    schema_registry = referencing.Registry(retrieve=mno_retreiver)
    jsonschema.validate(instance=data, schema=schema, registry=schema_registry)
    print("JSON data is valid")
except jsonschema.exceptions.ValidationError as ve:
    print("JSON data is invalid", ve)
