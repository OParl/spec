#!/usr/bin/env sh

root=$(git rev-parse --show-toplevel)
cd ${root}

retval=0

alias jsl="${root}/vendor/bin/jsonlint"

# json-lint all the json
for f in $(find . -type f -name \*.json)
do
  res=$(jsl $f)
  if [ "$res" != "Valid JSON" ]
  then
    retval=1
  fi
done

# validate markdown
cd src
res=$(pandoc -f markdown_strict -t json *.md | jsl)
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
