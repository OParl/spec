#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import json
import os
import sys
import glob
import codecs
import collections
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("schema_folder")
parser.add_argument("examples_folder")
parser.add_argument("output_file")
args = parser.parse_args()

objects = ["System", "Body", "Organization", "Person", "Meeting", "Paper", "File", "Location"]

# FIXME: Does this have any use?
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)
#sys.stderr = codecs.getwriter('utf8')(sys.stderr)

def err(msg):
    sys.stderr.write(msg + "\n")

def missing_property(prop_name, prop):
    err(prop_name + " is missing the " + prop + " property")

def schema_to_md_table(schema, small_heading=False):
    try:
        name = schema["title"]
    except:
        err("Schema does not have required title attribute")
        raise

    if small_heading:
        md = "###" + name + "###\n\n"
    else:
        md = "## " + name + "{#entity-" + name.lower() + "}" + "\n"

    # Zeichenlängen der drei Spalten
    propspace = 30
    typespace = 45
    descspace = 80

    if "description" in schema:
        md += schema["description"] + "\n"

    md += "\n"

    # Tabellenkopf
    md += "-"*(propspace + typespace + descspace) + "\n"
    md += "Name" + " "*(propspace - len("Name")) + "Typ" + " "*(typespace - len("Typ")) + "Beschreibung" +" "*(descspace - len("Beschreibung")) + "\n"
    md += "-"*(propspace - 1) + " " + "-"*(typespace - 1)+ " " + "-"*(descspace) + "\n"

    embedded_objects= []

    for prop_name, prop in schema["properties"].items():
        try:
            type = prop["type"]
        except:
            missing_property(prop_name, "type")
            raise

        if type not in ["object", "array", "string", "date-time", "boolean", "integer"]:
            err("Invalid type: " + type)
            raise Exception

        # eingebettete Objekte finden
        if type == "object" and "properties" in prop:
            embedded_objects.append(prop)

        elif type == "object":
            if "title" in prop:
                type = type + " (" + prop["title"] + ")"
            elif "$ref" in prop:
                type = type + " (" + prop['$ref'][0:-5] + ")"

        elif type == "array" and prop["items"]["type"] == "object" and "properties" in prop["items"]:
            embedded_objects.append(prop["items"])

        if isinstance(type, list):
            type = "/".join(type)

        if "oparl:ref" in prop and type == "string" and 'format' in prop:
            type = prop['format'] + " (" + prop["oparl:ref"] + ")"
        elif type == "string" and 'format' in prop:
            type = prop['format']

        if 'items' in prop:
            if "oparl:ref" in prop and type == "array" and 'type' in prop['items'] and 'format' in prop['items']:
                type = type + " of " + prop['items']['format'] + " (" + prop["oparl:ref"] + ")"
            elif type == "array" and 'type' in prop['items'] and 'format' in prop['items']:
                type = type + " of " + prop['items']['format']
            elif type == "array" and 'type' in prop['items']:
                if "title" in prop['items'] and "type" in prop['items']:
                    if prop['items']["type"] == "object":
                        type = type + " of " + prop['items']['type'] + " (" + prop['items']['title'] + ")"
                    else:
                        type = type + " of " + prop['items']['type']
                elif "$ref" in prop['items']:
                    type = type + " of " + prop['items']['type'] + " (" + prop['items']['$ref'][0:-5] + ")"
                else:
                    type = type + " of " + prop['items']['type']

        try:
            description = prop["description"]
        except:
            if prop_name not in ["id", "type", "modified", "created", "deleted", "keyword", "web"]:
                missing_property(prop_name, "description")
                raise
            else:
                description = ""

        if "required" in schema and prop_name in schema["required"] and description != "":
            description = "**ZWINGEND** " + description

        md += "`"+ prop_name + "`" + (propspace - len(prop_name))*u" " + type + (typespace - len(type))*u" " + description + "\n\n"

    # Tabellenende
    md += "-"*(propspace + typespace + descspace) + "\n\n"

    # eingebettete Objekte in einer eigenen Tabelle ausgeben
    for obj in embedded_objects:
        md += schema_to_md_table(obj, small_heading=True)

    md += json_examples_to_md(name)
    return md


def json_examples_to_md(name):
    md = ""
    filepath = os.path.join(args.examples_folder, name)
    examples = glob.glob(filepath + '-[0-9][0-9].json')
    for nr, examplepath in enumerate(examples):
        if len(examples) == 1:
            md += "**Beispiel**\n\n"
        else:
            md += "**Beispiel " + str(nr + 1) + "**\n\n"

        example = json.load(codecs.open(examplepath, encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
        md += "~~~~ {.json}\n"
        md += json.dumps(example, ensure_ascii=False, indent=4) + "\n"
        md += "~~~~\n\n"
        md += "\pagebreak\n"
        md += "\n"

    return md

def main():
    full_schema = ""

    for obj in objects:
        filepath = os.path.join(args.schema_folder, obj + ".json")
        schema = schema_to_md_table(json.load(codecs.open(filepath, encoding='utf-8'), object_pairs_hook=collections.OrderedDict))

        full_schema += schema

    with open(args.output_file, 'w') as out:
        out.write(full_schema)

if __name__ == "__main__":
    main()
