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
args = parser.parse_args()

objects = ["System", "Body", "Organization", "Person", "Meeting", "Paper", "File", "Location"]

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)


def schema_to_md_table(schema, small_heading=False):
    name = schema["title"]

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
        type = prop["type"]

        if isinstance(type, list):
            type = "/".join(type)

        if "oparl:ref" in prop and type == "string":
            type = type + ": " + prop["oparl:ref"] + "-id"
        
        if 'items' in prop:
            if "oparl:ref" in prop and type == "array" and 'type' in prop['items'] and 'format' in prop['items']:
                type = type + " aus " + prop['items']['type'] + "s (" + prop['items']['format'] + ": " + prop["oparl:ref"] + "-ids)"
            elif type == "array" and 'type' in prop['items'] and 'format' in prop['items']:
                type = type + " aus " + prop['items']['type'] + "s (" + prop['items']['format'] + ")"
            elif type == "array" and 'type' in prop['items']:
                type = type + " aus " + prop['items']['type'] + "s"
        
        if "description" in prop:
           description = prop["description"]
        else:
           description = ""

        # eingebettete Objekte finden
        if type == "object" and "properties" in prop:
            embedded_objects.append(prop)

        elif type == "array" and prop["items"]["type"] == "object" and "properties" in prop["items"]:
            embedded_objects.append(prop["items"])

        if "required" in schema and prop_name in schema["required"] and description  != "":
            description =  "**ZWINGEND** " + description

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


for obj in objects:
    filepath = os.path.join(args.schema_folder, obj + ".json")
    print schema_to_md_table(json.load(codecs.open(filepath, encoding='utf-8'), object_pairs_hook=collections.OrderedDict))
