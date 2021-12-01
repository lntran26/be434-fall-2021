#!/usr/bin/env bash

PRG="./tac.py"
OUTDIR="./expected"
[[ ! -f "$OUTDIR" ]] && mkdir -p "$OUTDIR"

for FILE in ./inputs/*; do
    $PRG $FILE > $OUTDIR/$(basename "$FILE").out
done

ALL="./inputs/empty.txt ./inputs/one.txt ./inputs/ten.txt"
$PRG $ALL > $OUTDIR/all.out
