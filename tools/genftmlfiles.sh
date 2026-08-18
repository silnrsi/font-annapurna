#!/bin/bash

# This script rebuilds the algorithmically-generated ftml files. See README.md

# Copyright (c) 2020-2026 SIL Global  (https://www.sil.org)
# Released under the MIT License (https://opensource.org/licenses/

# Assumes we're in the root folder, i.e., font-idiqlat

set -e

if [ ! -e OFL.txt ] 
then
	echo "Please cd to root of font project to use this script"
	exit 2
fi

prevfont="references/v3000/AnnapurnaSIL-Regular.ttf"
prevver="3.000"

commonParams=( \
	--prevfont "$prevfont"  \
	-s "url(../$prevfont)"  \
#	-s "url(../$prevfont)|$prevver"  \
	--ap '_?dia[ABO]$'  \
	--xsl ../tools/ftml.xsl  \
	--scale 250  \
	-i source/glyph_data.csv  \
	-w 75%  \
#	-s "url(../references/v3000/AnnapurnaSIL-Regular.ttf)"  \
)

echo "Rebuilding ftml files..."
tools/psfgenftml.py -q -t 'AllChars (auto)'                      source/AnnapurnaSIL-Regular.ufo  tests/AllChars-auto.ftml        -l tests/logs/AllChars.log         "${commonParams[@]}" -s 'url(../results/AnnapurnaSIL-Regular.ttf)' -s 'url(../results/AnnapurnaSIL-Medium.ttf)' -s 'url(../results/AnnapurnaSIL-SemiBold.ttf)' -s 'url(../results/AnnapurnaSIL-Bold.ttf)' &
tools/psfgenftml.py -q -t 'Diac Short (auto)'                    source/AnnapurnaSIL-Regular.ufo  tests/Diac-short-auto.ftml      -l tests/logs/DiacTest1-short.log  "${commonParams[@]}" -s 'url(../results/AnnapurnaSIL-Regular.ttf)' -s 'url(../results/AnnapurnaSIL-Medium.ttf)' -s 'url(../results/AnnapurnaSIL-SemiBold.ttf)' -s 'url(../results/AnnapurnaSIL-Bold.ttf)' &
tools/psfgenftml.py -q -t 'Diac (auto)'                          source/AnnapurnaSIL-Regular.ufo  tests/Diac-auto.ftml            -l tests/logs/DiacTest1.log        "${commonParams[@]}" -s 'url(../results/AnnapurnaSIL-Regular.ttf)' -s 'url(../results/AnnapurnaSIL-Medium.ttf)' -s 'url(../results/AnnapurnaSIL-SemiBold.ttf)' -s 'url(../results/AnnapurnaSIL-Bold.ttf)' &

wait
echo done.
