#description: improving my earsketch skills from last year. i realized less is more in terms of songs/beats. i wanted to test out the different drum beats, so you will see them in the melody

from earsketch import *
from random import *

init()
setTempo(128)

# Track numbers/variables for easy reference
introTrack = 1
guitarTracks = [2]
drumTracks = [3, 4]
beatTrack = [5, 6, 7]
melodyTrack = 8

# Other Variables: starting measure for the melody
melodyStartMeasure = 6

# Intro: 8-bit analog drums and beat loop to set the tone for the intro
fitMedia(EIGHT_BIT_ANALOG_DRUM_LOOP_004, introTrack, 1, 6)
fitMedia(HIPHOP_STOMP_BEAT_004, introTrack, 16,22)
fitMedia(CIARA_MELANIN_DRUMBEAT_1, introTrack, 32,38)

# Guitar Tracks: layer a guitar loop
fitMedia(Y25_GUITAR_1, guitarTracks[0], 2, 6)

# Drum Tracks: dubstep drum loop that plays beneath the guitar
fitMedia(DUBSTEP_DRUMLOOP_MAIN_001, drumTracks[0], 2, 6)


# Main loop for repeat the rhythm
# Repeats a pattern of melody and beat programming to create structure

for i in range(2):
    # Background 8-bit loop and alternating dubstep drums
	fitMedia(EIGHT_BIT_ANALOG_DRUM_LOOP_004, drumTracks[1], 6 + 16*i, 12 + 16*i)
	fitMedia(DUBSTEP_DRUMLOOP_MAIN_001, drumTracks[0], 16 + 16*i, 22 + 16*i)

	# Random melody: selects different electronic lead clips to play melodic lines

	melodyAudio = [ELECTRO_ANALOGUE_LEAD_009, ELECTRO_ANALOGUE_LEAD_010, ELECTRO_ANALOGUE_LEAD_011,
				   ELECTRO_ANALOGUE_LEAD_012]

    # 4 randomized melody segments across the 16-measure section
	fitMedia(melodyAudio[randint(0, len(melodyAudio) - 1)], melodyTrack, melodyStartMeasure + 4 + 16*i, melodyStartMeasure + 6 + 16*i)
	fitMedia(melodyAudio[randint(0, len(melodyAudio) - 1)], melodyTrack, melodyStartMeasure + 8 + 16*i, melodyStartMeasure + 10 + 16*i)
	fitMedia(melodyAudio[randint(0, len(melodyAudio) - 1)], melodyTrack, melodyStartMeasure + 12 + 16*i, melodyStartMeasure + 14 + 16*i)


    # 3 types of percussion sounds and custom beat strings
	beatAudio = [ELECTRO_DRUM_MAIN_LOOPPART_010, OS_OPENHAT01, OS_LOWTOM04]
	beatList = ["0---0---0-----0-", "0---0-0-0---0-0-", "0---0---0---0---"]
	drumsStartMeasure = 6
    
    #Add beats for 8 measures of the current loop
	for j in range(8):

		makeBeat(beatAudio[0], beatTrack[0], drumsStartMeasure + j + 16*i, beatList[0])
		makeBeat(beatAudio[1], beatTrack[1], drumsStartMeasure + j + 16*i, beatList[1])
		makeBeat(beatAudio[2], beatTrack[2], drumsStartMeasure + j + 16*i, beatList[2])

# Effects: reverb to the intro track to create ambience and a distortion effect with a time based modulation

setEffect(1, REVERB, REVERB_TIME, 100.0)
setEffect(3, DISTORTION, DISTO_GAIN, 0, 8, 30, 22)
setEffect(3, DISTORTION, DISTO_GAIN, 30, 35, 0, 38)


finish()
