from earsketch import *
import random

init()
setTempo(120)

# my selected clips
drum = [CIARA_MELANIN_DRUMBEAT_1,CIARA_ROOTED_DRUMBEAT_1, CIARA_SET_PERC_DISTBASS]
melody = [CIARA_SET_DRUMBEAT_5, CIARA_SET_THEME_PIANO,CIARA_SET_DRUMBEAT_1]
effect = [CIARA_SET_TALK_ADLIB_AH_2, CIARA_SET_TALK_ADLIB_LOFI_2, CIARA_SET_TALK_ADLIB_AH_3]

# 20 measure long melody
for measure in range(1, 20): 
    # random track number
    track = random.randint(1, 4)
    
    # random melody clip on a different track to vary the sound
    melody_clip = random.choice(melody)
    fitMedia(melody_clip, track + 1, measure, measure + 1)

     # random drum pattern from the given options
    drum_clip = random.choice(drum)
    fitMedia(drum_clip, track, measure, measure + 1)
    
    # maybe add an effect?!
    if measure % 4 == 0:
        effect_clip = random.choice(effect)
        fitMedia(effect_clip, track + 2, measure, measure + 0.5)
    
    # random pan effect
    # doesn't sound that great on computer speakers
    pan_value = random.randint(-100, 100)
    setEffect(track, "PAN", "LEFT_RIGHT", -100)

finish()
