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
import os
import re
import subprocess
from collections import OrderedDict


class Validate:
    def __init__(self):
        self.schema = self.load_schema()

    @staticmethod
    def load_schema():
        schema = {}

        for i in os.listdir("schema"):
            if not i.endswith(".json"):
                continue
            with open(os.path.join("schema", i), encoding='utf-8') as fp:
                content = json.load(fp, object_pairs_hook=OrderedDict)
                schema[content["title"]] = content

        return schema

    def validate_entry(self, attribute, value, properties, properties_key):
        """
        Validates one attribute value pair using the schema information given in
        properties. Recursively validates arrays or calls validate_object format
        embedded objects.

        :param attribute The key or key with array index of this entry for printing messages
        :param value The value of this entry
        :param properties The schema for the object from which the entry originates
        :param properties_key The key without array index for indexing the properties
        :return (bool, [string]) Returns a tuple of a bool stating wether the entry is valid or not and a list of
         messages
        with the errors or notes
        """
        # Skip vendor specific attributes
        if ":" in properties_key:
            return True, "Note: Not validating the vendor specific attribute " + properties_key

        if properties_key not in properties.keys():
            return False, "The attribute is not defined in the schema"

        properties = properties[properties_key]

        messages_from_embedded_objects = []

        result = None
        property_type = properties["type"]
        if property_type == "boolean":
            if not type(value) == bool:
                result = False, "The type '" + type(value).__name__ + "' was found instead of the expected type 'bool'"
        elif property_type == "integer":
            if not type(value) == int:
                result = False, "The type '" + type(value).__name__ + "' was found instead of the expected type 'int'"
        elif property_type == "string":
            result = self.property_string(value, properties)
        elif property_type == "object":
            result = self.property_object(attribute, properties, value)
        elif property_type == "array":
            result = self.property_array(attribute, properties, value, messages_from_embedded_objects)
        else:
            result = False, "Invalid json type: " + property_type

        if result:
            return result
        else:
            return True, messages_from_embedded_objects

    def property_object(self, attribute, properties, value):
        if not type(value) == OrderedDict:
            return False, "The type '" + type(
                value).__name__ + "' was found instead of the expected type 'OrderedDict'"
        if "schema" not in properties.keys():
            return True, "Note: Not validating " + attribute + " due to the lack of schema"
        return self.validate_object(value, attribute, properties["schema"])

    def property_array(self, attribute, properties, value, messages_from_embedded_objects):
        if not type(value) == list:
            return False, "The type  '" + type(value).__name__ + "' was found instead of the expected type 'list'"

        # Check every element of this list by recursive function calls with some debugging information attached
        for i, j in enumerate(value):
            valid, message = self.validate_entry(attribute + "[" + str(i) + "]", j, properties, "items")
            if not valid:
                return valid, message
            if message != "":
                message = message if type(message) == list else [message]
                messages_from_embedded_objects += message

    @staticmethod
    def property_string(value, properties):
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

    def validate_object(self, target, embedded_object="", ref=None):
        """
        Validates a whole object using validate_entry and prints every error

        :param target The object to be validated
        :param embedded_object The key of the corresponding if this is an embedded object. Used for better messages
        :param ref The expected type
        :return (bool, [string]) Returns a tuple of a bool stating wether the object is valid or not and a list of
        messages
        with the errors or notes
        """
        valid = True
        messages = []

        oparl_type = re.compile(r"^https://schema.oparl.org/1.1/([a-zA-Z]+)$").match(target["type"]).group(1)
        schema = self.schema[oparl_type]

        if ref and schema["title"] + ".json" != ref:
            messages.append(" - [ ] schema '" + ref + "' doesn't match actual type '" + target["type"] + "'")
            valid = False

        for i in schema["required"]:
            if i not in target.keys() or not target[i]:
                messages.append(" - [ ] Required key " + i + " missing.")

        for attribute, value in target.items():
            attribut_valid, message = self.validate_entry(attribute, value, schema["properties"], attribute)
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

    def run(self):
        all_valid = True
        print("Validating " + str(len(os.listdir("examples"))) + " files ...")
        for file in os.listdir("examples"):
            print("\n#### " + os.path.join("examples", file))
            target = json.load(open(os.path.join("examples", file), encoding='utf-8'), object_pairs_hook=OrderedDict)
            valid, messages = self.validate_object(target)
            if not valid:
                all_valid = False
            for i in messages:
                print(i)

        if all_valid:
            print("\n --- Passed --- \n")
        else:
            print("\n --- Failed --- \n")
            exit(1)


def main():
    git_root = subprocess.getoutput("git rev-parse --show-toplevel")
    os.chdir(git_root)
    Validate().run()


if __name__ == "__main__":
    main()
