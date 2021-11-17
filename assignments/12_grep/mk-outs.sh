#!/usr/bin/env bash

set -u

PRG="./grep.py"
OUTDIR="./expected"
SONNET="./inputs/sonnet-29.txt"
CONST="./inputs/constitution.txt"

[[ ! -d "$OUTDIR" ]] && mkdir -p "$OUTDIR"
rm -f $OUTDIR/*

$PRG weep $SONNET > "$OUTDIR/weep-sonnet.out"
$PRG 'ings?' $SONNET > "$OUTDIR/ings-sonnet.out"

$PRG person $CONST > "$OUTDIR/person-lower-const.out"
$PRG Person $CONST > "$OUTDIR/person-title-const.out"
$PRG PERSON -i $CONST > "$OUTDIR/person-upper-const-i.out"

$PRG king $CONST $SONNET > "$OUTDIR/king-const-sonnet.out"
$PRG king -i $CONST $SONNET > "$OUTDIR/king-const-sonnet-i.out"

