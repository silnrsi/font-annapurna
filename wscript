#!/usr/bin/python3
# this is a smith configuration file for the Annapurna font project

# override the default folders
DOCDIR = ['documentation', 'web']  # add 'web' to default
STANDARDS = 'tests/reference'

# set package name
APPNAME = 'AnnapurnaSIL'

# set the font family name
FAMILY = APPNAME

DESC_SHORT = 'Devanagari Unicode TrueType font with OT and Graphite support'

# Get version info from Regular UFO; must be first function call:
getufoinfo('source/' + FAMILY + '-Regular' + '.ufo')
# BUILDLABEL = 'beta'

# Commands to process with target font
cmds = []
cmds.append(cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['source/${DS:FILENAME_BASE}.ufo']))
cmds.append(cmd('${TTFAUTOHINT} -n -W ${DEP} ${TGT}'))

# set the build and test parameters
d = designspace('source/AnnapurnaSIL-RB.designspace',
        target = process('${DS:FILENAME_BASE}.ttf', *cmds),
        instanceparams = "-W",
        ap = 'source/ap/${DS:FILENAME_BASE}.xml',

        opentype = fea('source/fea/${DS:FILENAME_BASE}.fea',
            master = 'source/annapurna_ot.feax'
        ),

#        graphite = gdl('source/gdl/${DS:FILENAME_BASE}.gdl',
#            master = 'source/annapurna_gr_rules.gdl',
#            params = '-w3521 -w3530 -q -d -D -v5 -e gdlerr-' + '${DS:FILENAME_BASE}' + '.txt', make_params="-m _R",
#           depends = ['source/annapurna_gr_features.gdl']
#        ),


##for ext in ('-Regular', '-Bold') :
##    fbase = 'AnnapurnaSIL' + ext
##    font (target = process('AnnapurnaSIL' + ext + '.ttf', name('Annapurna SIL'),
#            cmd('../tools/FFchangeGlyphNames.py -i ' + psnames + ' ${DEP} ${TGT}'),
##            cmd('${TTFAUTOHINT} -n -W ${DEP} ${TGT}')),
##        source = create('buildsrc/AnnapurnaSIL' + ext + '_src.ttf', cmd('psfufo2ttf ${SRC} ${TGT}', ['source/AnnapurnaSIL' + ext + '.ufo'])),
##        ap = create('buildsrc/ap/Annapurna' + ext + '.xml', cmd('psfexportanchors -g ${SRC} ${TGT}', [ 'source/AnnapurnaSIL' + ext + '.ufo' ])),
#        version = TTF_VERSION,
#        copyright = COPYRIGHT,
##        opentype = fea ('buildsrc/fea/Annapurna' + ext + '_make.fea',
##            master = 'source/annapurna_ot.feax'),
##            make_params="-z 8"),
##        graphite = gdl ('buildsrc/gdl/AnnapurnaSIL' + ext + '.gdl',
##            master = 'source/annapurna_gr_rules.gdh',
##            make_params = ' --package "../tools/perllib/gdl_deva.pm"'),
        script = ['deva', 'dev2'],
        pdf = fret(params="-r -oi"),
        woff = woff('web/${DS:FILENAME_BASE}.woff', params = '-v ' + VERSION + ' -m ../source/AnnapurnaSIL-WOFF-metadata.xml'),
	)

def configure(ctx) :
    ctx.find_program('ttfautohint')
