
Annapurna SIL is an OpenType-enabled font family that supports the Devanagari script. It includes a number of optional features that may be useful or required for particular uses or languages. These OpenType features are primarily specified using four-letter tags (e.g. 'cv04'). 

This document lists all the available features. For more information on how to access OpenType features in specific environments and applications, see [Using Font Features](https://software.sil.org/fonts/features).

This page uses web fonts (WOFF2) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use Annapurna SIL as a web font see [Annapurna SIL Webfont Example](../web/AnnapurnaSIL-webfont-example.html). For detailed information see [Using SIL Fonts on Web Pages](https://software.sil.org/fonts/webfonts).

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*


## Language-specific features

<span class='affects'>Affects: U+091D U+096B U+096E U+096F</span>

Language      | Test sequences               | OpenType/Graphite tag
:------------ | :--------------------------- |  :-------
Default       | <span class='annapurna-R normal'>झ झ् झ़ झ़् झ्र झ़्र  &nbsp;&nbsp;  ५ ८ ९</span> | `none`
Nepali        | <span class='annapurna-R normal' lang="ne">झ झ् झ़ झ़् झ्र झ़्र  &nbsp;&nbsp;  ५ ८ ९</span>  | `NEP  / ne`
Newari        | <span class='annapurna-R normal' lang="new">झ झ् झ़ झ़् झ्र झ़्र  &nbsp;&nbsp;  ५ ८ ९</span> | `NEW  / new`

## User-selected feature list

### Character variants

#### Jha alternates

<span class='affects'>Affects: U+091D</span>

Feature    | Sample                       | Feature setting
:--------- | :--------------------------- |  :-------
Standard    | <span class='annapurna-R normal'>झ झ् झ़ झ़् झ्र झ़्र</span> | `cv01=0`
Nepali style| <span class='annapurna-cv01-1-R normal'>झ झ् झ़ झ़् झ्र झ़्र</span> | `cv01=1`
Newari style| <span class='annapurna-cv01-2-R normal'>झ झ् झ़ झ़् झ्र झ़्र</span> | `cv01=2`

#### Kra alternate

<span class='affects'>Affects: U+0915 U+0930</span>

Feature    | Sample                       | Feature setting
:--------- | :--------------------------- | :-------
Standard   | <span class='annapurna-R normal'>क्र क़्र</span> | `cv03=0`
Open style | <span class='annapurna-cv03-1-R normal'>क्र क़्र</span> | `cv03=1`

#### Tra alternate 

<span class='affects'>Affects: U+0924 U+0930</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard     | <span class='annapurna-R normal'>त्र त़्र</span> | `cv04=0`
Closed style | <span class='annapurna-cv04-1-R normal'>त्र त़्र</span> | `cv04=1`

#### Shra alternate

<span class='affects'>Affects: U+0936 U+0930</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- |  :-------
Standard  | <span class='annapurna-R normal'>श्र श़्र</span> | `cv05=0`
Sha style | <span class='annapurna-cv05-1-R normal'>श्र श़्र</span> | `cv05=1`

#### Ukar nukta position

<span class='affects'>Affects: U+0941 U+0942 U+093C</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- |  :-------
Standard | <span class='annapurna-R normal'>कु़ कू़ क्कु़ क्कू़</span> | `cv06=0`
Outside  | <span class='annapurna-cv06-1-R normal'>कु़ कू़ क्कु़ क्कू़</span> | `cv06=1`

#### Ekar nukta position

<span class='affects'>Affects: U+0947 U+093C</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>के़</span> | `cv07=0`
Above bar| <span class='annapurna-cv07-1-R normal'>के़</span> | `cv07=1`

#### Digit five alternate

<span class='affects'>Affects: U+096B</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard    | <span class='annapurna-R normal'>५</span> | `cv08=0`
Nepali style| <span class='annapurna-cv08-1-R normal'>५</span> | `cv08=1`

#### Digit eight alternate

<span class='affects'>Affects: U+096E</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard     | <span class='annapurna-R normal'>८</span> | `cv09=0`
Nepali style | <span class='annapurna-cv09-1-R normal'>८</span> | `cv09=1`

#### Digit nine alternates

<span class='affects'>Affects: U+096F</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard     | <span class='annapurna-R normal'>९</span> | `cv10=0`
Nepali style | <span class='annapurna-cv10-1-R normal'>९</span> | `cv10=1`
Newari style | <span class='annapurna-cv10-2-R normal'>९</span> | `cv10=2`

#### Visarga with connecting bar

<span class='affects'>Affects: U+0903</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>&nbsp;ः</span> | `cv12=0`
With bar | <span class='annapurna-cv12-1-R normal'>&nbsp;ः</span> | `cv12=1`

#### Glottal stop - no connecting bar

<span class='affects'>Affects: U+097D</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>ॽ</span> | `cv13=0`
No bar   | <span class='annapurna-cv13-1-R normal'>ॽ</span> | `cv13=1`

#### Dya and Hya alternates

<span class='affects'>Affects: U+0926 U+0939 U+094D U+092F</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard       | <span class='annapurna-R normal'>द्य द्य्&zwj; द्य़ द्य़्&zwj; द्य्र द्य़्र &nbsp;&nbsp; ह्य ह्य्&zwj; ह्य़ ह्य़्&zwj; ह्य्र ह्य़्र</span> | `cv14=0`
Open Ya | <span class='annapurna-cv14-1-R normal'>द्य द्य्&zwj; द्य़ द्य़्&zwj; द्य्र द्य़्र &nbsp;&nbsp; ह्य ह्य्&zwj; ह्य़ ह्य़्&zwj; ह्य्र ह्य़्र</span> | `cv14=1`

#### Archaic forms

<span class='affects'>Affects: U+0905 U+0906 U+0913 U+0914 U+0923 (U+0915 U+0937)</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard      | <span class='annapurna-R normal'>अ आ ओ औ ण ण्&zwj; क्ष क्ष्&zwj;</span> | `cv15=0`
Archaic form | <span class='annapurna-cv15-1-R normal'>अ आ ओ औ ण ण्&zwj; क्ष क्ष्&zwj;</span> | `cv15=1`

#### Ra Ukar with Nukta ligatures

<span class='affects'>Affects: U+0930 U+0931 U+0941 U+093C</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>रु़ ऱु़</span> | `cv16=0`
Ligature form| <span class='annapurna-cv16-1-R normal'>रु़ ऱु़</span> | `cv16=1`

#### Cha alternate

<span class='affects'>Affects: U+091B U+094D</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>छ छ्</span> | `cv17=0`
With tail or no stem| <span class='annapurna-cv17-1-R normal'>छ छ्</span> | `cv17=1`

#### Headstroke alternates

<span class='affects'>Affects: U+A8FB</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>ꣻ</span> | `cv21=0`
Discrete | <span class='annapurna-cv21-1-R normal'>ꣻ</span> | `cv21=1`
Filler (zero width)| <span class='annapurna-cv21-2-R normal'>ꣻ</span> | `cv21=2`

#### JainOm alternate

<span class='affects'>Affects: U+A8FD</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>ꣽ</span> | `cv22=0`
Extended bar| <span class='annapurna-cv22-1-R normal'>ꣽ</span> | `cv22=1`


### Stylistic Sets

#### Jha alternates

<span class='affects'>Affects: U+091D</span>

Feature    | Sample                       | Feature setting
:--------- | :--------------------------- |  :-------
Standard    | <span class='annapurna-R normal'>झ झ् झ़ झ़् झ्र झ़्र</span> | `ss01=0`
Nepali style| <span class='annapurna-ss01-1-R normal'>झ झ् झ़ झ़् झ्र झ़्र</span> | `ss01=1`
Newari style| <span class='annapurna-ss02-1-R normal'>झ झ् झ़ झ़् झ्र झ़्र</span> | `ss02=1`

#### Kra alternate

<span class='affects'>Affects: U+0915 U+0930</span>

Feature    | Sample                       | Feature setting
:--------- | :--------------------------- | :-------
Standard   | <span class='annapurna-R normal'>क्र क़्र</span> | `ss03=0`
Open style | <span class='annapurna-ss03-1-R normal'>क्र क़्र</span> | `ss03=1`

#### Tra alternate 

<span class='affects'>Affects: U+0924 U+0930</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard     | <span class='annapurna-R normal'>त्र त़्र</span> | `ss04=0`
Closed style | <span class='annapurna-ss04-1-R normal'>त्र त़्र</span> | `ss04=1`

#### Shra alternate

<span class='affects'>Affects: U+0936 U+0930</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- |  :-------
Standard  | <span class='annapurna-R normal'>श्र श़्र</span> | `ss05=0`
Sha style | <span class='annapurna-ss05-1-R normal'>श्र श़्र</span> | `ss05=1`

#### Ukar nukta position

<span class='affects'>Affects: U+0941 U+0942 U+093C</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- |  :-------
Standard | <span class='annapurna-R normal'>कु़ कू़ क्कु़ क्कू़</span> | `ss06=0`
Outside  | <span class='annapurna-ss06-1-R normal'>कु़ कू़ क्कु़ क्कू़</span> | `ss06=1`

#### Ekar nukta position

<span class='affects'>Affects: U+0947 U+093C</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>के़</span> | `ss07=0`
Above bar| <span class='annapurna-ss07-1-R normal'>के़</span> | `ss07=1`

#### Digit five alternate

<span class='affects'>Affects: U+096B</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard    | <span class='annapurna-R normal'>५</span> | `ss08=0`
Nepali style| <span class='annapurna-ss08-1-R normal'>५</span> | `ss08=1`

#### Digit eight alternate

<span class='affects'>Affects: U+096E</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard     | <span class='annapurna-R normal'>८</span> | `ss09=0`
Nepali style | <span class='annapurna-ss09-1-R normal'>८</span> | `ss09=1`

#### Digit nine alternates

<span class='affects'>Affects: U+096F</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard     | <span class='annapurna-R normal'>९</span> | `ss10=0`
Nepali style | <span class='annapurna-ss10-1-R normal'>९</span> | `ss10=1`
Newari style | <span class='annapurna-ss11-1-R normal'>९</span> | `ss11=1`

#### Visarga with connecting bar

<span class='affects'>Affects: U+0903</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>&nbsp;ः</span> | `ss12=0`
With bar | <span class='annapurna-ss12-1-R normal'>&nbsp;ः</span> | `ss12=1`

#### Glottal stop - no connecting bar

<span class='affects'>Affects: U+097D</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>ॽ</span> | `ss13=0`
No bar   | <span class='annapurna-ss13-1-R normal'>ॽ</span> | `ss13=1`

#### Dya and Hya alternates

<span class='affects'>Affects: U+0926 U+0939 U+094D U+092F</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard       | <span class='annapurna-R normal'>द्य द्य्&zwj; द्य़ द्य़्&zwj; द्य्र द्य़्र &nbsp;&nbsp; ह्य ह्य्&zwj; ह्य़ ह्य़्&zwj; ह्य्र ह्य़्र</span> | `ss14=0`
Open Ya | <span class='annapurna-ss14-1-R normal'>द्य द्य्&zwj; द्य़ द्य़्&zwj; द्य्र द्य़्र &nbsp;&nbsp; ह्य ह्य्&zwj; ह्य़ ह्य़्&zwj; ह्य्र ह्य़्र</span> | `ss14=1`

#### Archaic forms

<span class='affects'>Affects: U+0905 U+0906 U+0913 U+0914 U+0923 (U+0915 U+0937)</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard      | <span class='annapurna-R normal'>अ आ ओ औ ण ण्&zwj; क्ष क्ष्&zwj;</span> | `ss15=0`
Archaic form | <span class='annapurna-ss15-1-R normal'>अ आ ओ औ ण ण्&zwj; क्ष क्ष्&zwj;</span> | `ss15=1`

#### Ra Ukar with Nukta ligatures

<span class='affects'>Affects: U+0930 U+0931 U+0941 U+093C</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>रु़ ऱु़</span> | `ss16=0`
Ligature form| <span class='annapurna-ss16-1-R normal'>रु़ ऱु़</span> | `ss16=1`

#### Cha alternate

<span class='affects'>Affects: U+091B U+094D</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>छ छ्</span> | `ss17=0`
With tail or no stem| <span class='annapurna-ss17-1-R normal'>छ छ्</span> | `ss17=1`




[font id='annapurna' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%']
[font id='annapurna-cv01-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv01 1']
[font id='annapurna-cv01-2' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv01 2']
[font id='annapurna-cv03-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv03 1']
[font id='annapurna-cv04-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv04 1']
[font id='annapurna-cv05-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv05 1']
[font id='annapurna-cv06-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv06 1']
[font id='annapurna-cv07-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv07 1']
[font id='annapurna-cv08-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv08 1']
[font id='annapurna-cv09-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv09 1']
[font id='annapurna-cv10-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv10 1']
[font id='annapurna-cv10-2' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv10 2']
[font id='annapurna-cv12-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv12 1']
[font id='annapurna-cv13-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv13 1']
[font id='annapurna-cv14-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv14 1']
[font id='annapurna-cv15-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv15 1']
[font id='annapurna-cv16-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv16 1']
[font id='annapurna-cv17-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv17 1']
[font id='annapurna-cv21-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv21 1']
[font id='annapurna-cv21-2' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv21 2']
[font id='annapurna-cv22-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='cv22 1']
[font id='annapurna-ss01-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss01 1']
[font id='annapurna-ss02-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss02 1']
[font id='annapurna-ss03-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss03 1']
[font id='annapurna-ss04-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss04 1']
[font id='annapurna-ss05-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss05 1']
[font id='annapurna-ss06-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss06 1']
[font id='annapurna-ss07-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss07 1']
[font id='annapurna-ss08-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss08 1']
[font id='annapurna-ss09-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss09 1']
[font id='annapurna-ss10-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss10 1']
[font id='annapurna-ss11-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss11 1']
[font id='annapurna-ss12-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss12 1']
[font id='annapurna-ss13-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss13 1']
[font id='annapurna-ss14-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss14 1']
[font id='annapurna-ss15-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss15 1']
[font id='annapurna-ss16-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss16 1']
[font id='annapurna-ss17-1' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%' feats='ss17 1']
