# -*- encoding: utf-8 -*-
import json
import sys
import codecs
import collections
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("action")
parser.add_argument("contributors_json")

args = parser.parse_args()

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

def json_contributors_to_chapters(contributors):
    contributors_md  = u"## Unterstützer {#unterstuetzer}\n\n"
    contributors_md += u"Die folgenden Organisationen und Unternehmen zählen zu den Unterstützern von OParl 1.0:\n\n"
    contributors_md += "Organisation/Firma|Kategorie\n"
    contributors_md += "-----------------------------------------------------------------|-----------\n"

    for supporter in contributors["supporters"]:
        contributors_md += "[%s](%s) | (%s)\n" % (supporter["name"], supporter["website"], supporter["type"])

    authors_md  = "## Autoren {#autoren}\n\n"
    authors_md += "An diesem Dokument haben mitgewirkt:\n\n"

    for author in contributors["authors"][:-1]:
        authors_md += author + ",\n"

    authors_md += contributors["authors"][-1] + "\n"

    return contributors_md + "\n\n" + authors_md

def format_metadata(key, value):
    item = ""

    if isinstance(value, list):
        for v in value:
            item += "%s:\n" % (key)

            item += "- %s: %s\n" % (v.keys()[0], v.values()[0])
            for k in v.keys()[1:]:
                item += "  %s: %s\n" % (k, v[k])

    if isinstance(value, str):
        item = "%s: %s\n" % (key, value)

    return item

def json_contributors_to_info_block(contributors):
    md  = format_metadata("title", "OParl-Spezifikation 1.0 - Entwurf")
    md += format_metadata("rights", "OParl Contributors, CC-BY-SA 4.0")
    md += format_metadata("year", "2015")

    authors = []

    # declare authors as MARC:Author
    for author in contributors["authors"]:
        authors.append({"name": author, "role": "aut"})

    # declare supporters as MARC:Supporting Host
    for supporter in contributors["supporters"]:
        authors.append({"name": supporter["name"], "role": "sht"})

    md += format_metadata("contributor", authors)
    md += "---\n" + md + "...\n"

    md += "Lizenz: [Creative Commons CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)"

    return md

contributors = json.load(codecs.open(args.contributors_json, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)

if args.action == "chapter":
    print(json_contributors_to_chapters(contributors))

if args.action == "infoblock":
    print(json_contributors_to_info_block(contributors))
