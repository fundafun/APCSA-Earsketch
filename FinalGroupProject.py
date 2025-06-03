## Song name: Sickocode
#-----------------------#
#      Setup           #
#-----------------------#
from earsketch import *
setTempo(140)  # Set tempo of the track to 140 BPM

#-----------------------#
# Beat Class (Charlie) #
#-----------------------#
class Beat():
    # Constructor to create beats using a string of characters
    def __init__(self, notes:str):
        self.notes = []
        dt = 1.0 / len(notes)  # Each note duration relative to full measure
        print(dt)
        for x in range(0, len(notes)):
            if notes[x:x+1] == "-":
                continue  # Dash means rest
            elif notes[x:x+1] == "+":
                self.notes[len(self.notes)-1][2] += dt  # Extend last note
            else:
                self.notes.append([notes[x:x+1], x*dt, (x+1)*dt])  # Add note with start & end time

    def addNote(self, note:str, start:float, end:float):
        self.notes.append([note, start, end])

    def getNotes(self):
        return self.notes

#-----------------------------#
# Instrument Class (Charlie) #
#-----------------------------#
class Instrument():
    def __init__(self, notes:dict):
        self.notes = notes

    def playNote(self, startMeasure:int, startBeat:float, endBeat:float, note:str, track:int):
        fitMedia(self.notes[note], track, startMeasure+startBeat, startMeasure+endBeat)

    def playBeat(self, beat:Beat, startMeasure:int, track:int):
        for x in beat.getNotes():
            self.playNote(startMeasure, x[1], x[2], x[0], track)

#-----------------------------#
# Sebastian’s Effects Tools  #
#-----------------------------#
def applyVolFade_50_1(t, V, s, e):  
    setEffect(t, VOLUME, GAIN, -50, s, V, s+1)
    setEffect(t, VOLUME, GAIN, V, e-1, -50, e)

def setDelay(t, s, e, time, feedback, mix):
    setEffect(t, DELAY, DELAY_TIME, time, s, time, e)
    setEffect(t, DELAY, DELAY_FEEDBACK, feedback, s, feedback, e)
    setEffect(t, DELAY, MIX, mix, s, mix, e)

#-----------------------------#
# Sound File Definitions     #
#-----------------------------#
# Quinn’s SFX
quinn1SFX = RD_TRAP_SFX_GATEDRISE_1
quinn2SFX = Y14_SFX_1
quinn3SFX = DUBSTEP_FILTERCHORD_001

# Sebastian's stretched sounds
sebastian2 = createAudioStretch(JWOLF_COTG_THEME_SYNTH, 0.5)
sebastian1 = createAudioStretch(RADICAL_NOTHING_SYNTH_1, 0.5)

# Adi’s beat foundation
WASSUP = createAudioStretch(ADECHOLA_WASSUP_MAIN_MUSIC_AUDIOTRIMMER_COM_, 1/0.883280757)

# Quinn’s Piano drop
PIANO = createAudioStretch(ADECHOLA_KING_OF_ATLANTA_AGGRESSIVE_PIANO_168BPM, 168.0/140.0)

# Taglines & Vocal Snippets
ALIVE = ADECHOLA_ALIVEEE
HAHA = ADECHOLA_SWAMP_IZZO_VOICE_TAG_AHAHAH
ROCK = ADECHOLA_SWAMP_IZZO_VOICE_TAG_LIVING_UPON_A_ROCK
MUSIC = ADECHOLA_SWAMP_IZZO_VOICE_TAG_MUSIC

#-----------------------------#
# Intro: Building Energy     #
#-----------------------------#
fitMedia(WASSUP, 1, 1, 18)
fitMedia(quinn1SFX, 2, 17, 19.5)
fitMedia(quinn2SFX, 2, 35, 37.5)
fitMedia(quinn3SFX, 2, 53, 55)
fitMedia(PIANO, 5, 28, 54)

# Sebastian’s layered synth build-ups
for start in [10, 26, 42]:
    fitMedia(sebastian1, 3, start, start + 8)
    fitMedia(sebastian2, 3, start + 8, start + 12)

#-----------------------------#
# Charlie’s Custom Bass      #
#-----------------------------#
BassCharlieNotes = {
    "1": AN0CT0LING_BOOM_BASS_B0,
    "2": AN0CT0LING_BOOM_BASS_CS0,
    "3": AN0CT0LING_BOOM_BASS_D0,
    "4": AN0CT0LING_BOOM_BASS_E0,
    "5": AN0CT0LING_BOOM_BASS_FS0,
    "6": AN0CT0LING_BOOM_BASS_G0,
    "7": AN0CT0LING_BOOM_BASS_A1,
    "8": AN0CT0LING_BOOM_BASS_B1,
    "9": AN0CT0LING_BOOM_BASS_CS1,
    "0": AN0CT0LING_BOOM_BASS_D1,
    "!": AN0CT0LING_BOOM_BASS_E1,
    "@": AN0CT0LING_BOOM_BASS_FS1,
    "#": AN0CT0LING_BOOM_BASS_G1,
    "$": AN0CT0LING_BOOM_BASS_A2,
    "%": AN0CT0LING_BOOM_BASS_B2
}
guitarCharlie = Instrument(BassCharlieNotes)

