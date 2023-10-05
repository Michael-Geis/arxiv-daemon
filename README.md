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

Step 1. Clone the repository to a local directory

```git clone https://github.com/Michael-Geis/arxiv-daemon.git your-directory```

Step 2. Open the config file `your-directory/src/config.py` in a text editor and make the following changes:
  - change the value of SOURCE_DIR to the absolute path of your downloads folder. For example, mine is
  `c:/users/leems/downloads`
  - change the value of TARGET_DIR to the absolute path of the directory you want to store your papers in. Mine is
  `c:/users/leems/math/papers`

Step 3. Open the startup file `your-directory/startup.bat` in a text editor and change the argument of the `cd` command in line 2 to be the
absolute path of your copy of the repository, e.g. the absolute path of `your-directory`. Mine is
`c:/users/leems/coding/projects/arxiv-daemon`

Step 4. Create a shortcut to `your-directory/startup.bat` and place it in your startup scripts folder. To open this on windows, press
Win + r and type "shell:startup"

Now the next time you restart your pc, any arxiv downloads will be automatically renamed and moved.


------------------------------------------------------------------------------------------------------
## Known Issues

### 1. Older arxiv articles have a naming convention which will currently be missed by this app. It will see anything with id in the forms

1. XXXX.XXXXX
1. XXXX.XXXX

Where 'X' is any digit. Some older articles have ids in the form arch-ive/XXXXXXX and these are not currently captured.

### 2. Dashes are currently being removed if they are inside the title of the paper

### 3. Right now, the app only runs by cloning the repo and running src/daemon.py with an instance of python which has installed all of the package dependencies in requirements.txt. Working on containerizing the app so that it may be built and run as a docker container.

------------------------------------------------------------------------------------------------------

## TODO:

Handle the exception where we download the same paper e.g. we have a paper already catalogued and we try to download it again. This throws an error because
we are trying to rename something to a path that already exists.
