#!/usr/bin/env bash

set -e

root=$(git rev-parse --show-toplevel)
export PATH=${PATH}:${root}/vendor/bin/:~/.composer/vendor/bin/
cd ${root}
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
res=$(pandoc -t json *.md | jsonlint)
if [ "$res" != "Valid JSON" ]
then
  retval=1
fi
cd ..

# validate schema and examples
res=$(scripts/validate-examples.py)
if [ $? -gt 0 ]
then
  retval=1
fi

# validate tex-template
# TODO: validate tex with lacheck or chktex

exit $retval
