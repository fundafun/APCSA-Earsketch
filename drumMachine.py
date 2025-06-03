from earsketch import *

init()
setTempo(100)

# variable and sound definitions
kick = CIARA_SET_KICK_1
snare = HIPHOP_SNARE_ROLL_007
hihat = CIARA_SET_PERC_HIHAT_1
theme = CIARA_SET_THEME_ATMOS_1

# beat patterns
kickPatternAlt = "0-0-----0-0-----"    
snarePatternAlt = "----0---0-------"
hihatPattern1 = "0-0-0-0-0-0-0-0-"     
hihatPattern2 = "0---0---0---0---"      

# reusable function
def addBeatLoop(beat, sound, track, startMeasure, numMeasures):
    for i in range(numMeasures):
        makeBeat(sound, track, startMeasure + i, beat)

# M 1–2: introduce rhythm 
addBeatLoop(kickPatternAlt, kick, 1, 1, 2)
addBeatLoop(snarePatternAlt, snare, 2, 1, 2)
addBeatLoop(hihatPattern2, hihat, 3, 1, 2)
fitMedia(theme, 4, 1, 3)

# M 3–4: stop hi-hat for a break
addBeatLoop(kickPatternAlt, kick, 1, 3, 2)
addBeatLoop(snarePatternAlt, snare, 2, 3, 2)
# No hi-hat
fitMedia(theme, 4, 3, 5)

# M 5–6: bring hihat back
addBeatLoop(kickPatternAlt, kick, 1, 5, 2)
addBeatLoop(snarePatternAlt, snare, 2, 5, 2)
addBeatLoop(hihatPattern1, hihat, 3, 5, 2)
fitMedia(theme, 4, 5, 7)

# M 7–8: switch hi-hat again
addBeatLoop(kickPatternAlt, kick, 1, 7, 2)
addBeatLoop(snarePatternAlt, snare, 2, 7, 2)
addBeatLoop(hihatPattern2, hihat, 3, 7, 2)
fitMedia(theme, 4, 7, 9)

# sound effects
setEffect(1, VOLUME, GAIN, 5)
setEffect(3, DISTORTION, DISTO_GAIN, 0.3)
setEffect(4, DELAY, DELAY_TIME, 250)

finish()
