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


# set the build and test parameters
for ext in ('-Regular', '-Bold') :
    fbase = 'AnnapurnaSIL' + ext
    font (target = process('AnnapurnaSIL' + ext + '.ttf', name('Annapurna SIL'),
            cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['source/AnnapurnaSIL' + ext + '.ufo']),
            cmd('${TTFAUTOHINT} -n -W ${DEP} ${TGT}')),
        source = create('buildsrc/AnnapurnaSIL' + ext + '_src.ttf', cmd('psfufo2ttf ${SRC} ${TGT}', ['source/AnnapurnaSIL' + ext + '.ufo'])),
        ap = create('buildsrc/ap/Annapurna' + ext + '.xml', cmd('psfexportanchors -g ${SRC} ${TGT}', [ 'source/AnnapurnaSIL' + ext + '.ufo' ])),
#        version = TTF_VERSION,
#        copyright = COPYRIGHT,
        opentype = fea ('buildsrc/fea/Annapurna' + ext + '_make.fea',
            master = 'source/annapurna_ot.feax'),
##            make_params="-z 8"),
##        graphite = gdl ('buildsrc/gdl/AnnapurnaSIL' + ext + '.gdl',
##            master = 'source/annapurna_gr_rules.gdh',
##            make_params = ' --package "../tools/perllib/gdl_deva.pm"'),
        script = ['deva', 'dev2'],
        pdf = fret(),
        woff = woff('web/AnnapurnaSIL' + ext + '.woff', params = '-v ' + VERSION + ' -m ../source/AnnapurnaSIL-WOFF-metadata.xml'),
	)

def configure(ctx) :
    ctx.find_program('ttfautohint')
