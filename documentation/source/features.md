---
title: Annapurna SIL - Font Features
fontversion: 3.000
---

Annapurna SIL is an OpenType-enabled font family that supports the Devanagari script. It includes a number of optional user-selected features that may be useful or required for particular uses or languages. These OpenType features are primarily specified using four-letter tags (e.g. 'cv04' or 'ss04') to display variant characters or specific behavior. Certain apps, such as web browsers, can also use language tags to display all the language-specific variants and behaviors.

This document lists all the language and user-selected features in Annapurna SIL. For more information on how to access these features in specific environments and applications, see [Using Font Features](https://software.sil.org/fonts/features). This is the preferred way of using features; however, Annapurna SIL is also available through the [TypeTuner Web](https://scripts.sil.org/ttw/fonts2go.cgi) service, which allows you to choose among the user-selected font features (shown below) and download a font with those features preset. This enables them to work in many applications that do not make use of OpenType Stylistic Sets.

This page uses web fonts (WOFF2) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use Annapurna SIL as a web font see [Annapurna SIL Webfont Example](../web/AnnapurnaSIL-webfont-example.html). For detailed information see [Using SIL Fonts on Web Pages](https://software.sil.org/fonts/webfonts).

*If this document is not displaying correctly, a PDF version is also provided in the documentation/pdf folder of the release package.*


## Language-specific features

<span class='affects'>Affects: U+091D U+096B U+096E U+096F</span>

Language      | Test sequences               | OpenType lang tag
:------------ | :--------------------------- |  :-------
Default       | <span class='annapurna-R normal'>झ झ् झ़ झ़् झ्र झ़्र  &nbsp;&nbsp;  ५ ८ ९</span> | `none`
Nepali        | <span class='annapurna-R normal' lang="ne">झ झ् झ़ झ़् झ्र झ़्र  &nbsp;&nbsp;  ५ ८ ९</span>  | `NEP or ne`
Newari        | <span class='annapurna-R normal' lang="new">झ झ् झ़ झ़् झ्र झ़्र  &nbsp;&nbsp;  ५ ८ ९</span> | `NEW or new`

## User-selected feature list

### Stylistic Sets and Character Variants

#### Jha alternates

<span class='affects'>Affects: U+091D</span>

Feature    | Sample                       | Feature setting
:--------- | :--------------------------- |  :-------
Standard    | <span class='annapurna-R normal'>झ झ् झ़ झ़् झ्र झ़्र</span> | `ss01=0`
Nepali style| <span class='annapurna-R normal' style='font-feature-settings: "cv01" 1, "ss01" 1'>झ झ् झ़ झ़् झ्र झ़्र</span> | `ss01=1`
Newari style| <span class='annapurna-R normal' style='font-feature-settings: "cv01" 2, "ss02" 1'>झ झ् झ़ झ़् झ्र झ़्र</span> | `ss02=1`

#### Kra alternate

<span class='affects'>Affects: U+0915 U+0930</span>

Feature    | Sample                       | Feature setting
:--------- | :--------------------------- | :-------
Standard   | <span class='annapurna-R normal'>क्र क़्र</span> | `ss03=0`
Open style | <span class='annapurna-R normal' style='font-feature-settings: "cv03" 1, "ss03" 1'>क्र क़्र</span> | `ss03=1`

#### Tra alternate 

<span class='affects'>Affects: U+0924 U+0930</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard     | <span class='annapurna-R normal'>त्र त़्र</span> | `ss04=0`
Closed style | <span class='annapurna-R normal' style='font-feature-settings: "cv04" 1, "ss04" 1'>त्र त़्र</span> | `ss04=1`

#### Shra alternate

<span class='affects'>Affects: U+0936 U+0930</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- |  :-------
Standard  | <span class='annapurna-R normal'>श्र श़्र</span> | `ss05=0`
Sha style | <span class='annapurna-R normal' style='font-feature-settings: "cv05" 1, "ss05" 1'>श्र श़्र</span> | `ss05=1`

#### Ukar nukta position

<span class='affects'>Affects: U+0941 U+0942 U+093C</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- |  :-------
Standard | <span class='annapurna-R normal'>कु़ कू़ क्कु़ क्कू़</span> | `ss06=0`
Outside  | <span class='annapurna-R normal' style='font-feature-settings: "cv06" 1, "ss06" 1'>कु़ कू़ क्कु़ क्कू़</span> | `ss06=1`

#### Ekar nukta position

<span class='affects'>Affects: U+0947 U+093C</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>के़</span> | `ss07=0`
Above bar| <span class='annapurna-R normal' style='font-feature-settings: "cv07" 1, "ss07" 1'>के़</span> | `ss07=1`

#### Digit five alternate

<span class='affects'>Affects: U+096B</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard    | <span class='annapurna-R normal'>५</span> | `ss08=0`
Nepali style| <span class='annapurna-R normal' style='font-feature-settings: "cv08" 1, "ss08" 1'>५</span> | `ss08=1`

#### Digit eight alternate

<span class='affects'>Affects: U+096E</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard     | <span class='annapurna-R normal'>८</span> | `ss09=0`
Nepali style | <span class='annapurna-R normal' style='font-feature-settings: "cv09" 1, "ss09" 1'>८</span> | `ss09=1`

#### Digit nine alternates

<span class='affects'>Affects: U+096F</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard     | <span class='annapurna-R normal'>९</span> | `ss10=0`
Nepali style | <span class='annapurna-R normal' style='font-feature-settings: "cv10" 1, "ss10" 1'>९</span> | `ss10=1`
Newari style | <span class='annapurna-R normal' style='font-feature-settings: "cv10" 2, "ss11" 1'>९</span> | `ss11=1`

#### Visarga with connecting bar

<span class='affects'>Affects: U+0903</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>&nbsp;ः</span> | `ss12=0`
With bar | <span class='annapurna-R normal' style='font-feature-settings: "cv12" 1, "ss12" 1'>&nbsp;ः</span> | `ss12=1`

#### Glottal stop - no connecting bar

<span class='affects'>Affects: U+097D</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>ॽ</span> | `ss13=0`
No bar   | <span class='annapurna-R normal' style='font-feature-settings: "cv13" 1, "ss13" 1'>ॽ</span> | `ss13=1`

#### Dya and Hya alternates

<span class='affects'>Affects: U+0926 U+0939 U+094D U+092F</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard       | <span class='annapurna-R normal'>द्य द्य्&zwj; द्य़ द्य़्&zwj; द्य्र द्य़्र &nbsp;&nbsp; ह्य ह्य्&zwj; ह्य़ ह्य़्&zwj; ह्य्र ह्य़्र</span> | `ss14=0`
Open Ya | <span class='annapurna-R normal' style='font-feature-settings: "cv14" 1, "ss14" 1'>द्य द्य्&zwj; द्य़ द्य़्&zwj; द्य्र द्य़्र &nbsp;&nbsp; ह्य ह्य्&zwj; ह्य़ ह्य़्&zwj; ह्य्र ह्य़्र</span> | `ss14=1`

#### Archaic forms

<span class='affects'>Affects: U+0905 U+0906 U+0913 U+0914 U+0923 (U+0915 U+0937)</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard      | <span class='annapurna-R normal'>अ आ ओ औ ण ण्&zwj; क्ष क्ष्&zwj;</span> | `ss15=0`
Archaic form | <span class='annapurna-R normal' style='font-feature-settings: "cv15" 1, "ss15" 1'>अ आ ओ औ ण ण्&zwj; क्ष क्ष्&zwj;</span> | `ss15=1`

#### Ra Ukar with Nukta ligatures

<span class='affects'>Affects: U+0930 U+0931 U+0941 U+093C</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>रु़ ऱु़ &nbsp;&nbsp; रू़ ऱू़</span> | `ss16=0`
Ligature form| <span class='annapurna-R normal' style='font-feature-settings: "cv16" 1, "ss16" 1'>रु़ ऱु़ &nbsp;&nbsp; रू़ ऱू़</span> | `ss16=1`

#### Cha alternate

<span class='affects'>Affects: U+091B U+094D</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>छ छ् छ्क</span> | `ss17=0`
With tail or no stem| <span class='annapurna-R normal' style='font-feature-settings: "cv17" 1, "ss17" 1'>छ छ् छ्क</span> | `ss17=1`

#### Sha alternate

<span class='affects'>Affects: U+0936</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>श शृं</span> | `ss18=0`
As a loop| <span class='annapurna-R normal' style='font-feature-settings: "cv18" 1, "ss18" 1'>श शृं</span> | `ss18=1`

#### Headstroke alternates

<span class='affects'>Affects: U+A8FB</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>ꣻ &nbsp;&nbsp;  कꣻम</span> | `cv21=0`
Discrete | <span class='annapurna-R normal' style='font-feature-settings: "cv21" 1'>ꣻ &nbsp;&nbsp;  कꣻम</span> | `cv21=1`
Narrow   | <span class='annapurna-R normal' style='font-feature-settings: "cv21" 2'>ꣻ  &nbsp;&nbsp;&nbsp;&nbsp;  कꣻम </span> | `cv21=2`
Filler  (zero advance width)| <span class='annapurna-R normal' style='font-feature-settings: "cv21" 3'>ꣻ  &nbsp;&nbsp;&nbsp;&nbsp;  कꣻम </span> | `cv21=3`

#### JainOm alternate

<span class='affects'>Affects: U+A8FD</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>ꣽ</span> | `cv22=0`
Extended headstroke | <span class='annapurna-R normal' style='font-feature-settings: "cv22" 1'>ꣽ</span> | `cv22=1`

## Default behavior

Many font features in Annapurna SIL, common to both OpenType and Graphite rendering engines, work behind the scenes to display the proper shaping of Devanagari characters, such as half forms and conjuncts, and to correctly position diacritics or marks. Other features (listed below) are used to create a more pleasing look. These features are always “on”.

### Stacking conjunct compression

If there is a matra below a stacking conjunct, this feature compresses the conjunct which raises the matra above the descender height line. Otherwise, they could clash with matras or signs above the bar on the following line. <em>In the test sequence below, note the first conjunct (without a matra) is normal height.</em>

<span class='affects'>Affects: U+0915 U+0916 U+0917 U+0918 U+0919 U+091A U+091F U+0920 U+0921 U+092E U+0932 U+0939 </span>

Feature          | Sample              | Feature setting
:--------------- | :-------------------| :--------------
Conjunct compression | <span class='annapurna-R normal'>क्क क्कु क्कू क्कु़ क्कू़</span> | Contextual Alternate 'calt' 

### Fractions

Note: The Ligature feature is included in the font since some OpenType applications use it instead of the Fractions feature setting.

<span class='affects'>Affects: U+0967 U+0968 U+0969 U+096A U+2044 </span>

Feature          | Sample              | Feature setting
:--------------- | :-------------------| :--------------
No ligature (using ZWNJ) | <span class='annapurna-R normal'>१⁄‌२ १⁄‌४ ३⁄‌४</span> | None 
Fractions        | <span class='annapurna-R normal'>१⁄२ १⁄४ ३⁄४</span> | Fractions 'frac' or Ligature 'liga'

### Latin punctuation

The Latin characters in Annapurna SIL are derived from the Charis SIL font. However, the exclamation and question marks were redrawn to fit the style of the Annapurna Devanagari glyphs and are used by default. But they will switch to the Charis style punctuation when preceded by a Latin character. This is accomplished by use of the Contextual Alternates OpenType feature.

<span class='affects'>Affects: U+0021 U+003F </span>

Feature          | Sample              | Feature setting
:--------------- | :-------------------| :--------------
Devanagari style | <span class='annapurna-R normal'>test क्र! test क्र?</span> | Default 
Latin style      | <span class='annapurna-R normal'>test kra! test kra?</span> | Contextual Alternate 'calt'
Mixed styles     | <span class='annapurna-R normal'>नमस्ते! Namaste!</span> | Contextual Alternate 'calt'


<!-- PRODUCT SITE ONLY
[font id='annapurna' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%']
-->
