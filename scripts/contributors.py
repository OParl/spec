# -*- encoding: utf-8 -*-
import json
import sys
import glob
import codecs
import collections
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("contributors_json")

args = parser.parse_args()

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

def json_contributors_to_chapters(contributors):
    contributors_md = u"## Unterstützer {#unterstuetzer}\n\n"
    contributors_md += u"Die folgenden Organisationen und Unternehmen zählen zu den Unterstützern von OParl 1.0:\n\n"
    contributors_md += "Organisation/Firma|Kategorie\n"
    contributors_md += "-----------------------------------------------------------------|-----------\n"

    for supporter in contributors["supporters"]:
        contributors_md += "[%s](%s) | (%s)" % (supporter["name"], supporter["website"], supporter["type"])

    authors_md = "## Autoren {#autoren}\n\n"
    authors_md += "An diesem Dokument haben mitgewirkt:\n\n"

    for author in contributors["authors"][:-1]:
        authors_md += author + ",\n"

    authors_md += contributors["authors"][-1] + "\n"

    return contributors_md + "\n\n" + authors_md

def json_contributors_to_epub_info(contributors):
    pass

contributors = json.load(codecs.open(args.contributors_json, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)
print(json_contributors_to_chapters(contributors))
