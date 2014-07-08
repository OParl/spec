#encoding utf8

import sys
import re

pattern = re.compile("(http[s]*://[^\s>\"\)\]`]+[^ >\"`\.\s])")

def extract_urls(path):
	f = open(path, "rb")
	content = f.read()
	f.close()
	urls = re.findall(pattern, content)
	return urls

if __name__ == "__main__":
	urls = set()
	for path in sorted(sys.argv):
		this_urls = extract_urls(path)
		for url in this_urls:
			urls.add(url)
	for url in sorted(list(urls)):
		print url
