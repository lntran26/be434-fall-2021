#!/usr/bin/env bash

set -u

PRG="./kmers.py"
OUTDIR="./expected"
FOO="./inputs/foo.txt"
BAR="./inputs/bar.txt"
AMERICAN="./inputs/american.txt"
BRITISH="./inputs/british.txt"
SAMPLE1="./inputs/sample1.txt"
SAMPLE2="./inputs/sample2.txt"

[[ ! -d "$OUTDIR" ]] && mkdir -p "$OUTDIR"

$PRG $FOO $BAR > $OUTDIR/foo_bar
$PRG $FOO $BAR -k 1 > $OUTDIR/foo_bar.k1
$PRG $FOO $BAR -k 2 > $OUTDIR/foo_bar.k2
$PRG $FOO $BAR -k 4 > $OUTDIR/foo_bar.k4

$PRG $AMERICAN $BRITISH > $OUTDIR/american_british
$PRG $AMERICAN $BRITISH -k 1 > $OUTDIR/american_british.k1
$PRG $AMERICAN $BRITISH -k 2 > $OUTDIR/american_british.k2
$PRG $AMERICAN $BRITISH -k 4 > $OUTDIR/american_british.k4

$PRG $SAMPLE1 $SAMPLE2 > $OUTDIR/sample1_sample2
$PRG $SAMPLE1 $SAMPLE2 -k 1 > $OUTDIR/sample1_sample2.k1
$PRG $SAMPLE1 $SAMPLE2 -k 2 > $OUTDIR/sample1_sample2.k2
$PRG $SAMPLE1 $SAMPLE2 -k 4 > $OUTDIR/sample1_sample2.k4
