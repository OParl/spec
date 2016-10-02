#!/usr/bin/env bash

set -e

root=$(git rev-parse --show-toplevel)
cd ${root}

# validate schema and examples
res=$(scripts/validate-examples.py)
if [ $? -gt 0 ]
then
  exit 1
fi

# validate tex-template
# TODO: validate tex with lacheck or chktex
