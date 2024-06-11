### 11 June 2024 (SIL WSTech team)  Annapurna SIL version 2.100
- Enabled rendering for a unique sequence (an implosive) in the Wambule language
  - Consists of a DDA, BA or LA half-form (using ZWJ) plus a full vowel A
  - The sequence may include a vowel sign or virama (halant)
  - Inspect the GSUB OpenType code for details since this is not usual behaviour
- Added TypeTuner support for Ra+Ukar+Nukta ligature (feature in Stylistic Set 16)
- Fixed CHA variant bug (feature in Stylistic Set 17)
- Fixed ikar + vowel reordering bug (Graphite only)

### 08 November 2023 (SIL WSTech team)  Annapurna SIL version 2.000
***Note that this is a major upgrade that may cause document reflow as
some glyphs widths have changed and linespacing has been adjusted.***

- First release that uses a UFO-based design and production workflow
  - All sources are in open formats
  - Build toolkit and workflow is completely open-source
  - See https://silnrsi.github.io/silfontdev/en-US/Introduction.html
- Web fonts are provided in both WOFF and WOFF2 formats
- Added Devanagari characters
  - U+A8FC DEVANAGARI SIGN SIDDHAM
  - U+A8FD DEVANAGARI JAIN OM
  - U+A8FE DEVANAGARI LETTER AY
  - U+A8FF DEVANAGARI VOWEL SIGN AY
- Added recommended characters (Latin, punctuation, other) for non-Latin fonts
  - U+02C7 caron
  - U+02D8 breve
  - U+02D9 dotaccent
  - U+02DA ring
  - U+02DB ogonek
  - U+02DD hungarumlaut
  - U+0306 brevecomb
  - U+034F graphemejoinercomb
  - U+03C0 pi
  - U+2000 enquad
  - U+2001 emquad
  - U+2002 enspace
  - U+2003 emspace
  - U+2004 threeperemspace
  - U+2005 fourperemspace
  - U+2006 sixperemspace
  - U+2007 figurespace
  - U+2008 punctuationspace
  - U+200A hairspace
  - U+2010 hyphentwo
  - U+2011 nonbreakinghyphen
  - U+2012 figuredash
  - U+2015 horizontalbar
  - U+2027 hyphenationpoint
  - U+2028 lineseparator
  - U+2029 paragraphseparator
  - U+2060 wordjoiner
  - U+2126 Omega, Ohm
  - U+2202 partialdiff
  - U+2206 Delta
  - U+220F product
  - U+2211 summation
  - U+2215 divisionslash
  - U+2219 bulletoperator
  - U+221A radical
  - U+221E infinity
  - U+222B integral
  - U+2248 approxequal
  - U+2260 notequal
  - U+2264 lessequal
  - U+2265 greaterequal
  - U+2423 blank
  - U+25CA lozenge
  - U+FB01 fi
  - U+FB02 fl
  - U+FE00 VS1
  - U+FE01 VS2
  - U+FE02 VS3
  - U+FE03 VS4
  - U+FE04 VS5
  - U+FE05 VS6
  - U+FE06 VS7
  - U+FE07 VS8
  - U+FE08 VS9
  - U+FE09 VS10
  - U+FE0A VS11
  - U+FE0B VS12
  - U+FE0C VS13
  - U+FE0D VS14
  - U+FE0E VS15
  - U+FE0F VS16
  - U+FEFF zeroWidthNoBreakSpace
  - U+FFFC objectReplacementCharacter
  - U+FFFD replacementCharacter
- Added variant glyphs
  - DEVANAGARI CHA variants
    - Full Cha with tail
    - Half Cha with no stem or halant
  - DEVANAGARI HEADSTROKE variants
    - Discrete (to show the number of missing characters)
    - Narrow (for use in typography)
    - Filler (zero advance width for use in typography)
  - DEVANAGARI JAIN OM variant (extended headstroke)
- Added Stylistic Set features
  - ss16 uses ligature forms for ra + ukar (or uukar) with nukta
  - ss17 for full Cha with tail, half Cha with no stem or halant
