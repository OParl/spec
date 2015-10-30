#!/usr/bin/env sh
# this script is supposed to be run from the repository root
# TODO: make sure that this changes to the repository root

retval=0

alias jsl='~/.composer/vendor/bin/jsonlint'

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

# validate tex-template
# TODO: validate tex with lacheck or chktex

exit $retval
