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

objects = ["System", "Body", "Organization", "Person", "Meeting", "AgendaItem", "Paper", "File", "Consultation", "Location", "Membership", "LegislativeTerm"]

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)


def schema_to_md_table(schema):
    name = schema["title"]
    md = "## " + name + "\n"

    # Zeichenlängen der drei Spalten
    propspace = 26
    typespace = 30
    descspace = 80

    if "description" in schema:
        md += schema["description"] + "\n"

    md += "\n"

    # Tabellenkopf
    md += "-"*(propspace + typespace + descspace) + "\n"
    md += "Name" + " "*(propspace - len("Name")) + "Typ" + " "*(typespace - len("Typ")) + "Beschreibung" +" "*(descspace - len("Beschreibung")) + "\n"
    md += "-"*(propspace - 1) + " " + "-"*(typespace - 1)+ " " + "-"*(descspace) + "\n"

    for prop_name, prop in schema["properties"].items():
        type = prop["type"]

        if isinstance(type, list):
            type = "/".join(type)

        if "oparl:ref" in prop and type == "string":
            type = type + ": " + prop["oparl:ref"] + "-id"

        if "oparl:ref" in prop and type == "array":
            type = type + ": " + prop["oparl:ref"] + "-ids"

        if "description" in prop:
           description = prop["description"]
        else:
           description = ""

        if "required" in schema and prop_name in schema["required"] and description  != "":
            description =  "**ZWINGEND** " + description

        if "oparl:optional" in schema and prop_name in schema["oparl:optional"] and description != "":
            description =  "*OPTIONAL* " + description

        md += "`"+ prop_name + "`" + (propspace - len(prop_name))*u" " + type + (typespace - len(type))*u" " + description + "\n\n"

    # Tabellenende
    md += "-"*(propspace + typespace + descspace) + "\n\n"

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

