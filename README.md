# GEEZ
.
1. downloaded UTF8 format MARC records: 
    https://www.loc.gov/cds/products/MDSConnect-music.html

2. converted UTF8 files into json dictionaries using readmarc_1.py and readmarc_2.py

3. found records cataloged as Rap (Music) in sound disc format via post_sift.py and post_sift2.py, 
    creating a new json dictionary to hold the results

BONUS CODES!!!

4. readLOC_jsonM.py looks at tag data with a count greater than 100 and cleans up extraneous tags like 
    "sigh another album from my not dissipated enough youth"

5. note_test.py looks at the amount of times hip-hop is used in the note field (as was suggested by my supervisor to
    be more inclusive of the term in MARC records
