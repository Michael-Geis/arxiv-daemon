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

It's fucked because I don't understand how computers work.

------------------------------------------------------------------------------------------------------
## Known Issues

### 1. Older arxiv articles have a naming convention which will currently be missed by this app. It will see anything with id in the forms

1. XXXX.XXXXX
1. XXXX.XXXX

Where 'X' is any digit. Some older articles have ids in the form arch-ive/XXXXXXX and these are not currently captured.

### 3. Right now, the app only runs by cloning the repo and running src/daemon.py with an instance of python which has installed all of the package dependencies in requirements.txt. Working on containerizing the app so that it may be built and run as a docker container.

------------------------------------------------------------------------------------------------------

## TODO:

Handle the exception where we download the same paper e.g. we have a paper already catalogued and we try to download it again. This throws an error because
we are trying to rename something to a path that already exists.