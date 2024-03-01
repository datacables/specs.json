## datacables.io / specs.json Schema Documentation
`(original name - mnoforms.com)`

This document explains the **Datacables Specifications**, a JSON Schema-based approach for defining data structures that can be efficiently used for both data representation and communication. The speficiation aims to achieve this by separating data structure and definition standards and leveraging references to sub-schemas.

### Introduction

**Datacables Speficiations** aim to streamline data management by providing a standardized way to describe data structures using JSON Schema. This schema separates concerns, allowing for:

* Defining the core data structure of the information.
* Specifying validation rules to ensure data integrity.
* (Optional) Establishing rules for data transformation during serialization/deserialization (not covered in detail here).

This separation enables seamless communication between data storage systems, APIs, and applications that utilize the same schema foundation.

### Founder's Belief: Isolated and Asynchronous Communication
The Datacables schema is heavily influenced by the founder's belief in promoting loosely coupled and asynchronous communication within software systems. 
[Details explained here - PRINCIPLE.md](.project/docs/PRINCIPLE.md)

### Core Concepts

The **Datacables Specifications**  utilizes a modular approach with several key components:

1. **Main Schema (`master.schema.json`)** [master.schema.json](https://standards.mnoforms.com/specs/v1/master.schema.json)
    * `master.schema.json` Defines the overall structure of a standard communication cable.
    * Includes references to sub-schemas for specific functionalities.
    * Enforces stricter validation using `additionalProperties: false`.

2. **Form Schema (`form.schema.json`)** [form.schema.json](https://standards.mnoforms.com/specs/v1/form.schema.json)
    * (Terminology kept for consistency with existing schema references) Defines the actual data fields and their data types.
    * References the `field.schema.json` schema for individual field definitions.

3. **Field Schema (`field.schema.json`)** [field.schema.json](https://standards.mnoforms.com/specs/v1/field.schema.json)
    * Defines the structure of individual data fields.
    * Separates data definition (`type`), and validation (`validators`).
    * Field emphasizes on the data type, but not necessarily on how it renders. HTML rendering is defined separately.

4. **Layout Schema (`layout.schema.json`)** [layout.schema.json](https://standards.mnoforms.com/specs/v1/layout.schema.json)
    * TODO    
    
5. **Rule Schema (`rule.schema.json`)** [rule.schema.json](https://standards.mnoforms.com/specs/v1/rule.schema.json)
    * TODO 
    * Could define rules for data transformation during serialization/deserialization but not core data structure.

**Catch-all Properties:**

Both the main schema and form schema include optional catch-all properties (`meta` and `extras`) to store additional information that doesn't directly affect core functionalities.
These properties are kept for the higher portability scope of the communication cable. However, structure for `meta` and `extras` will be also be suggested in later version, not to make the properties too generic to compromise the whole datacable convention.

### Schema Breakdown

**Main Schema** [master.schema.json](specs/v1/master.schema.json)

```json
{
  "$schema": "...",
  "$id": "...",
  "title" : "a standard communication cable specification",
  "description": "...",
  "type": "object",
  "properties": {
    "meta": {  },
    "form": { "$ref": "https://standards.mnoforms.com/specs/v1/form.schema.json" },
    "extras": {  }
  },
  "required": ["form"]
}
```

**Form Schema** [form.schema.json](specs/v1/form.schema.json)

```json
{
  "$schema": "...",
  "$id": "...",
  "title": "mnoforms : Specification for Data Cable",
  "description": "...",
  "type": "object",
  "properties": {
    "meta": {  },
    "fields": {
      "type": "array",
      "items": { "$ref": "https://standards.mnoforms.com/specs/v1/field.schema.json" }
    },
    "extras": {  }
  }
}
```

**Field Schema** [field.schema.json](specs/v1/field.schema.json)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://standards.mnoforms.com/specs/v1/field.schema.json",
  "title": "mnoforms : Form field",
  "type": "object",
  "properties": {
    "meta": {
      "type": "object",
      "additionalProperties": true
    },
    "name": {
      "type": "string"
    },
    "label": {
      "type": "string"
    },
    "type": {
      "type": "string",
      "default": "string",
      "enum": ["text", "number", "email", "..."]
    },
    "default": {
      "type": "string"
    },
    "attributes": {
      "type": "object",
      "properties": {
        "is_required": {
          "type": "boolean"
        },
        "is_null": {
          "type": "boolean"
        }
      }
    },
    "render": {
      "type": "object",
      "properties": {
        "input": {
          "type": "string",
          "enum": ["text", "number", "email", "..."]
        },
        "placeholder": {
          "type": "string"
        }
      }
    },
    "choices": {
      "type": "array",
      "items": {
        "anyOf": [
          {"type": "string"},
          {
            "type": "object",
            "properties": {
              "value": {"type": "string"},
              "label": {"type": "string"}
            },
            "required": ["value", "label"]
          }
        ]
      }
    },
    "validators": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "function": {"type": "string"},
          "message": {"type": "string"},
          "params": {"type": "object"}
        },
        "required": ["function"]
      }
    },
    "extras": {
      "type": "object",
      "additionalProperties": true
    }
  },
  "required": ["name", "type"]
}
```
