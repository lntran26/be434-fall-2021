#!/usr/bin/env bash

set -u

PRG="./au_pair.py"

$PRG inputs/* -o expected
