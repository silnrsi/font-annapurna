#!/usr/bin/python
# encoding: utf-8
# this is a smith configuration file
# please adjust this template to your needs

# set the default output folders
out = "results"
DOCDIR = ["documentation", "web"]
OUTDIR = "installers"
ZIPDIR = "releases"
TESTDIR = "tests"
TESTRESULTSDIR = 'tests'
STANDARDS = 'tests/reference'

# set the version control system
VCS = 'git'

# set the font name, version, licensing and description
APPNAME = 'AnnapurnaSIL'
VERSION = '1.202'
TTF_VERSION = '1.202'
#BUILDLABEL = "alpha1"
COPYRIGHT = 'Copyright (c) 2017 SIL International(http://www.sil.org) with Reserved Font Names Annapurna and SIL"'
LICENSE = "OFL.txt"

DESC_SHORT = 'Devanagari Unicode TrueType font with OT and Graphite support'

# packaging
DESC_NAME = 'Annapurna SIL'
DEBPKG = 'fonts-sil-annapurna'


# set the build and test parameters
for ext in ('-Regular', '-Bold') :
	fbase = 'AnnapurnaSIL' + ext
	font (target = process('AnnapurnaSIL' + ext + '.ttf', name('Annapurna SIL'),
                   cmd('${TTFAUTOHINT} -n -W ${DEP} ${TGT}')),
		source = 'source/AnnapurnaSIL' + ext + '_source.ttf',
		version = TTF_VERSION,
		copyright = COPYRIGHT,
		script = ['deva', 'dev2'],
		opentype = volt ('source/VOLT_AnnapurnaSIL' + ext + '.vtp', no_make = (1)),
		graphite = gdl ('AnnapurnaSIL' + ext + '.gdl',
			master = 'source/annapurna_rules.gdh'),
		ap = 'source/AnnapurnaSIL' + ext + '_anchors.xml',
		pdf = fret(),
		woff = woff('web/AnnapurnaSIL' + ext + '.woff', params = '-v ' + VERSION + ' -m ../source/AnnapurnaSIL-WOFF-metadata.xml'),
	)

def configure(ctx) :
    ctx.find_program('ttfautohint')
