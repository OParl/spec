#!/usr/bin/env python3
"""
Checks for that the right atttribute types are used in the examples of the OParl
spec.

To use this as as library, call validate_object() with the jsob loaded into an
OrderedDict. Requires the schema files of at least version ac8c3b to be in a
`schema/` folder.

### Type Mapping
----------------------------
| OParl JSON | Python      |
----------------------------
| object     | OrderedDict |
| array      | list        |
| string     | str         |
| boolean    | bool        |
| int        | int         |
----------------------------
"""

import json
import re
import os

from collections import OrderedDict


def validate_entry(attribute, value, properties, properties_key):
    """
    Validates one attribute value pair using the schema information given in
    properties. Recursively validates arrays or calls validate_object format
    embedded objects.

    :param attribute The key or key with array index of this entry for printing messages
    :param value The value of this entry
    :param properties The schema for the object from which the entry originates
    :param properties_key The key without array index for indexing the properties
    :return (bool, [string]) Returns a tuple of a bool stating wether the entry is valid or not and a list of messages
    with the errors or notes
    """
    # Skip vendor specific attributes
    if ":" in properties_key:
        return True, "Note: Not validating the vendor specific attribute " + properties_key

    if properties_key not in properties.keys():
        return False, "The attribute is not defined in the schema"

    properties = properties[properties_key]

    messages_from_embedded_objects = []

    property_type = properties["type"]
    if property_type == "boolean":
        if not type(value) == bool:
            return False, "The type '" + type(value).__name__ + "' was found instead of the expected type 'bool'"
    elif property_type == "integer":
        if not type(value) == int:
            return False, "The type '" + type(value).__name__ + "' was found instead of the expected type 'int'"
    elif property_type == "string":
        if not type(value) == str:
            return False, "The type '" + type(value).__name__ + "' was found instead of the expected type 'str'"

        # String mean different types of String, defined by format
        if "format" in properties.keys():
            subtype = properties["format"]
        else:
            return True, ""

        if subtype == "url":
            url = re.compile("(http[s]*://[^\s>\")\]`]+[^ >\"`.\s])")
            if not url.match(value):
                return False, "'" + value + "' is not a valid url"
        elif subtype == "date":
            date = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
            if not date.match(value):
                return False, "'" + value + "' is not a valid date"
        elif subtype == "date-time":
            datetime = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}[+-][0-9]{2}:[0-9]{2}$")
            if not datetime.match(value):
                return False, "'" + value + "' is not a valid datetime"
        else:
            return "Invalid string type"
    elif property_type == "object":
        if not type(value) == OrderedDict:
            return False, "The type '" + type(value).__name__ + "' was found instead of the expected type 'OrderedDict'"

        if "schema" not in properties.keys():
            return True, "Note: Not validating " + attribute + " due to the lack of schema"

        return validate_object(value, attribute, properties["schema"])
    elif property_type == "array":
        if not type(value) == list:
            return False, "The type  '" + type(value).__name__ + "' was found instead of the expected type 'list'"

        # Check every element of this list by recursive function calls with some debugging information attached
        for i, j in enumerate(value):
            valid, message = validate_entry(attribute + "[" + str(i) + "]", j, properties, "items")
            if not valid:
                return valid, message
            if message != "":
                message = message if type(message) == list else [message]
                messages_from_embedded_objects += message
    else:
        return False, "Invalid json type: " + property_type

    return True, messages_from_embedded_objects


def validate_object(target, embedded_object="", ref=None, schema=None):
    """
    Validates a whole object using validate_entry and prints every error

    :param target The object to be validated
    :param embedded_object The key of the corresponding if this is an embedded object. Used for better messages
    :param ref The expected type
    :param schema
    :return (bool, [string]) Returns a tuple of a bool stating wether the object is valid or not and a list of messages
    with the errors or notes
    """
    valid = True
    messages = []

    oparl_type = re.compile(r"^https://schema.oparl.org/1.0/([a-zA-Z]+)$").match(target["type"]).group(1)
    objects = [i for i in os.listdir("schema")]
    for i in objects:
        if i == oparl_type + ".json":
            schema_file = i
            break
    else:
        messages.append(" - [ ] Unknown object type " + oparl_type + ". Skipping object " + embedded_object)
        return False

    if ref and schema_file != ref:
        messages.append(" - [ ] schema '" + ref + "' doesn't match actual type '" + target["type"] + "'")
        valid = False

    if not schema:
        schema = json.load(open(os.path.join("schema/", schema_file), encoding='utf-8'), object_pairs_hook=OrderedDict)
    else:
        schema = schema[oparl_type]

    for i in schema["required"]:
        if i not in target.keys() or not target[i]:
            messages.append(" - [ ] Required key " + i + " missing.")

    for attribute, value in target.items():
        attribut_valid, message = validate_entry(attribute, value, schema["properties"], attribute)
        if attribut_valid:
            pass
        else:
            valid = False

        message = message if type(message) == list else [message]

        for i in message:
            if i == "":
                continue

            if embedded_object == "":
                messages.append(" - [ ] '" + attribute + "': " + i)
            else:
                messages.append("In the embedded object '" + embedded_object + "': '" + attribute + "': " + i)

    return valid, messages


def main():
    all_valid = True
    print("Validating " + str(len(os.listdir("examples"))) + " files ...")
    for file in os.listdir("examples"):
        print("\n#### " + os.path.join("examples", file))
        target = json.load(open(os.path.join("examples", file), encoding='utf-8'), object_pairs_hook=OrderedDict)
        valid, messages = validate_object(target)
        if not valid:
            all_valid = False
        for i in messages:
            print(i)

    if all_valid:
        print("\n --- Passed --- \n")
    else:
        print("\n --- Failed --- \n")
        exit(1)


if __name__ == "__main__":
    main()
