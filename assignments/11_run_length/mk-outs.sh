#!/usr/bin/env bash

PRG="./run.py"
OUTDIR="./expected"

[[ ! -d "$OUTDIR" ]] && mkdir -p "$OUTDIR"
rm -f $OUTDIR/*

$PRG A > "$OUTDIR/A.out"
$PRG AA > "$OUTDIR/AA.out"
$PRG AAAAA > "$OUTDIR/AAAAA.out"
$PRG ACGT > "$OUTDIR/ACGT.out"
$PRG ACCGGGTTTT > "$OUTDIR/ACCGGGTTTT.out"

$PRG inputs/sample1.txt > "$OUTDIR/sample1.out"
$PRG inputs/sample2.txt > "$OUTDIR/sample2.out"
$PRG inputs/sample3.txt > "$OUTDIR/sample3.out"
