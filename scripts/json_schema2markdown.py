#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import json
import os
import sys
import glob
import collections
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("schema_folder")
parser.add_argument("examples_folder")
parser.add_argument("output_file")
args = parser.parse_args()

class OParl:
    # Default properties don't need a description
    default_properties = [
        "id",
        "type",
        "license",
        "modified",
        "created",
        "deleted",
        "keyword",
        "web"
    ]
    objects = [
        "System",
        "Body",
        "LegislativeTerm",
        "Organization",
        "Person",
        "Membership",
        "Meeting",
        "AgendaItem",
        "Paper",
        "Consultation",
        "File",
        "Location"
    ]


def type_to_string(prop):
    """
    Converts the json descriptions of the type of any attribute into a human-
    readable string printed in spec
    """
    type = prop["type"]

    # switch over all types
    if type == "object":
        # Check for embedded objects
        if "schema" in prop:
            type = type + " (" + prop["schema"][0:-5] + ")"
    elif type == "string":
        if "format" in prop:
            if "references" in prop:
                type = prop["format"] + " (" + prop["references"] + ")"
            else:
                type = prop["format"]
    elif type == "array":
        items = prop["items"]
        subtype = items["type"]

        # Let's do recursion the copy&paste way
        if items["type"] == "object":
            # Check for embedded objects
            if "schema" in items:
                subtype = subtype + " (" + items["schema"][0:-5] + ")"
        elif items["type"] == "string":
            if "format" in items:
                if "references" in items:
                    subtype = items["format"] + " (" + items["references"] + ")"
                elif "references" in prop:
                    subtype = items["format"] + " (" + prop["references"] + ")"
                else:
                    subtype = items["format"]
        elif type == "boolean":
            pass
        elif type == "integer":
            pass
        else:
            raise Exception("Invalid type: " + type)

        type = type + " of " + subtype
    elif type == "boolean":
        pass
    elif type == "integer":
        pass
    else:
        raise Exception("Invalid type: " + type)

    return type

def schema_to_md_table(schema):
    # Formatting
    propspace = 30
    typespace = 45
    descspace = 80

    # Headline
    md = "## " + schema["title"] + "{#entity-" + schema["title"].lower() + "}" + "\n"

    # Summary/Description
    md += schema["description"] + "\n\n"

    # Table Header
    md += "-"*(propspace + typespace + descspace) + "\n"
    md += "Name" + " " * (propspace - len("Name"))
    md += "Typ" + " " * (typespace - len("Typ"))
    md += "Beschreibung" + " " * (descspace - len("Beschreibung")) + "\n"
    md += "-" * (propspace - 1) + " " + "-" * (typespace - 1) + " " + "-" * (descspace) + "\n"

    # A row for each attribute
    for prop_name, prop in schema["properties"].items():
        type = type_to_string(prop)

        if "description" in prop.keys():
            description = prop["description"]
        elif prop_name in OParl.default_properties:
            description = ""
        else:
            raise Exception(prop_name + " is missing the description property")

        if prop_name in schema["required"] and description != "":
            description = "**ZWINGEND** " + description

        # The actual table row
        md += "`"+ prop_name + "`" + " " * (propspace - len(prop_name)) + type + " " * (typespace - len(type)) + description + "\n\n"

    # End of Table
    md += "-" * (propspace + typespace + descspace) + "\n\n"

    md += json_examples_to_md(schema["title"])
    return md


def json_examples_to_md(name):
    md = ""
    filepath = os.path.join(args.examples_folder, name)
    examples = glob.glob(filepath + "-[0-9][0-9].json")
    for nr, examplepath in enumerate(examples):
        if len(examples) == 1:
            md += "**Beispiel**\n\n"
        else:
            md += "**Beispiel " + str(nr + 1) + "**\n\n"

        example = json.load(open(examplepath), object_pairs_hook=collections.OrderedDict)
        md += "~~~~ {.json}\n"
        md += json.dumps(example, ensure_ascii=False, indent=4) + "\n"
        md += "~~~~\n\n"
        md += "\pagebreak\n"
        md += "\n"

    return md

def main():
    generated_schema = ""

    # Avoid missing objects
    assert(len(OParl.objects) == len(os.listdir(args.schema_folder)))

    for obj in OParl.objects:
        filepath = os.path.join(args.schema_folder, obj + ".json")
        print("Processing " + filepath)
        schema = schema_to_md_table(json.load(open(filepath), object_pairs_hook=collections.OrderedDict))
        generated_schema += schema

    with open(args.output_file, "w") as out:
        out.write(generated_schema)

if __name__ == "__main__":
    main()