- Added Character Variant features
  - cv21 for headstroke variants discrete, narrow and filler
  - ss22 for Jain Om variants with extended headstroke
  - Graphite only: added features cv01-cv17 to correspond to OpenType ss01-ss17
- Width of typographic spaces have been made more consistent to reflect
  common publishing industry usage. Note that this may affect line and page
  lengths. Affected spaces are
  - U+2003 EN SPACE
  - U+2004 THREE-PER-EM SPACE
  - U+2005 FOUR-PER-EM SPACE
  - U+2006 SIX-PER-EM SPACE
  - U+2009 THIN SPACE
  - U+200A HAIR SPACE
  - U+202F NARROW NO-BREAK SPACE
- Fixed OpenType rendering of double Nga stack with open-Ya to match Graphite
- Fixed OpenType rendering of nukta forms of stemless characters with open-Ya 
  to match Graphite
- Added Graphite rules to reorder ikar before full vowel and possible cons 
  or half-cons 
- Fixed Ra+ukar collision with preceding ukar
- Fixed ikar-anusvara collision on conjuncts
- Fixed misoriented contours and duplicated knots
- Added UFO key and value data to set head table flag bits 0 and 1
- Revised content and format of the documentation

### 22 February 2019 (SIL WSTech team)  Annapurna SIL version 1.204
- Reworked Graphite code to remove duplicates from substitution input classes.
- Fixed Graphite bug involving alternate renderings of the half forms of ya. 
  Fixed default rendering of dya.

### 08 December 2017 (SIL NRSI team)  Annapurna SIL version 1.203
- Matched OpenType with Graphite rendering where "ra halant ra halant" renders 
  as "reph over ra-halant" instead of "eyelash ra" with reph over following cons.
- Fixed Graphite bugs in reph position chaining rules
- Fixed Graphite bug involving ta+ta conjunct half-form

### 10 February 2017 (SIL NRSI team)  Annapurna SIL version 1.202
- Fixed Graphite where reph was skipping the aakar after the ya
- Used TTFautohint for hinting which solved disappearing candrabindu in Bold

### 01 August 2016 (SIL NRSI team)  Annapurna SIL version 1.201
- Fixed Graphite (reordering) issue when reph and ikar are in a cluster
- Fixed Graphite issue related to TypeTuner fonts

### 15 January 2015 (SIL NRSI team)  Annapurna SIL version 1.200
- Added glyph U+0978 from the Devanagari block
- Added half forms of all the consonant-rakar conjuncts
- Fixed a near collision between Ha-Nukta and the uukar
- Fixed many collisions of ekar/aikar over ra with a preceding upper mark
- Hinting was done to enhance the on-screen rendering in Windows and Linux

### 25 October 2012 (SIL NRSI team)  Annapurna SIL version 1.100
- Added glyphs (with OpenType and Graphite support) from the Devanagari block
  - 0900, 093A..093B, 094E..094F, 0955..0957, 0973..0977, 0979..097A
- Added glyphs from the Devanagari Extended block
  - A8E0..A8FB
- Added glyphs from the North Indic Number Forms block
  - A830..A839
- U+dot (and UU+dot) is now attached under the Ra instead of the ligature version
- Graphite feature IDs are now all four-character tags per CSS requirements
- Minor bug fixes

### 12 July 2011 (SIL NRSI team)  Annapurna SIL version 1.001
- Added ligature glyphs and smart code support for minority languages
  - 0930 with 0941 and 093C
  - 0931 with 0941
  - 0931 with 0941 and 093C
  - 0930 with 0942 and 093C
  - 0931 with 0942
  - 0931 with 0942 and 093C
- Fixed design bug in Bold font. The long I with nasal dot had a missing dot
- Minor tweaks by adjusting attachment points and hinting parameters
- Numerous bug fixes in Graphite

### 31 Dec 2010 (SIL NRSI team)  Annapurna SIL version 1.000
- First version released under the SIL Open Font License

