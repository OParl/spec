#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import argparse
import collections
import glob
import json
import os

import yaml


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
        subtype = array_type_to_string(prop, type)

        type = type + " of " + subtype
    elif type == "boolean":
        pass
    elif type == "integer":
        pass
    else:
        raise Exception("Invalid type: " + type)

    return type


def array_type_to_string(prop, type):
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
    return subtype


def schema_to_md_table(schema, examples_folder):
    # Formatting
    propspace = 30
    typespace = 45
    descspace = 80

    # Headline
    md = "## " + schema["title"] + "{#entity-" + schema["title"].lower() + "}" + "\n"

    # Summary/Description
    md += schema["description"] + "\n\n"

    # Table Header
    md += "-" * (propspace + typespace + descspace) + "\n"
    md += "Name" + " " * (propspace - len("Name"))
    md += "Typ" + " " * (typespace - len("Typ"))
    md += "Beschreibung" + " " * (descspace - len("Beschreibung")) + "\n"
    md += "-" * (propspace - 1) + " " + "-" * (typespace - 1) + " " + "-" * (descspace) + "\n"

    md = table_body(propspace, schema, typespace)

    # End of Table
    md += "-" * (propspace + typespace + descspace) + "\n\n"

    md += json_examples_to_md(examples_folder, schema["title"])
    return md


def table_body(propspace, schema, typespace):
    md = ""
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
        md += "`" + prop_name + "`" + " " * (propspace - len(prop_name)) + type + " " * (
            typespace - len(type)) + description + "\n\n"
    return md


def json_examples_to_md(examples_folder, name):
    md = ""
    filepath = os.path.join(examples_folder, name)
    examples = glob.glob(filepath + "-[0-9][0-9].json")
    for nr, examplepath in enumerate(examples):
        # TODO: localize examples
        if len(examples) == 1:
            md += "**Beispiel**\n\n"
        else:
            md += "**Beispiel " + str(nr + 1) + "**\n\n"

        example = json.load(open(examplepath, encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
        md += "~~~~ {.json}\n"
        md += json.dumps(example, ensure_ascii=False, indent=4) + "\n"
        md += "~~~~\n\n"
        md += "\pagebreak\n"
        md += "\n"

    return md


def localize_schema(language, translations_file, schema_file):
    """
    Replaces the handlebars/django style templates in the schema files with the translations stored in
    `translations_file`. The keys used the templates resemble JSONPath
    """
    schema = schema_file.read()

    with open(translations_file) as f:
        translations = yaml.load(f)["de"]

    for key in translations.keys():
        pattern = "{{ " + key + " }}"  # Avoid mixing python's and our own template language
        if schema.find(pattern):
            translation = json.dumps(translations[key], ensure_ascii=False)[1:-1]
            schema = schema.replace(pattern, translation)

    return json.loads(schema, object_pairs_hook=collections.OrderedDict)


def schema_to_markdown(schema_folder, examples_folder, output_file, language, language_file):
    # Avoid missing objects
    # NOTE: the schema folder contains all schema files and the translations strings file
    assert (len(OParl.objects) == len(os.listdir(schema_folder)) - 1)

    generated_schema = ""

    for obj in OParl.objects:
        filepath = os.path.join(schema_folder, obj + ".json")

        with open(filepath, encoding='utf-8') as file_handle:
            schema_json = localize_schema(language, language_file, file_handle)

        schema = schema_to_md_table(schema_json, examples_folder)

        generated_schema += schema

    with open(output_file, "w", encoding='utf-8') as out:
        out.write(generated_schema)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("schema_folder")
    parser.add_argument("examples_folder")
    parser.add_argument("output_file")
    parser.add_argument("language")
    parser.add_argument("language_file")

    args = parser.parse_args()

    schema_to_markdown(args.schema_folder, args.examples_folder, args.output_file, args.language, args.language_file)