# Bass pattern for intro
StartBassline = [
    Beat("8+------"),
    Beat("8+--9+-0"),
    Beat("0+!+----"),
    Beat("!+--9+-0"),
    Beat("0+9+----"),
    Beat("!+--9+-0"),
    Beat("0+9+----"),
]

# Bass pattern for chorus/outro
MainBassline = [
    Beat("9+9+----"),
    Beat("--------"),
    Beat("9+9+----"),
    Beat("--------"),
    Beat("!+!+----"),
    Beat("--------"),
    Beat("0+0+----"),
    Beat("9+9+----")
]

# Play ending bass multiple times
for x in range(0, 3):
    for y in range(0, len(MainBassline)):
        guitarCharlie.playBeat(MainBassline[y], 28 + y + x * len(MainBassline), 4)

guitarCharlie.playBeat(MainBassline[0], 52, 4)

# Play intro bass
for x in range(0, 1):
    for y in range(0, len(StartBassline)):
        guitarCharlie.playBeat(StartBassline[y], 3 + y + x * len(StartBassline), 12)

# Long bass fade-in through intro
fitMedia(createAudioStretch(AN0CT0LING_BOOM_BASS_B0, 25), 13, 1, 28)
setEffect(13, VOLUME, GAIN, -50, 1, 10, 28)

#-----------------------------#
# Audio Effects               #
#-----------------------------#
applyVolFade_50_1(1, 0, 1, 18)   # Bass fade in
setEffect(2, REVERB, REVERB_DAMPFREQ, 1000)
applyVolFade_50_1(2, 0, 17, 37.5)
setEffect(2, VOLUME, GAIN, -50, 53, -10, 53.5)

# Delay and volume fade for synth layers
setDelay(3, 1, 54, 200, -50, 1.0)
applyVolFade_50_1(3, -5, 10, 54)

# Static volume for track 4
setEffect(4, VOLUME, GAIN, 5)

# Reverb and fade on piano
applyVolFade_50_1(5, -5, 28, 54)
setEffect(5, REVERB, MIX, 1.0)

# Chorus effect
setEffect(12, VOLUME, GAIN, -20)
setEffect(12, CHORUS, CHORUS_NUMVOICES, 8)
setEffect(12, CHORUS, CHORUS_RATE, 8)
setEffect(12, CHORUS, CHORUS_MOD, 0.8)

#-----------------------------#
# Nikka’s Vocals & Sections  #
#-----------------------------#
# [Intro]
fitMedia(NTDI_VOCAL_NIKKA_INTRO, 8, 1, 7)
setEffect(8, REVERB, MIX, 0.2)
setEffect(8, REVERB, REVERB_TIME, 800)

# [Verse 1]
fitMedia(NTDI_VOCAL_NIKKA_JAVA_BAR, 9, 6.5, 12.5)

# [Ad-lib]
fitMedia(NTDI_VOCAL_NIKKA_ADLIB_3, 8, 12, 13.3)

# [Verse 2]
fitMedia(NTDI_VOCAL_NIKKA_DAROL_VERSE, 9, 12.5, 15.5)

# [Bridge]
fitMedia(NTDI_VOCAL_NIKKA_BRIDGE_2, 8, 15, 17.5)

# [Quinn’s Section]
fitMedia(NTDI_VOCAL_NIKKA_QUINN_BAR, 9, 20, 28)

# [Ad-lib - Charlie Tag]
fitMedia(NTDI_VOCAL_NIKKA_ADLIB_CHARLIE, 8, 27.5, 29.5)

# [Chorus 1]
fitMedia(NTDI_VOCAL_NIKKA_CHORUS_1, 9, 29, 36)

# [Edward's Verse]
fitMedia(NTDI_VOCAL_NIKKA_EDDY_VERSE, 10, 33.2, 40)

# [Chorus 2]
fitMedia(NTDI_VOCAL_NIKKA_CHORUS_2, 9, 37.5, 44)

# [Hard Verse]
fitMedia(NTDI_VOCAL_NIKKA_HARD_BAR, 10, 41.9, 47)

# [Ad-lib to Outro]
fitMedia(NTDI_VOCAL_NIKKA_ADLIB, 8, 48, 52)

#-----------------------------#
# Voice Tags (Intro/Outro)   #
#-----------------------------#
fitMedia(HAHA, 9, 1, 2)
fitMedia(ROCK, 10, 2, 5)
fitMedia(MUSIC, 10, 6, 7)
fitMedia(HAHA, 10, 7, 8)

# Outro Energy
fitMedia(ALIVE, 11, 42, 48)
