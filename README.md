# arXiv Paper Cataloguer
-------------------------------------------------------------------------------------------------------

## About

This script runs in the background and watches your downloads folder. Whenever an arXiv article is downloaded, it is renamed according to custom
logic and moved to a directory you specify. 
------------------------------------------------------------------------------------------------------

## Default Renaming Scheme

By default, the paper is renamed as follows: The last names of the first three authors are concatenated by '-'. The title is stripped of special
characters and swapped to lowercase. Spaces in the title are replaced by '-'. The filename is "author1-author2-author3-title-of-paper.pdf"

Examples: 

1. https://arxiv.org/abs/1910.06441 -> "vig-the-wave-trace-and-birkhoff-billiards.pdf"
1. https://arxiv.org/abs/2106.12017 -> "mccleerey-pluri-supported-currents-on-compact-kahler-manifolds.pdf"
1. https://arxiv.org/abs/1706.03762 -> "vaswani-shazeer-parmar-attention-is-all-you-need.pdf"
------------------------------------------------------------------------------------------------------

## Setup

1. open config.py
    - Change SOURCE_DIR to the absolute path of your downloads directory
    - Change TARGET_DIR to the absolute path of the directory you want your papers to be stored.
2. Open arXivdaemon.bat and make sure the path to this project directory is correct
3. Place arXivdaemon.bat in your startup scripts.
------------------------------------------------------------------------------------------------------
## Potential Issues

Older arxiv articles have a naming convention which will currently be missed by this app. It will see anything with id in the forms

1. XXXX.XXXXX
1. XXXX.XXXX

Where 'X' is any digit. Some older articles have ids in the form arch-ive/XXXXXXX and these are not currently captured.
------------------------------------------------------------------------------------------------------

## TODO:

Handle the exception where we download the same paper e.g. we have a paper already catalogued and we try to download it again. This throws an error because
we are trying to rename something to a path that already exists.