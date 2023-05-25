---
title: Annapurna SIL - Font Features
fontversion: 2.000
---

Annapurna SIL is an OpenType-enabled font family that supports the Devanagari script. It includes a number of optional features that may be useful or required for particular uses or languages. These OpenType features are primarily specified using four-letter tags (e.g. 'cv04'). 

This document lists all the available features. For more information on how to access OpenType features in specific environments and applications, see [Using Font Features](https://software.sil.org/fonts/features).

This page uses web fonts (WOFF2) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use Annapurna SIL as a web font see [Annapurna SIL Webfont Example](../web/AnnapurnaSIL-webfont-example.html). For detailed information see [Using SIL Fonts on Web Pages](https://software.sil.org/fonts/webfonts).

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*


## User-selected feature list

### Character variants

#### Jha alternates

<span class='affects'>Affects: U+091D</span>

Feature    | Sample                       | Feature setting
:--------- | :--------------------------- |  :-------
Standard    | <span class='annapurna-R normal'>झ झ् झ़ झ़् झ्र झ़्र</span> | `cv01=0`
Nepali style| <span class='annapurna-R normal' style='font-feature-settings: "cv01" 1'>झ झ् झ़ झ़् झ्र झ़्र</span> | `cv01=1`
Newari style| <span class='annapurna-R normal' style='font-feature-settings: "cv01" 2'>झ झ् झ़ झ़् झ्र झ़्र</span> | `cv01=2`

#### Kra alternate

<span class='affects'>Affects: U+0915 U+0930</span>

Feature    | Sample                       | Feature setting
:--------- | :--------------------------- | :-------
Standard   | <span class='annapurna-R normal'>क्र क़्र</span> | `cv03=0`
Open style | <span class='annapurna-R normal' style='font-feature-settings: "cv03" 1'>क्र क़्र</span> | `cv03=1`

#### Tra alternate 

<span class='affects'>Affects: U+0924 U+0930</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard     | <span class='annapurna-R normal'>त्र त़्र</span> | `cv04=0`
Closed style | <span class='annapurna-R normal' style='font-feature-settings: "cv04" 1'>त्र त़्र</span> | `cv04=1`

#### Shra alternate

<span class='affects'>Affects: U+0936 U+0930</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- |  :-------
Standard  | <span class='annapurna-R normal'>श्र श़्र</span> | `cv05=0`
Sha style | <span class='annapurna-R normal' style='font-feature-settings: "cv05" 1'>श्र श़्र</span> | `cv05=1`

#### Ukar nukta position

<span class='affects'>Affects: U+0941 U+0942 U+093C</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- |  :-------
Standard | <span class='annapurna-R normal'>कु़ कू़ क्कु़ क्कू़</span> | `cv06=0`
Outside  | <span class='annapurna-R normal' style='font-feature-settings: "cv06" 1'>कु़ कू़ क्कु़ क्कू़</span> | `cv06=1`

#### Ekar nukta position

<span class='affects'>Affects: U+0947 U+093C</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>के़</span> | `cv07=0`
Above bar| <span class='annapurna-R normal' style='font-feature-settings: "cv07" 1'>के़</span> | `cv07=1`

#### Digit five alternate

<span class='affects'>Affects: U+096B</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard    | <span class='annapurna-R normal'>५</span> | `cv08=0`
Nepali style| <span class='annapurna-R normal' style='font-feature-settings: "cv08" 1'>५</span> | `cv08=1`

#### Digit eight alternate

<span class='affects'>Affects: U+096E</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard     | <span class='annapurna-R normal'>८</span> | `cv09=0`
Nepali style | <span class='annapurna-R normal' style='font-feature-settings: "cv09" 1'>८</span> | `cv09=1`

#### Digit nine alternates

<span class='affects'>Affects: U+096F</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard     | <span class='annapurna-R normal'>९</span> | `cv10=0`
Nepali style | <span class='annapurna-R normal' style='font-feature-settings: "cv10" 1'>९</span> | `cv10=1`
Newari style | <span class='annapurna-R normal' style='font-feature-settings: "cv10" 2'>९</span> | `cv10=2`

#### Visarga with connecting bar

<span class='affects'>Affects: U+0903</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>&nbsp;ः</span> | `cv12=0`
With bar | <span class='annapurna-R normal' style='font-feature-settings: "cv11" 1'>&nbsp;ः</span> | `cv12=1`

#### Glottal stop - no connecting bar

<span class='affects'>Affects: U+097D</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>ॽ</span> | `cv13=0`
No bar   | <span class='annapurna-R normal' style='font-feature-settings: "cv13" 1'>ॽ</span> | `cv13=1`

#### Dya and Hya alternates

<span class='affects'>Affects: U+0926 U+0939 U+094D U+092F</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard       | <span class='annapurna-R normal'>द्य द्य्&zwj; द्य़ द्य़्&zwj; द्य्र द्य़्र &nbsp;&nbsp; ह्य ह्य्&zwj; ह्य़ ह्य़्&zwj; ह्य्र ह्य़्र</span> | `cv14=0`
Open Ya | <span class='annapurna-R normal' style='font-feature-settings: "cv14" 1'>द्य द्य्&zwj; द्य़ द्य़्&zwj; द्य्र द्य़्र &nbsp;&nbsp; ह्य ह्य्&zwj; ह्य़ ह्य़्&zwj; ह्य्र ह्य़्र</span> | `cv14=1`

#### Archaic forms

<span class='affects'>Affects: U+0905 U+0906 U+0913 U+0914 U+0923 (U+0915 U+0937)</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard      | <span class='annapurna-R normal'>अ आ ओ औ ण ण्&zwj; क्ष क्ष्&zwj;</span> | `cv15=0`
Archaic forms | <span class='annapurna-R normal' style='font-feature-settings: "cv15" 1'>अ आ ओ औ ण ण्&zwj; क्ष क्ष्&zwj;</span> | `cv15=1`

#### Ra Ukar with Nukta ligatures

<span class='affects'>Affects: U+0930 U+0931 U+0941 U+093C</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>रु़ ऱु़</span> | `cv16=0`
Ligature form| <span class='annapurna-R normal' style='font-feature-settings: "cv16" 1'>रु़ ऱु़</span> | `cv16=1`

#### Cha alternate

<span class='affects'>Affects: U+091B U+094D</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>छ छ्</span> | `cv17=0`
With tail or no stem| <span class='annapurna-R normal' style='font-feature-settings: "cv17" 1'>छ छ्</span> | `cv17=1`

#### Headstroke alternates

<span class='affects'>Affects: U+A8FB</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>ꣻ</span> | `cv21=0`
Discrete | <span class='annapurna-R normal' style='font-feature-settings: "cv21" 1'>ꣻ</span> | `cv21=1`
Filler   | <span class='annapurna-R normal' style='font-feature-settings: "cv21" 2'>ꣻ</span> | `cv21=2`

#### JainOm alternate

<span class='affects'>Affects: U+A8FD</span>

Feature  | Sample                       | Feature setting
:------- | :--------------------------- | :-------
Standard | <span class='annapurna-R normal'>ꣽ</span> | `cv22=0`
Extended bar| <span class='annapurna-R normal' style='font-feature-settings: "cv22" 1'>ꣽ</span> | `cv22=1`





<!-- PRODUCT SITE ONLY
[font id='annapurna' face='AnnapurnaSIL-Regular' bold='AnnapurnaSIL-Bold' size='150%']
-->
