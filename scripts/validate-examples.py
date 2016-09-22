#!/usr/bin/env python3
"""
Checks for that the right atttribute types are used in the examples.

To use this as as library, call validate_object() with the jsob loaded into an
OrderedDict.
"""


import json
import re
import os
import sys

from collections import OrderedDict

def validate_single_attribut(attribute, value, properties):
    """
    Validates one attribute value pair using the schema information given in
    properties. Recursively validates arrays or calls validate_object format
    embedded objects.

    Returns True on succes and a String with the error message in case of a failure
    """
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
                return "'" + value + "' is not a valid date as of ISO 8601"
        elif subtype == "date-time":
            datetime = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}[\+\-][0-9]{2}:[0-9]{2}$")
            if not datetime.match(value):
                return "'" + value + "' is not a valid datetime as of ISO 8601"
        else:
            return "Invalid string type"
    elif property_type == "array":
        if not type(value) == list:
            return "'" + attribute + "' has the type '" + type(value).__name__ + "' instead of the expected type 'list'"

        # Check every element of this list by recursive function calls with some debugging information attached
        for i, j in enumerate(value):
            if False and validate_single_attribut(attribute + "[" + str(i) + "]", j, properties["items"]) != True:
                return "The list '" + attribute + "' has an invalid embedded object"
    elif property_type == "object":
        if not type(value) == OrderedDict:
            return "'" + attribute + "' has the type '" + type(value).__name__ + "' instead of the expected type 'OrderedDict'"

        # Got an object, so let's validate it
        if not validate_object(value):
            return "The embedded object '" + attribute + "' is invalid"
    else:
        return "Invalid json type: " + property_type

    return True

def validate_object(target):
    """
    Validates a whole object using validate_single_attribut and prints every error

    Returns a bool stating wether the object is valid or not
    """
    valid = True
    oparl_type = re.compile(r"^https://schema.oparl.org/1.0/([a-zA-Z]+)$").match(target["type"]).group(1).title()
    schema = json.load(open("schema/" + oparl_type + ".json"), object_pairs_hook=OrderedDict)

    for i in schema["required"]:
        if not i in target.keys() or target[i] == None:
            return "Required key " + i + " missing."

    for (key, value) in target.items():
        if not key in schema["properties"].keys():
            print("The attribute '" + key + "' is undefined")
            valid = False
            continue

        result = validate_single_attribut(key, value, schema["properties"][key])
        if result != True:
            print(result)
            valid = False

    return valid

def main():
    for file in os.listdir("examples"):
        print(" --- " + file + " --- ")
        target = json.load(open(os.path.join("examples", file)), object_pairs_hook=OrderedDict)
        valid = validate_object(target)
        if valid:
            print("Passed")
        else:
            print("Failed")

if __name__ == "__main__":
    main()
