
from earsketch import *

init()
setTempo(100)

# drums & percussion
drumBeat1 = RD_UK_HOUSE_MAINBEAT_10
drumBeat2 = CIARA_MELANIN_DRUMBEAT_1
drumBeat3 = CIARA_SET_DRUMBEAT_1
percussion = CIARA_SET_PERC_SHAKER

# bass
bass1 = CIARA_SET_BASSLINE_1
bass2 = CIARA_SET_BASSLINE_2

# fx
fxRise = HOUSE_BREAKBEAT_003

# song sections and functions
def intro():
    fitMedia(percussion, 1, 1, 3)
    fitMedia(fxRise, 3, 1.5, 3)

def verse():
    fitMedia(drumBeat1, 1, 3, 7)
    fitMedia(bass1, 2, 3, 7)

def chorus():
    fitMedia(drumBeat2, 1, 7, 11)
    fitMedia(percussion, 4, 7, 11)

def bridge():
    for m in range(11, 13):
        fitMedia(bass2, 2, m, m + 1)

def drop():
    fitMedia(drumBeat3, 2, 13, 17)
    fitMedia(fxRise, 3, 13, 14)

# song structure
intro()
verse()
chorus()
bridge()
drop()

finish()
