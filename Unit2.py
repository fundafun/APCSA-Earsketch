from earsketch import *

init()
setTempo(100)

#Main Tracks
drums = 1
melody = 2
bass = 3

# Define clips
drumClip = CIARA_SET_DRUMBEAT_5
melodyClip = YG_TRAP_SYNTH_MELODY_1
bassClip = CIARA_SET_BASSLINE_1

# Place 3 clips over 4 measures
for measure in range(1, 5):
    fitMedia(drumClip, drums, measure, measure + 1)
    fitMedia(melodyClip, melody, measure, measure + 1)
    fitMedia(bassClip, bass, measure, measure + 1)

# Add extra beats to reach 8 measures
fitMedia(drumClip, drums, 5, 9)
fitMedia(melodyClip, melody, 5, 9)
fitMedia(bassClip, bass, 5, 9)

# Time effect: reverb on the melody
setEffect(melody, "REVERB", "REVERB_TIME", 2000)

# Volume effect: pan the bass left to adjust the volume
setEffect(bass, "PAN", "LEFT_RIGHT", -50)
setEffect(drums, "VOLUME", "GAIN", -1)
setEffect(bass, "VOLUME", "GAIN", -5)

# Volume fades on melody from measure 5 to 9
setEffect(melody, "VOLUME", "GAIN", 0, 5, -60, 9)

finish()
