#!/bin/bash

config=$PWD/tools/archive/latin
pushd source
psfgetglyphnames -a ~/script/zind/fonts/aglfn-nr.csv -i $config/chars.txt ~/script/latn/fonts/charis/source/CharisSIL-Regular.ufo glyphs_import.csv

for ufo in *.ufo
do
    # style
    basename=$(basename $ufo .ufo)
    style=$(echo $basename | cut -d\- -f 2)

    # save needed anchors
    ~/script/tools/anchor-keep.py mark $ufo

    # import characters
    psfcopyglyphs --rename rename --unicode usv --force -s ~/script/latn/fonts/charis/source/CharisSIL-${style}.ufo -i glyphs_import.csv -l ${style}_import.log $ufo
    psfbuildcomp -i $config/composites.txt $ufo

    # restore original anchors
    ~/script/tools/anchor-keep.py only $ufo

    # scale characters
    awk 'FS=","{printf "%s,%s,%s\n", $2, $2, $3}' glyphs_import.csv | tail -n +2 > glyphs_scale.csv
    psfmakescaledshifted -i glyphs_scale.csv -t latin -l ${style}_scale.log $ufo

    # cleanup
    psfdeleteglyphs -i $config/delete.txt $ufo
    git add $ufo/glyphs/* $ufo/lib.plist
done
popd
