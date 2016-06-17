#!/usr/bin/env bash

export PATH=${PATH}:${root}/vendor/bin/jsonlint:~/.composer/vendor/bin/jsonlint
cd $(git rev-parse --show-toplevel)
retval=0

# json-lint all the json
for f in schema/*.json examples/*.json
do
  res=$(jsonlint $f)
  if [ "$res" != "Valid JSON" ]
  then
    retval=1
  fi
done

# validate markdown
cd src
res=$(pandoc -f markdown_strict -t json *.md | jsonlint)
if [ "$res" != "Valid JSON" ]
then
  retval=1
fi
cd ..

# validate schema and examples
res=$(python scripts/json_schema2markdown.py schema examples)
if [ $? -gt 0 ]
then
  retval=1
fi

# validate tex-template
# TODO: validate tex with lacheck or chktex

exit $retval
