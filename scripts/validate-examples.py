#!/usr/bin/env python3
"""
Checks for that the right atttribute types are used in the examples of the OParl
spec.

To use this as as library, call validate_object() with the jsob loaded into an
OrderedDict. Requires the schema files of at least version ac8c3b to be in a
`schema/` folder.

Type Mapping:
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
import sys

from collections import OrderedDict

def validate_single_attribut(attribute, value, properties, properties_key):
    """
    Validates one attribute value pair using the schema information given in
    properties. Recursively validates arrays or calls validate_object format
    embedded objects.

    Returns True on succes, False on failure without addional error message
    or a string with an error message
    """
    if not properties_key in properties.keys():
        return "The attribute '" + properties_key + "' is not defined in the schema"

    properties = properties[properties_key]

    property_type = properties["type"]
    if property_type == "boolean":
        if not type(value) == bool:
            return "'" + attribute + "' has the type '" + type(value).__name__ + "' instead of the expected type 'bool'"
    elif property_type == "integer":
        if not type(value) == int:
            return "'" + attribute + "' has the type '" + type(value).__name__ + "' instead of the expected type 'int'"
    elif property_type == "string":
        if not type(value) == str:
            return "'" + attribute + "' has the type '" + type(value).__name__ + "' instead of the expected type 'str'"

        if "format" in properties.keys():
            subtype = properties["format"]
        else:
            return True

        if subtype == "url":
            url = re.compile("(http[s]*://[^\s>\"\)\]`]+[^ >\"`\.\s])")
            if not url.match(value):
                return "'" + value + "' is not a valid url"
        elif subtype == "date":
            date = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
            if not date.match(value):
                return "'" + value + "' is not a valid date"
        elif subtype == "date-time":
            datetime = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}[\+\-][0-9]{2}:[0-9]{2}$")
            if not datetime.match(value):
                return "'" + value + "' is not a valid datetime"
        else:
            return "Invalid string type"
    elif property_type == "object":
        if not type(value) == OrderedDict:
            return "The type '" + type(value).__name__ + "' was found instead of the expected type 'OrderedDict'"

        if not "$ref" in properties.keys():
            print("Note: Not validating " + attribute + " due to the lack of $ref")
            return True

        if not validate_object(value, attribute, properties["$ref"]):
            return False
    elif property_type == "array":
        if not type(value) == list:
            return "'" + attribute + "' has the type '" + type(value).__name__ + "' instead of the expected type 'list'"

        # Check every element of this list by recursive function calls with some debugging information attached
        for i, j in enumerate(value):
            result = validate_single_attribut(attribute + "[" + str(i) + "]", j, properties, "items")
            if result == False:
                return False
            elif type(result) == str:
                return result
    else:
        return "Invalid json type: " + property_type

    return True

def validate_object(target, embedded_object = "", ref = None):
    """
    Validates a whole object using validate_single_attribut and prints every error

    Returns a bool stating wether the object is valid or not
    """
    valid = True

    objects = [i for i in os.listdir("schema")]
    oparl_type = re.compile(r"^https://schema.oparl.org/1.0/([a-zA-Z]+)$").match(target["type"]).group(1)
    for i in objects:
        if i.lower() == oparl_type + ".json":
            schema_file = i

    if ref != None and schema_file != ref:
        print(" - [ ] $ref '" + ref + "' doesn't match actual type '" + target["type"] + "'")

    schema = json.load(open(os.path.join("schema/", schema_file)), object_pairs_hook=OrderedDict)

    for i in schema["required"]:
        if not i in target.keys() or target[i] == None:
            print(" - [ ] Required key " + i + " missing.")

    for attribute, value in target.items():
        result = validate_single_attribut(attribute, value, schema["properties"], attribute)
        if result == True:
            continue

        valid = False
        if type(result) == str:
            if embedded_object == "":
                print(" - [ ] " + result)
            else:
                print(" - [ ] In the embedded object '" + embedded_object + "': " + result)


    return valid

def main():
    all_valid = True
    print("Validating " + str(len(os.listdir("examples"))) + " files ...")
    for file in os.listdir("examples"):
        print("\n#### " + os.path.join("examples", file))
        target = json.load(open(os.path.join("examples", file)), object_pairs_hook=OrderedDict)
        valid = validate_object(target)
        if valid != True:
            all_valid = False

    if all_valid:
        print()
        print(" --- Passed --- ")
        print()
    else:
        print()
        print(" --- Failed --- ")
        print()
        exit(1)

if __name__ == "__main__":
    main()
