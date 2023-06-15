---
title: Annapurna SIL - Version History
fontversion: 2.000
---

22 February 2019 (SIL WSTech team)  Annapurna SIL version 1.204
- Reworked Graphite code to remove duplicates from substitution input classes.
- Fixed Graphite bug involving alternate renderings of the half forms of ya. 
  Fixed default rendering of dya.

08 December 2017 (SIL NRSI team)  Annapurna SIL version 1.203
- Matched OpenType with Graphite rendering where "ra halant ra halant" renders 
  as "reph over ra-halant" instead of "eyelash ra" with reph over following cons.
- Fixed Graphite bugs in reph position chaining rules
- Fixed Graphite bug involving ta+ta conjunct half-form

10 February 2017 (SIL NRSI team)  Annapurna SIL version 1.202
- Fixed Graphite where reph was skipping the aakar after the ya
- Used TTFautohint for hinting which solved disappearing candrabindu in Bold

01 August 2016 (SIL NRSI team)  Annapurna SIL version 1.201
- Fixed Graphite (reordering) issue when reph and ikar are in a cluster
- Fixed Graphite issue related to TypeTuner fonts

15 January 2015 (SIL NRSI team)  Annapurna SIL version 1.200
- Added glyph U+0978 from the Devanagari block
- Added half forms of all the consonant-rakar conjuncts
- Fixed a near collision between Ha-Nukta and the uukar
- Fixed many collisions of ekar/aikar over ra with a preceding upper mark
- Hinting was done to enhance the on-screen rendering in Windows and Linux

25 October 2012 (SIL NRSI team)  Annapurna SIL version 1.100
- Added glyphs (with OpenType and Graphite support) from the Devanagari block
  *0900, 093A..093B, 094E..094F, 0955..0957, 0973..0977, 0979..097A
- Added glyphs from the Devanagari Extended block
  *A8E0..A8FB
- Added glyphs from the North Indic Number Forms block
  *A830..A839
- U+dot (and UU+dot) is now attached under the Ra instead of the ligature version
- Graphite feature IDs are now all four-character tags per CSS requirements
- Minor bug fixes

12 July 2011 (SIL NRSI team)  Annapurna SIL version 1.001
- Added ligature glyphs and smart code support for minority languages
  * 0930 with 0941 and 093C
  * 0931 with 0941
  * 0931 with 0941 and 093C
  * 0930 with 0942 and 093C
  * 0931 with 0942
  * 0931 with 0942 and 093C
- Fixed design bug in Bold font. The long I with nasal dot had a missing dot
- Minor tweaks by adjusting attachment points and hinting parameters
- Numerous bug fixes in Graphite

31 Dec 2010 (SIL NRSI team)  Annapurna SIL version 1.000
- First version released under the SIL Open Font License
