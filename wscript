#!/usr/bin/python3
# this is a smith configuration file for the Annapurna font project

# override the default folders
DOCDIR = ['documentation', 'web']  # add 'web' to default
# STANDARDS = 'references/dev_build'
STANDARDS = 'references/v2000'

# set package name
APPNAME = 'AnnapurnaSIL'

# set the font family name
FAMILY = APPNAME

DESC_SHORT = 'Devanagari Unicode TrueType font with OT and Graphite support'

# Get version info from Regular UFO; must be first function call:
getufoinfo('source/' + FAMILY + '-Regular' + '.ufo')
# BUILDLABEL = 'beta'

# APs to ignore when generating OT and GDL classes
# omitAPs = '--omitaps "UpperCenter"'

# Commands to process with target font
cmds = []
cmds.append(cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['source/${DS:FILENAME_BASE}.ufo']))
cmds.append(cmd('${TTFAUTOHINT} -n -W ${DEP} ${TGT}'))
cmds.append(cmd('${TYPETUNER} -o ${TGT} add ${SRC} ${DEP}', "source/typetuner/feat_all.xml"))

# set the build and test parameters
d = designspace('source/AnnapurnaSIL-RB.designspace',
        target = process('${DS:FILENAME_BASE}.ttf', *cmds),
        # instanceparams = "-W",
        ap = 'source/ap/${DS:FILENAME_BASE}.xml',
        # classes = 'source/annapurna_classes.xml',

        opentype = fea('source/fea/${DS:FILENAME_BASE}.fea',
            master = 'source/annapurna_ot.feax',
            mapfile = 'source/typetuner/${DS:FILENAME_BASE}.map', 
            # make_params = omitAPs
        ),

        graphite = gdl('source/gdl/${DS:FILENAME_BASE}.gdl',
            master = 'source/annapurna_gr_rules.gdh',
            params = '-q -d -v5 -e gdlerr-${DS:FILENAME_BASE}.txt', 
            depends = ['source/annapurna_gr_features.gdh']
        ),

        typetuner = typetuner('source/typetuner/feat_all.xml'),

        woff = woff('web/${DS:FILENAME_BASE}.woff', 
            params = '-v ' + VERSION + ' -m ../source/AnnapurnaSIL-WOFF-metadata.xml'
        ),

        script = ['dev2'],
        pdf = fret(params="-r -oi"),
    )

# Make Nepal TypeTuned package
npackage = package(appname="AnnapurnaSILNepal", 
                   version = VERSION, 
                   package_files = {
                                    '*.txt': 'Nepal/', 
                                    'source/typetuner/README_Nepal.txt': 'Nepal/', 
                                    'source/typetuner/feat_set_Nepal.xml': 'Nepal/', 
                                    'documentation/': 'Nepal/documentation/', 
                                    'web/*.*': 'Nepal/web/'
                                   })
for f in d.fonts:
    font(target = process('Nepal/'+f.target.replace('AnnapurnaSIL', 'AnnapurnaSILNepal'),
                        cmd('${TYPETUNER} -o ${TGT} applyset ${SRC} ${DEP}', ['source/typetuner/feat_set_Nepal.xml']), 
                        name('Annapurna SIL Nepal')),
            opentype = internal(),
            source = f.target,
            package = npackage)

def configure(ctx) :
    ctx.find_program('ttfautohint')
    ctx.find_program('typetuner')
