#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on June 09, 2021, at 13:12
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard
from utils.song_loader import SongLoader



# Ensure that relative paths start from the same directory as this script

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'experiment_eo_ec'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'group': 'EOEC'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\miche\\EIT\\INTERNSHIP_MYBRAIN\\experimental_phase\\experiment_continuous_annotation\\emotion_music_experiment_eo_ec.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[900, 900], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
welcome_instruction = visual.TextStim(win=win, name='welcome_instruction',
    text='Welcome to the Emotion Music experiment.\n\nThis is the recorded experimental session.\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcome_instructions_2 = visual.TextStim(win=win, name='welcome_instructions_2',
    text='The experiment is based on timed routines, it is important that you follow the instructions and answer the song ratings in the given time (15 seconds).\n\nYour main task is to listen to the proposed music playlist and annotate your emotions continuously by moving the red reticle on the Valence-Arousal space.\n\nThe total length of the experiment is about 20-25 minutes, with the possibility of a short break in the middle.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
start_button = visual.ButtonStim(win, 
   text='Start Experiment', font='Arvo',
   pos=(0, 0),
   letterHeight=0.05,
   size=None, borderWidth=0.0,
   fillColor='darkgrey', borderColor=None,
   color='white', colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='start_button')
start_button.buttonClock = core.Clock()

# Initialize components for Routine "trials_first_part"
trials_first_partClock = core.Clock()
valence_arousal_space = visual.ImageStim(
    win=win,
    name='valence_arousal_space', 
    image='res\\\\img\\\\valence_arousal_space_basic.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
reticle = visual.ImageStim(
    win=win,
    name='reticle', 
    image='res\\\\img\\\\reticle.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.075, 0.075),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
song_one = sound.Sound(None, secs=-1.0, stereo=True, hamming=True,
    name='song_one')
song_one.setVolume(1.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
open_eyes = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='open_eyes')
open_eyes.setVolume(0.5)
win.allowStencil = True
song_one_rating = visual.Form(win=win, name='song_one_rating',
    items='res\\\\forms\\\\rating_form.csv',
    textHeight=0.03,
    randomize=False,
    size=(1, 0.7),
    pos=(0, 0),
    style='dark',
    itemPadding=0.1,)
white_noise_one = sound.Sound('res\\1 min wn.wav', secs=-1.0, stereo=True, hamming=True,
    name='white_noise_one')
white_noise_one.setVolume(0.7)
instruction_ec = visual.TextStim(win=win, name='instruction_ec',
    text='Now CLOSE your eyes and get ready for the next song.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
eyes_closed = visual.ImageStim(
    win=win,
    name='eyes_closed', 
    image='res\\\\img\\\\eye_closed.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
valence_arousal_space_2 = visual.ImageStim(
    win=win,
    name='valence_arousal_space_2', 
    image='res\\\\img\\\\valence_arousal_space_basic.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
song_two = sound.Sound(None, secs=-1.0, stereo=True, hamming=True,
    name='song_two')
song_two.setVolume(1.0)
reticle_2 = visual.ImageStim(
    win=win,
    name='reticle_2', 
    image='res\\\\img\\\\reticle.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.075, 0.075),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
open_eyes_two = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='open_eyes_two')
open_eyes_two.setVolume(0.5)
win.allowStencil = True
song_two_rating = visual.Form(win=win, name='song_two_rating',
    items='res\\\\forms\\\\rating_form.csv',
    textHeight=0.03,
    randomize=False,
    size=(1, 0.7),
    pos=(0, 0),
    style='dark',
    itemPadding=0.05,)
white_noise_two = sound.Sound('res\\1 min wn.wav', secs=-1.0, stereo=True, hamming=True,
    name='white_noise_two')
white_noise_two.setVolume(0.7)
instruction_eo = visual.TextStim(win=win, name='instruction_eo',
    text='Now OPEN your eyes and get ready for the next song.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
eyes_open_2 = visual.ImageStim(
    win=win,
    name='eyes_open_2', 
    image='res\\\\img\\\\eye_open.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)

# Initialize components for Routine "mid_break"
mid_breakClock = core.Clock()
break_instruction = visual.TextStim(win=win, name='break_instruction',
    text='You are on a break.\n\nFeel free to look around and relax your eyes.\n\nPlease do NOT remove your headset.\n\nWhen you are ready to continue, click the button.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resume_experiment = visual.ButtonStim(win, 
   text='Resume Experiment', font='Arvo',
   pos=(0, 0),
   letterHeight=0.05,
   size=None, borderWidth=0.0,
   fillColor='darkgrey', borderColor=None,
   color='white', colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='resume_experiment')
resume_experiment.buttonClock = core.Clock()

# Initialize components for Routine "white_noise_break"
white_noise_breakClock = core.Clock()
after_break_white_noise = sound.Sound('res\\1 min wn.wav', secs=-1.0, stereo=True, hamming=True,
    name='after_break_white_noise')
after_break_white_noise.setVolume(1.0)
after_break_instruction = visual.TextStim(win=win, name='after_break_instruction',
    text='We are about to resume the experiment.\n\nThe next trial will begin with your eyes OPEN.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
first_eyes_instruction_2 = visual.ImageStim(
    win=win,
    name='first_eyes_instruction_2', 
    image='res\\\\img\\\\eye_open.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "trials_second_part"
trials_second_partClock = core.Clock()
valence_arousal_space_3 = visual.ImageStim(
    win=win,
    name='valence_arousal_space_3', 
    image='res\\\\img\\\\valence_arousal_space_basic.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
reticle_3 = visual.ImageStim(
    win=win,
    name='reticle_3', 
    image='res\\\\img\\\\reticle.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.075, 0.075),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
song_one_2 = sound.Sound(None, secs=-1.0, stereo=True, hamming=True,
    name='song_one_2')
song_one_2.setVolume(1.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
open_eyes_2 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='open_eyes_2')
open_eyes_2.setVolume(0.5)
win.allowStencil = True
song_one_rating_2 = visual.Form(win=win, name='song_one_rating_2',
    items='res\\\\forms\\\\rating_form.csv',
    textHeight=0.03,
    randomize=False,
    size=(1, 0.7),
    pos=(0, 0),
    style='dark',
    itemPadding=0.1,)
white_noise_one_2 = sound.Sound('res\\1 min wn.wav', secs=-1.0, stereo=True, hamming=True,
    name='white_noise_one_2')
white_noise_one_2.setVolume(0.7)
instruction_ec_2 = visual.TextStim(win=win, name='instruction_ec_2',
    text='Now CLOSE your eyes and get ready for the next song.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
eyes_closed_2 = visual.ImageStim(
    win=win,
    name='eyes_closed_2', 
    image='res\\\\img\\\\eye_closed.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
valence_arousal_space_4 = visual.ImageStim(
    win=win,
    name='valence_arousal_space_4', 
    image='res\\\\img\\\\valence_arousal_space_basic.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
song_two_2 = sound.Sound(None, secs=-1.0, stereo=True, hamming=True,
    name='song_two_2')
song_two_2.setVolume(1.0)
reticle_4 = visual.ImageStim(
    win=win,
    name='reticle_4', 
    image='res\\\\img\\\\reticle.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.075, 0.075),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()
open_eyes_two_2 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='open_eyes_two_2')
open_eyes_two_2.setVolume(0.5)
win.allowStencil = True
song_two_rating_2 = visual.Form(win=win, name='song_two_rating_2',
    items='res\\\\forms\\\\rating_form.csv',
    textHeight=0.03,
    randomize=False,
    size=(1, 0.7),
    pos=(0, 0),
    style='dark',
    itemPadding=0.05,)
white_noise_two_2 = sound.Sound('res\\1 min wn.wav', secs=-1.0, stereo=True, hamming=True,
    name='white_noise_two_2')
white_noise_two_2.setVolume(0.7)
instruction_eo_2 = visual.TextStim(win=win, name='instruction_eo_2',
    text='Now OPEN your eyes and get ready for the next song.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
eyes_open = visual.ImageStim(
    win=win,
    name='eyes_open', 
    image='res\\\\img\\\\eye_open.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)

# Initialize components for Routine "exit_rest_state"
exit_rest_stateClock = core.Clock()
resting_state_instructions_2 = visual.TextStim(win=win, name='resting_state_instructions_2',
    text='Congratulations, you made it!\nBefore you leave, we need to record your "resting" state with both eyes OPEN and eyes CLOSED for 2 minutes each.\n\nThink of it as short meditation session, relax your brain and focus on your breathing.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
rest_state_eyes_open_2 = visual.TextStim(win=win, name='rest_state_eyes_open_2',
    text='We start we eyes OPEN, get ready!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
rest_state_eyes_open_icon_2 = visual.ImageStim(
    win=win,
    name='rest_state_eyes_open_icon_2', 
    image='res\\\\img\\\\eye_open.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
rest_eyes_closed_2 = visual.TextStim(win=win, name='rest_eyes_closed_2',
    text="Now eyes CLOSED, a sound will tell you when it's over.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
rest_eyes_closed_icon_2 = visual.ImageStim(
    win=win,
    name='rest_eyes_closed_icon_2', 
    image='res\\\\img\\\\eye_closed.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
sound_2 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
text = visual.TextStim(win=win, name='text',
    text='And this is the END!\n\nThanks again for participating, please do NOT touch or close anything, the researcher will come to help you remove the headset. This window will close automatically...',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
introComponents = [welcome_instruction, welcome_instructions_2, start_button]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_instruction* updates
    if welcome_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_instruction.frameNStart = frameN  # exact frame index
        welcome_instruction.tStart = t  # local t and not account for scr refresh
        welcome_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_instruction, 'tStartRefresh')  # time at next scr refresh
        welcome_instruction.setAutoDraw(True)
    if welcome_instruction.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > welcome_instruction.tStartRefresh + 15.0-frameTolerance:
            # keep track of stop time/frame for later
            welcome_instruction.tStop = t  # not accounting for scr refresh
            welcome_instruction.frameNStop = frameN  # exact frame index
            win.timeOnFlip(welcome_instruction, 'tStopRefresh')  # time at next scr refresh
            welcome_instruction.setAutoDraw(False)
    
    # *welcome_instructions_2* updates
    if welcome_instructions_2.status == NOT_STARTED and tThisFlip >= 15.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_instructions_2.frameNStart = frameN  # exact frame index
        welcome_instructions_2.tStart = t  # local t and not account for scr refresh
        welcome_instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_instructions_2, 'tStartRefresh')  # time at next scr refresh
        welcome_instructions_2.setAutoDraw(True)
    if welcome_instructions_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > welcome_instructions_2.tStartRefresh + 40.0-frameTolerance:
            # keep track of stop time/frame for later
            welcome_instructions_2.tStop = t  # not accounting for scr refresh
            welcome_instructions_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(welcome_instructions_2, 'tStopRefresh')  # time at next scr refresh
            welcome_instructions_2.setAutoDraw(False)
    
    # *start_button* updates
    if start_button.status == NOT_STARTED and tThisFlip >= 55.0-frameTolerance:
        # keep track of start time/frame for later
        start_button.frameNStart = frameN  # exact frame index
        start_button.tStart = t  # local t and not account for scr refresh
        start_button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_button, 'tStartRefresh')  # time at next scr refresh
        start_button.setAutoDraw(True)
    if start_button.status == STARTED:
        # check whether start_button has been pressed
        if start_button.isClicked:
            if not start_button.wasClicked:
                start_button.timesOn.append(start_button.buttonClock.getTime()) # store time of first click
                start_button.timesOff.append(start_button.buttonClock.getTime()) # store time clicked until
            else:
                start_button.timesOff[-1] = start_button.buttonClock.getTime() # update time clicked until
            if not start_button.wasClicked:
                continueRoutine = False  # end routine when start_button is clicked
                None
            start_button.wasClicked = True  # if start_button is still clicked next frame, it is not a new click
        else:
            start_button.wasClicked = False  # if start_button is clicked next frame, it is a new click
    else:
        start_button.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
        start_button.wasClicked = False  # if start_button is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_instruction.started', welcome_instruction.tStartRefresh)
thisExp.addData('welcome_instruction.stopped', welcome_instruction.tStopRefresh)
thisExp.addData('welcome_instructions_2.started', welcome_instructions_2.tStartRefresh)
thisExp.addData('welcome_instructions_2.stopped', welcome_instructions_2.tStopRefresh)
thisExp.addData('start_button.started', start_button.tStartRefresh)
thisExp.addData('start_button.stopped', start_button.tStopRefresh)
thisExp.addData('start_button.numClicks', start_button.numClicks)
if start_button.numClicks:
   thisExp.addData('start_button.timesOn', start_button.timesOn)
   thisExp.addData('start_button.timesOff', start_button.timesOff)
else:
   thisExp.addData('start_button.timesOn', "")
   thisExp.addData('start_button.timesOff', "")
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
phase_1 = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='phase_1')
thisExp.addLoop(phase_1)  # add the loop to the experiment
thisPhase_1 = phase_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPhase_1.rgb)
if thisPhase_1 != None:
    for paramName in thisPhase_1:
        exec('{} = thisPhase_1[paramName]'.format(paramName))

# Setup song loader and a randomized playlist
song_loader = SongLoader()
playlist_p1 = song_loader.generate_shuffle_playlist('phase_1')
print(playlist_p1)

# keep track of the trial counter for loading song conditions
trial_counter = 0

# init mouse position
mouse_first_frame = True
mouse_2_first_frame = True

for thisPhase_1 in phase_1:

    currentLoop = phase_1
    # abbreviate parameter names if possible (e.g. rgb = thisPhase_1.rgb)
    if thisPhase_1 != None:
        for paramName in thisPhase_1:
            exec('{} = thisPhase_1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trials_first_part"-------
    continueRoutine = True
    routineTimer.add(190.000000)
    # update component parameters for each repeat

    # setup sound sources for current loop
    sound_source_one = playlist_p1[trial_counter][0]
    sound_source_two = playlist_p1[trial_counter][1]
    song_one.setSound(sound_source_one, secs=60.0, hamming=True)
    song_one.setVolume(1.0, log=False)
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    open_eyes.setSound('A', secs=1.0, hamming=True)
    open_eyes.setVolume(0.5, log=False)
    white_noise_one.setSound('res\\1 min wn.wav', secs=15.0, hamming=True)
    white_noise_one.setVolume(0.7, log=False)
    song_two.setSound(sound_source_two, secs=60.0, hamming=True)
    song_two.setVolume(1.0, log=False)

    # increase condition counter for next loop
    trial_counter += 1

    # setup some python lists for storing info about the mouse_2
    mouse_2.x = []
    mouse_2.y = []
    mouse_2.leftButton = []
    mouse_2.midButton = []
    mouse_2.rightButton = []
    mouse_2.time = []
    gotValidClick = False  # until a click is received
    open_eyes_two.setSound('A', secs=1.0, hamming=True)
    open_eyes_two.setVolume(0.5, log=False)
    white_noise_two.setSound('res\\1 min wn.wav', secs=15.0, hamming=True)
    white_noise_two.setVolume(0.7, log=False)
    # keep track of which components have finished
    trials_first_partComponents = [valence_arousal_space, reticle, song_one, mouse, open_eyes, song_one_rating, white_noise_one, instruction_ec, eyes_closed, valence_arousal_space_2, song_two, reticle_2, mouse_2, open_eyes_two, song_two_rating, white_noise_two, instruction_eo, eyes_open_2]
    for thisComponent in trials_first_partComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trials_first_partClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trials_first_part"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trials_first_partClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trials_first_partClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *valence_arousal_space* updates
        if valence_arousal_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            valence_arousal_space.frameNStart = frameN  # exact frame index
            valence_arousal_space.tStart = t  # local t and not account for scr refresh
            valence_arousal_space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(valence_arousal_space, 'tStartRefresh')  # time at next scr refresh
            valence_arousal_space.setAutoDraw(True)
        if valence_arousal_space.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > valence_arousal_space.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                valence_arousal_space.tStop = t  # not accounting for scr refresh
                valence_arousal_space.frameNStop = frameN  # exact frame index
                win.timeOnFlip(valence_arousal_space, 'tStopRefresh')  # time at next scr refresh
                valence_arousal_space.setAutoDraw(False)
        
        # *reticle* updates
        if reticle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reticle.frameNStart = frameN  # exact frame index
            reticle.tStart = t  # local t and not account for scr refresh
            reticle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reticle, 'tStartRefresh')  # time at next scr refresh
            reticle.setAutoDraw(True)
        if reticle.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > reticle.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                reticle.tStop = t  # not accounting for scr refresh
                reticle.frameNStop = frameN  # exact frame index
                win.timeOnFlip(reticle, 'tStopRefresh')  # time at next scr refresh
                reticle.setAutoDraw(False)
        # start/stop song_one
        if song_one.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            song_one.frameNStart = frameN  # exact frame index
            song_one.tStart = t  # local t and not account for scr refresh
            song_one.tStartRefresh = tThisFlipGlobal  # on global time
            song_one.play(when=win)  # sync with win flip
        if song_one.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > song_one.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                song_one.tStop = t  # not accounting for scr refresh
                song_one.frameNStop = frameN  # exact frame index
                win.timeOnFlip(song_one, 'tStopRefresh')  # time at next scr refresh
                song_one.stop()
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                mouse.tStop = t  # not accounting for scr refresh
                mouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse, 'tStopRefresh')  # time at next scr refresh
                mouse.status = FINISHED
        if mouse.status == STARTED:  # only update if started and not finished!
            if mouse_first_frame:
                mouse.setPos([0, 0])
                mouse_first_frame = False
            x, y = mouse.getPos()
            reticle.pos = [x, y]
            mouse.x.append(x)
            mouse.y.append(y)
            buttons = mouse.getPressed()
            mouse.leftButton.append(buttons[0])
            mouse.midButton.append(buttons[1])
            mouse.rightButton.append(buttons[2])
            mouse.time.append(mouse.mouseClock.getTime())
        # start/stop open_eyes
        if open_eyes.status == NOT_STARTED and tThisFlip >= 59.0-frameTolerance:
            # keep track of start time/frame for later
            open_eyes.frameNStart = frameN  # exact frame index
            open_eyes.tStart = t  # local t and not account for scr refresh
            open_eyes.tStartRefresh = tThisFlipGlobal  # on global time
            open_eyes.play(when=win)  # sync with win flip
        if open_eyes.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > open_eyes.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                open_eyes.tStop = t  # not accounting for scr refresh
                open_eyes.frameNStop = frameN  # exact frame index
                win.timeOnFlip(open_eyes, 'tStopRefresh')  # time at next scr refresh
                open_eyes.stop()
        
        # *song_one_rating* updates
        if song_one_rating.status == NOT_STARTED and tThisFlip >= 60.0-frameTolerance:
            # keep track of start time/frame for later
            song_one_rating.frameNStart = frameN  # exact frame index
            song_one_rating.tStart = t  # local t and not account for scr refresh
            song_one_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(song_one_rating, 'tStartRefresh')  # time at next scr refresh
            song_one_rating.setAutoDraw(True)
        if song_one_rating.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > song_one_rating.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                song_one_rating.tStop = t  # not accounting for scr refresh
                song_one_rating.frameNStop = frameN  # exact frame index
                win.timeOnFlip(song_one_rating, 'tStopRefresh')  # time at next scr refresh
                song_one_rating.setAutoDraw(False)
        # start/stop white_noise_one
        if white_noise_one.status == NOT_STARTED and tThisFlip >= 80.0-frameTolerance:
            # keep track of start time/frame for later
            white_noise_one.frameNStart = frameN  # exact frame index
            white_noise_one.tStart = t  # local t and not account for scr refresh
            white_noise_one.tStartRefresh = tThisFlipGlobal  # on global time
            white_noise_one.play(when=win)  # sync with win flip
        if white_noise_one.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > white_noise_one.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                white_noise_one.tStop = t  # not accounting for scr refresh
                white_noise_one.frameNStop = frameN  # exact frame index
                win.timeOnFlip(white_noise_one, 'tStopRefresh')  # time at next scr refresh
                white_noise_one.stop()
        
        # *instruction_ec* updates
        if instruction_ec.status == NOT_STARTED and tThisFlip >= 80.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_ec.frameNStart = frameN  # exact frame index
            instruction_ec.tStart = t  # local t and not account for scr refresh
            instruction_ec.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_ec, 'tStartRefresh')  # time at next scr refresh
            instruction_ec.setAutoDraw(True)
        if instruction_ec.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_ec.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                instruction_ec.tStop = t  # not accounting for scr refresh
                instruction_ec.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruction_ec, 'tStopRefresh')  # time at next scr refresh
                instruction_ec.setAutoDraw(False)
        
        # *eyes_closed* updates
        if eyes_closed.status == NOT_STARTED and tThisFlip >= 90.0-frameTolerance:
            # keep track of start time/frame for later
            eyes_closed.frameNStart = frameN  # exact frame index
            eyes_closed.tStart = t  # local t and not account for scr refresh
            eyes_closed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eyes_closed, 'tStartRefresh')  # time at next scr refresh
            eyes_closed.setAutoDraw(True)
        if eyes_closed.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eyes_closed.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                eyes_closed.tStop = t  # not accounting for scr refresh
                eyes_closed.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eyes_closed, 'tStopRefresh')  # time at next scr refresh
                eyes_closed.setAutoDraw(False)
        
        # *valence_arousal_space_2* updates
        if valence_arousal_space_2.status == NOT_STARTED and tThisFlip >= 95.0-frameTolerance:
            # keep track of start time/frame for later
            valence_arousal_space_2.frameNStart = frameN  # exact frame index
            valence_arousal_space_2.tStart = t  # local t and not account for scr refresh
            valence_arousal_space_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(valence_arousal_space_2, 'tStartRefresh')  # time at next scr refresh
            valence_arousal_space_2.setAutoDraw(True)
        if valence_arousal_space_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > valence_arousal_space_2.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                valence_arousal_space_2.tStop = t  # not accounting for scr refresh
                valence_arousal_space_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(valence_arousal_space_2, 'tStopRefresh')  # time at next scr refresh
                valence_arousal_space_2.setAutoDraw(False)
        # start/stop song_two
        if song_two.status == NOT_STARTED and tThisFlip >= 95.0-frameTolerance:
            # keep track of start time/frame for later
            song_two.frameNStart = frameN  # exact frame index
            song_two.tStart = t  # local t and not account for scr refresh
            song_two.tStartRefresh = tThisFlipGlobal  # on global time
            song_two.play(when=win)  # sync with win flip
        if song_two.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > song_two.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                song_two.tStop = t  # not accounting for scr refresh
                song_two.frameNStop = frameN  # exact frame index
                win.timeOnFlip(song_two, 'tStopRefresh')  # time at next scr refresh
                song_two.stop()
        
        # *reticle_2* updates
        if reticle_2.status == NOT_STARTED and tThisFlip >= 95.0-frameTolerance:
            # keep track of start time/frame for later
            reticle_2.frameNStart = frameN  # exact frame index
            reticle_2.tStart = t  # local t and not account for scr refresh
            reticle_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reticle_2, 'tStartRefresh')  # time at next scr refresh
            reticle_2.setAutoDraw(True)
        if reticle_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > reticle_2.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                reticle_2.tStop = t  # not accounting for scr refresh
                reticle_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(reticle_2, 'tStopRefresh')  # time at next scr refresh
                reticle_2.setAutoDraw(False)
        # *mouse_2* updates
        if mouse_2.status == NOT_STARTED and t >= 95.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            mouse_2.status = STARTED
            mouse_2.mouseClock.reset()
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_2.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                mouse_2.tStop = t  # not accounting for scr refresh
                mouse_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse_2, 'tStopRefresh')  # time at next scr refresh
                mouse_2.status = FINISHED
        if mouse_2.status == STARTED:  # only update if started and not finished!
            if mouse_2_first_frame:
                mouse_2.setPos([0, 0])
                mouse_2_first_frame = False
            x, y = mouse_2.getPos()
            reticle_2.pos = [x, y]
            mouse_2.x.append(x)
            mouse_2.y.append(y)
            buttons = mouse_2.getPressed()
            mouse_2.leftButton.append(buttons[0])
            mouse_2.midButton.append(buttons[1])
            mouse_2.rightButton.append(buttons[2])
            mouse_2.time.append(mouse_2.mouseClock.getTime())
        # start/stop open_eyes_two
        if open_eyes_two.status == NOT_STARTED and tThisFlip >= 154.0-frameTolerance:
            # keep track of start time/frame for later
            open_eyes_two.frameNStart = frameN  # exact frame index
            open_eyes_two.tStart = t  # local t and not account for scr refresh
            open_eyes_two.tStartRefresh = tThisFlipGlobal  # on global time
            open_eyes_two.play(when=win)  # sync with win flip
        if open_eyes_two.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > open_eyes_two.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                open_eyes_two.tStop = t  # not accounting for scr refresh
                open_eyes_two.frameNStop = frameN  # exact frame index
                win.timeOnFlip(open_eyes_two, 'tStopRefresh')  # time at next scr refresh
                open_eyes_two.stop()
        
        # *song_two_rating* updates
        if song_two_rating.status == NOT_STARTED and tThisFlip >= 155.0-frameTolerance:
            # keep track of start time/frame for later
            song_two_rating.frameNStart = frameN  # exact frame index
            song_two_rating.tStart = t  # local t and not account for scr refresh
            song_two_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(song_two_rating, 'tStartRefresh')  # time at next scr refresh
            song_two_rating.setAutoDraw(True)
        if song_two_rating.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > song_two_rating.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                song_two_rating.tStop = t  # not accounting for scr refresh
                song_two_rating.frameNStop = frameN  # exact frame index
                win.timeOnFlip(song_two_rating, 'tStopRefresh')  # time at next scr refresh
                song_two_rating.setAutoDraw(False)
        # start/stop white_noise_two
        if white_noise_two.status == NOT_STARTED and tThisFlip >= 175.0-frameTolerance:
            # keep track of start time/frame for later
            white_noise_two.frameNStart = frameN  # exact frame index
            white_noise_two.tStart = t  # local t and not account for scr refresh
            white_noise_two.tStartRefresh = tThisFlipGlobal  # on global time
            white_noise_two.play(when=win)  # sync with win flip
        if white_noise_two.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > white_noise_two.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                white_noise_two.tStop = t  # not accounting for scr refresh
                white_noise_two.frameNStop = frameN  # exact frame index
                win.timeOnFlip(white_noise_two, 'tStopRefresh')  # time at next scr refresh
                white_noise_two.stop()
        
        # *instruction_eo* updates
        if instruction_eo.status == NOT_STARTED and tThisFlip >= 175.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_eo.frameNStart = frameN  # exact frame index
            instruction_eo.tStart = t  # local t and not account for scr refresh
            instruction_eo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_eo, 'tStartRefresh')  # time at next scr refresh
            instruction_eo.setAutoDraw(True)
        if instruction_eo.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_eo.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                instruction_eo.tStop = t  # not accounting for scr refresh
                instruction_eo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruction_eo, 'tStopRefresh')  # time at next scr refresh
                instruction_eo.setAutoDraw(False)
        
        # *eyes_open_2* updates
        if eyes_open_2.status == NOT_STARTED and tThisFlip >= 185.0-frameTolerance:
            # keep track of start time/frame for later
            eyes_open_2.frameNStart = frameN  # exact frame index
            eyes_open_2.tStart = t  # local t and not account for scr refresh
            eyes_open_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eyes_open_2, 'tStartRefresh')  # time at next scr refresh
            eyes_open_2.setAutoDraw(True)
        if eyes_open_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eyes_open_2.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                eyes_open_2.tStop = t  # not accounting for scr refresh
                eyes_open_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eyes_open_2, 'tStopRefresh')  # time at next scr refresh
                eyes_open_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trials_first_partComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trials_first_part"-------
    for thisComponent in trials_first_partComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    phase_1.addData('valence_arousal_space.started', valence_arousal_space.tStartRefresh)
    phase_1.addData('valence_arousal_space.stopped', valence_arousal_space.tStopRefresh)
    phase_1.addData('reticle.started', reticle.tStartRefresh)
    phase_1.addData('reticle.stopped', reticle.tStopRefresh)
    song_one.stop()  # ensure sound has stopped at end of routine
    phase_1.addData('song_one.started', song_one.tStartRefresh)
    phase_1.addData('song_one.stopped', song_one.tStopRefresh)
    # store data for phase_1 (TrialHandler)
    phase_1.addData('mouse.x', mouse.x)
    phase_1.addData('mouse.y', mouse.y)
    phase_1.addData('mouse.leftButton', mouse.leftButton)
    phase_1.addData('mouse.midButton', mouse.midButton)
    phase_1.addData('mouse.rightButton', mouse.rightButton)
    phase_1.addData('mouse.time', mouse.time)
    phase_1.addData('mouse.started', mouse.tStart)
    phase_1.addData('mouse.stopped', mouse.tStop)
    open_eyes.stop()  # ensure sound has stopped at end of routine
    phase_1.addData('open_eyes.started', open_eyes.tStartRefresh)
    phase_1.addData('open_eyes.stopped', open_eyes.tStopRefresh)
    song_one_rating.addDataToExp(thisExp, 'rows')
    song_one_rating.autodraw = False
    white_noise_one.stop()  # ensure sound has stopped at end of routine
    phase_1.addData('white_noise_one.started', white_noise_one.tStartRefresh)
    phase_1.addData('white_noise_one.stopped', white_noise_one.tStopRefresh)
    phase_1.addData('instruction_ec.started', instruction_ec.tStartRefresh)
    phase_1.addData('instruction_ec.stopped', instruction_ec.tStopRefresh)
    phase_1.addData('eyes_closed.started', eyes_closed.tStartRefresh)
    phase_1.addData('eyes_closed.stopped', eyes_closed.tStopRefresh)
    phase_1.addData('valence_arousal_space_2.started', valence_arousal_space_2.tStartRefresh)
    phase_1.addData('valence_arousal_space_2.stopped', valence_arousal_space_2.tStopRefresh)
    song_two.stop()  # ensure sound has stopped at end of routine
    phase_1.addData('song_two.started', song_two.tStartRefresh)
    phase_1.addData('song_two.stopped', song_two.tStopRefresh)
    phase_1.addData('reticle_2.started', reticle_2.tStartRefresh)
    phase_1.addData('reticle_2.stopped', reticle_2.tStopRefresh)
    # store data for phase_1 (TrialHandler)
    phase_1.addData('mouse_2.x', mouse_2.x)
    phase_1.addData('mouse_2.y', mouse_2.y)
    phase_1.addData('mouse_2.leftButton', mouse_2.leftButton)
    phase_1.addData('mouse_2.midButton', mouse_2.midButton)
    phase_1.addData('mouse_2.rightButton', mouse_2.rightButton)
    phase_1.addData('mouse_2.time', mouse_2.time)
    phase_1.addData('mouse_2.started', mouse_2.tStart)
    phase_1.addData('mouse_2.stopped', mouse_2.tStop)
    open_eyes_two.stop()  # ensure sound has stopped at end of routine
    phase_1.addData('open_eyes_two.started', open_eyes_two.tStartRefresh)
    phase_1.addData('open_eyes_two.stopped', open_eyes_two.tStopRefresh)
    song_two_rating.addDataToExp(thisExp, 'rows')
    song_two_rating.autodraw = False
    white_noise_two.stop()  # ensure sound has stopped at end of routine
    phase_1.addData('white_noise_two.started', white_noise_two.tStartRefresh)
    phase_1.addData('white_noise_two.stopped', white_noise_two.tStopRefresh)
    phase_1.addData('instruction_eo.started', instruction_eo.tStartRefresh)
    phase_1.addData('instruction_eo.stopped', instruction_eo.tStopRefresh)
    phase_1.addData('eyes_open_2.started', eyes_open_2.tStartRefresh)
    phase_1.addData('eyes_open_2.stopped', eyes_open_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'phase_1'

# get names of stimulus parameters
if phase_1.trialList in ([], [None], None):
    params = []
else:
    params = phase_1.trialList[0].keys()
# save data for this loop
phase_1.saveAsExcel(filename + '.xlsx', sheetName='phase_1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
phase_1.saveAsText(filename + 'phase_1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "mid_break"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
mid_breakComponents = [break_instruction, resume_experiment]
for thisComponent in mid_breakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
mid_breakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "mid_break"-------
while continueRoutine:
    # get current time
    t = mid_breakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=mid_breakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *break_instruction* updates
    if break_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break_instruction.frameNStart = frameN  # exact frame index
        break_instruction.tStart = t  # local t and not account for scr refresh
        break_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break_instruction, 'tStartRefresh')  # time at next scr refresh
        break_instruction.setAutoDraw(True)
    if break_instruction.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > break_instruction.tStartRefresh + 15.0-frameTolerance:
            # keep track of stop time/frame for later
            break_instruction.tStop = t  # not accounting for scr refresh
            break_instruction.frameNStop = frameN  # exact frame index
            win.timeOnFlip(break_instruction, 'tStopRefresh')  # time at next scr refresh
            break_instruction.setAutoDraw(False)
    
    # *resume_experiment* updates
    if resume_experiment.status == NOT_STARTED and tThisFlip >= 15.0-frameTolerance:
        # keep track of start time/frame for later
        resume_experiment.frameNStart = frameN  # exact frame index
        resume_experiment.tStart = t  # local t and not account for scr refresh
        resume_experiment.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resume_experiment, 'tStartRefresh')  # time at next scr refresh
        resume_experiment.setAutoDraw(True)
    if resume_experiment.status == STARTED:
        # check whether resume_experiment has been pressed
        if resume_experiment.isClicked:
            if not resume_experiment.wasClicked:
                resume_experiment.timesOn.append(resume_experiment.buttonClock.getTime()) # store time of first click
                resume_experiment.timesOff.append(resume_experiment.buttonClock.getTime()) # store time clicked until
            else:
                resume_experiment.timesOff[-1] = resume_experiment.buttonClock.getTime() # update time clicked until
            if not resume_experiment.wasClicked:
                continueRoutine = False  # end routine when resume_experiment is clicked
                None
            resume_experiment.wasClicked = True  # if resume_experiment is still clicked next frame, it is not a new click
        else:
            resume_experiment.wasClicked = False  # if resume_experiment is clicked next frame, it is a new click
    else:
        resume_experiment.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
        resume_experiment.wasClicked = False  # if resume_experiment is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mid_breakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mid_break"-------
for thisComponent in mid_breakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('break_instruction.started', break_instruction.tStartRefresh)
thisExp.addData('break_instruction.stopped', break_instruction.tStopRefresh)
thisExp.addData('resume_experiment.started', resume_experiment.tStartRefresh)
thisExp.addData('resume_experiment.stopped', resume_experiment.tStopRefresh)
thisExp.addData('resume_experiment.numClicks', resume_experiment.numClicks)
if resume_experiment.numClicks:
   thisExp.addData('resume_experiment.timesOn', resume_experiment.timesOn)
   thisExp.addData('resume_experiment.timesOff', resume_experiment.timesOff)
else:
   thisExp.addData('resume_experiment.timesOn', "")
   thisExp.addData('resume_experiment.timesOff', "")
# the Routine "mid_break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "white_noise_break"-------
continueRoutine = True
routineTimer.add(20.000000)
# update component parameters for each repeat
after_break_white_noise.setSound('res\\1 min wn.wav', secs=20.0, hamming=True)
after_break_white_noise.setVolume(1.0, log=False)
# keep track of which components have finished
white_noise_breakComponents = [after_break_white_noise, after_break_instruction, first_eyes_instruction_2]
for thisComponent in white_noise_breakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
white_noise_breakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "white_noise_break"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = white_noise_breakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=white_noise_breakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop after_break_white_noise
    if after_break_white_noise.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        after_break_white_noise.frameNStart = frameN  # exact frame index
        after_break_white_noise.tStart = t  # local t and not account for scr refresh
        after_break_white_noise.tStartRefresh = tThisFlipGlobal  # on global time
        after_break_white_noise.play(when=win)  # sync with win flip
    if after_break_white_noise.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > after_break_white_noise.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            after_break_white_noise.tStop = t  # not accounting for scr refresh
            after_break_white_noise.frameNStop = frameN  # exact frame index
            win.timeOnFlip(after_break_white_noise, 'tStopRefresh')  # time at next scr refresh
            after_break_white_noise.stop()
    
    # *after_break_instruction* updates
    if after_break_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        after_break_instruction.frameNStart = frameN  # exact frame index
        after_break_instruction.tStart = t  # local t and not account for scr refresh
        after_break_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(after_break_instruction, 'tStartRefresh')  # time at next scr refresh
        after_break_instruction.setAutoDraw(True)
    if after_break_instruction.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > after_break_instruction.tStartRefresh + 15.0-frameTolerance:
            # keep track of stop time/frame for later
            after_break_instruction.tStop = t  # not accounting for scr refresh
            after_break_instruction.frameNStop = frameN  # exact frame index
            win.timeOnFlip(after_break_instruction, 'tStopRefresh')  # time at next scr refresh
            after_break_instruction.setAutoDraw(False)
    
    # *first_eyes_instruction_2* updates
    if first_eyes_instruction_2.status == NOT_STARTED and tThisFlip >= 15.0-frameTolerance:
        # keep track of start time/frame for later
        first_eyes_instruction_2.frameNStart = frameN  # exact frame index
        first_eyes_instruction_2.tStart = t  # local t and not account for scr refresh
        first_eyes_instruction_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(first_eyes_instruction_2, 'tStartRefresh')  # time at next scr refresh
        first_eyes_instruction_2.setAutoDraw(True)
    if first_eyes_instruction_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > first_eyes_instruction_2.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            first_eyes_instruction_2.tStop = t  # not accounting for scr refresh
            first_eyes_instruction_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(first_eyes_instruction_2, 'tStopRefresh')  # time at next scr refresh
            first_eyes_instruction_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in white_noise_breakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "white_noise_break"-------
for thisComponent in white_noise_breakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
after_break_white_noise.stop()  # ensure sound has stopped at end of routine
thisExp.addData('after_break_white_noise.started', after_break_white_noise.tStartRefresh)
thisExp.addData('after_break_white_noise.stopped', after_break_white_noise.tStopRefresh)
thisExp.addData('after_break_instruction.started', after_break_instruction.tStartRefresh)
thisExp.addData('after_break_instruction.stopped', after_break_instruction.tStopRefresh)
thisExp.addData('first_eyes_instruction_2.started', first_eyes_instruction_2.tStartRefresh)
thisExp.addData('first_eyes_instruction_2.stopped', first_eyes_instruction_2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
phase_2 = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='phase_2')
thisExp.addLoop(phase_2)  # add the loop to the experiment
thisPhase_2 = phase_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPhase_2.rgb)
if thisPhase_2 != None:
    for paramName in thisPhase_2:
        exec('{} = thisPhase_2[paramName]'.format(paramName))

# Setup song loader and a randomized playlist
playlist_p2 = song_loader.generate_shuffle_playlist('phase_2')
print(playlist_p2)

# keep track of the trial counter for loading song conditions
trial_counter = 0

# init mouse position
mouse_3_first_frame = True
mouse_4_first_frame = True

for thisPhase_2 in phase_2:
    currentLoop = phase_2
    # abbreviate parameter names if possible (e.g. rgb = thisPhase_2.rgb)
    if thisPhase_2 != None:
        for paramName in thisPhase_2:
            exec('{} = thisPhase_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trials_second_part"-------
    continueRoutine = True
    routineTimer.add(190.000000)
    # update component parameters for each repeat

    # Set the sound sources for this loop
    sound_source_one = playlist_p2[trial_counter][0]
    sound_source_two = playlist_p2[trial_counter][1]
    song_one_2.setSound(sound_source_one, secs=60.0, hamming=True)
    song_one_2.setVolume(1.0, log=False)
    # setup some python lists for storing info about the mouse_3
    mouse_3.x = []
    mouse_3.y = []
    mouse_3.leftButton = []
    mouse_3.midButton = []
    mouse_3.rightButton = []
    mouse_3.time = []
    gotValidClick = False  # until a click is received
    open_eyes_2.setSound('A', secs=1.0, hamming=True)
    open_eyes_2.setVolume(0.5, log=False)
    white_noise_one_2.setSound('res\\1 min wn.wav', secs=15.0, hamming=True)
    white_noise_one_2.setVolume(0.7, log=False)
    song_two_2.setSound(sound_source_two, secs=60.0, hamming=True)
    song_two_2.setVolume(1.0, log=False)

    # increase condition counter for next loop
    trial_counter += 1

    # setup some python lists for storing info about the mouse_4
    mouse_4.x = []
    mouse_4.y = []
    mouse_4.leftButton = []
    mouse_4.midButton = []
    mouse_4.rightButton = []
    mouse_4.time = []
    gotValidClick = False  # until a click is received
    open_eyes_two_2.setSound('A', secs=1.0, hamming=True)
    open_eyes_two_2.setVolume(0.5, log=False)
    white_noise_two_2.setSound('res\\1 min wn.wav', secs=15.0, hamming=True)
    white_noise_two_2.setVolume(0.7, log=False)
    # keep track of which components have finished
    trials_second_partComponents = [valence_arousal_space_3, reticle_3, song_one_2, mouse_3, open_eyes_2, song_one_rating_2, white_noise_one_2, instruction_ec_2, eyes_closed_2, valence_arousal_space_4, song_two_2, reticle_4, mouse_4, open_eyes_two_2, song_two_rating_2, white_noise_two_2, instruction_eo_2, eyes_open]
    for thisComponent in trials_second_partComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trials_second_partClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trials_second_part"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trials_second_partClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trials_second_partClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *valence_arousal_space_3* updates
        if valence_arousal_space_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            valence_arousal_space_3.frameNStart = frameN  # exact frame index
            valence_arousal_space_3.tStart = t  # local t and not account for scr refresh
            valence_arousal_space_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(valence_arousal_space_3, 'tStartRefresh')  # time at next scr refresh
            valence_arousal_space_3.setAutoDraw(True)
        if valence_arousal_space_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > valence_arousal_space_3.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                valence_arousal_space_3.tStop = t  # not accounting for scr refresh
                valence_arousal_space_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(valence_arousal_space_3, 'tStopRefresh')  # time at next scr refresh
                valence_arousal_space_3.setAutoDraw(False)
        
        # *reticle_3* updates
        if reticle_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reticle_3.frameNStart = frameN  # exact frame index
            reticle_3.tStart = t  # local t and not account for scr refresh
            reticle_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reticle_3, 'tStartRefresh')  # time at next scr refresh
            reticle_3.setAutoDraw(True)
        if reticle_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > reticle_3.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                reticle_3.tStop = t  # not accounting for scr refresh
                reticle_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(reticle_3, 'tStopRefresh')  # time at next scr refresh
                reticle_3.setAutoDraw(False)
        # start/stop song_one_2
        if song_one_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            song_one_2.frameNStart = frameN  # exact frame index
            song_one_2.tStart = t  # local t and not account for scr refresh
            song_one_2.tStartRefresh = tThisFlipGlobal  # on global time
            song_one_2.play(when=win)  # sync with win flip
        if song_one_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > song_one_2.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                song_one_2.tStop = t  # not accounting for scr refresh
                song_one_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(song_one_2, 'tStopRefresh')  # time at next scr refresh
                song_one_2.stop()
        # *mouse_3* updates
        if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            mouse_3.status = STARTED
            mouse_3.mouseClock.reset()
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_3.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                mouse_3.tStop = t  # not accounting for scr refresh
                mouse_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse_3, 'tStopRefresh')  # time at next scr refresh
                mouse_3.status = FINISHED
        if mouse_3.status == STARTED:  # only update if started and not finished!
            if mouse_3_first_frame:
                mouse_3.setPos([0, 0])
                mouse_3_first_frame = False
            x, y = mouse_3.getPos()
            reticle_3.pos = [x, y]
            mouse_3.x.append(x)
            mouse_3.y.append(y)
            buttons = mouse_3.getPressed()
            mouse_3.leftButton.append(buttons[0])
            mouse_3.midButton.append(buttons[1])
            mouse_3.rightButton.append(buttons[2])
            mouse_3.time.append(mouse_3.mouseClock.getTime())
        # start/stop open_eyes_2
        if open_eyes_2.status == NOT_STARTED and tThisFlip >= 59.0-frameTolerance:
            # keep track of start time/frame for later
            open_eyes_2.frameNStart = frameN  # exact frame index
            open_eyes_2.tStart = t  # local t and not account for scr refresh
            open_eyes_2.tStartRefresh = tThisFlipGlobal  # on global time
            open_eyes_2.play(when=win)  # sync with win flip
        if open_eyes_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > open_eyes_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                open_eyes_2.tStop = t  # not accounting for scr refresh
                open_eyes_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(open_eyes_2, 'tStopRefresh')  # time at next scr refresh
                open_eyes_2.stop()
        
        # *song_one_rating_2* updates
        if song_one_rating_2.status == NOT_STARTED and tThisFlip >= 60.0-frameTolerance:
            # keep track of start time/frame for later
            song_one_rating_2.frameNStart = frameN  # exact frame index
            song_one_rating_2.tStart = t  # local t and not account for scr refresh
            song_one_rating_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(song_one_rating_2, 'tStartRefresh')  # time at next scr refresh
            song_one_rating_2.setAutoDraw(True)
        if song_one_rating_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > song_one_rating_2.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                song_one_rating_2.tStop = t  # not accounting for scr refresh
                song_one_rating_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(song_one_rating_2, 'tStopRefresh')  # time at next scr refresh
                song_one_rating_2.setAutoDraw(False)
        # start/stop white_noise_one_2
        if white_noise_one_2.status == NOT_STARTED and tThisFlip >= 80.0-frameTolerance:
            # keep track of start time/frame for later
            white_noise_one_2.frameNStart = frameN  # exact frame index
            white_noise_one_2.tStart = t  # local t and not account for scr refresh
            white_noise_one_2.tStartRefresh = tThisFlipGlobal  # on global time
            white_noise_one_2.play(when=win)  # sync with win flip
        if white_noise_one_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > white_noise_one_2.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                white_noise_one_2.tStop = t  # not accounting for scr refresh
                white_noise_one_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(white_noise_one_2, 'tStopRefresh')  # time at next scr refresh
                white_noise_one_2.stop()
        
        # *instruction_ec_2* updates
        if instruction_ec_2.status == NOT_STARTED and tThisFlip >= 80.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_ec_2.frameNStart = frameN  # exact frame index
            instruction_ec_2.tStart = t  # local t and not account for scr refresh
            instruction_ec_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_ec_2, 'tStartRefresh')  # time at next scr refresh
            instruction_ec_2.setAutoDraw(True)
        if instruction_ec_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_ec_2.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                instruction_ec_2.tStop = t  # not accounting for scr refresh
                instruction_ec_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruction_ec_2, 'tStopRefresh')  # time at next scr refresh
                instruction_ec_2.setAutoDraw(False)
        
        # *eyes_closed_2* updates
        if eyes_closed_2.status == NOT_STARTED and tThisFlip >= 90.0-frameTolerance:
            # keep track of start time/frame for later
            eyes_closed_2.frameNStart = frameN  # exact frame index
            eyes_closed_2.tStart = t  # local t and not account for scr refresh
            eyes_closed_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eyes_closed_2, 'tStartRefresh')  # time at next scr refresh
            eyes_closed_2.setAutoDraw(True)
        if eyes_closed_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eyes_closed_2.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                eyes_closed_2.tStop = t  # not accounting for scr refresh
                eyes_closed_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eyes_closed_2, 'tStopRefresh')  # time at next scr refresh
                eyes_closed_2.setAutoDraw(False)
        
        # *valence_arousal_space_4* updates
        if valence_arousal_space_4.status == NOT_STARTED and tThisFlip >= 95.0-frameTolerance:
            # keep track of start time/frame for later
            valence_arousal_space_4.frameNStart = frameN  # exact frame index
            valence_arousal_space_4.tStart = t  # local t and not account for scr refresh
            valence_arousal_space_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(valence_arousal_space_4, 'tStartRefresh')  # time at next scr refresh
            valence_arousal_space_4.setAutoDraw(True)
        if valence_arousal_space_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > valence_arousal_space_4.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                valence_arousal_space_4.tStop = t  # not accounting for scr refresh
                valence_arousal_space_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(valence_arousal_space_4, 'tStopRefresh')  # time at next scr refresh
                valence_arousal_space_4.setAutoDraw(False)
        # start/stop song_two_2
        if song_two_2.status == NOT_STARTED and tThisFlip >= 95.0-frameTolerance:
            # keep track of start time/frame for later
            song_two_2.frameNStart = frameN  # exact frame index
            song_two_2.tStart = t  # local t and not account for scr refresh
            song_two_2.tStartRefresh = tThisFlipGlobal  # on global time
            song_two_2.play(when=win)  # sync with win flip
        if song_two_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > song_two_2.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                song_two_2.tStop = t  # not accounting for scr refresh
                song_two_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(song_two_2, 'tStopRefresh')  # time at next scr refresh
                song_two_2.stop()
        
        # *reticle_4* updates
        if reticle_4.status == NOT_STARTED and tThisFlip >= 95.0-frameTolerance:
            # keep track of start time/frame for later
            reticle_4.frameNStart = frameN  # exact frame index
            reticle_4.tStart = t  # local t and not account for scr refresh
            reticle_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reticle_4, 'tStartRefresh')  # time at next scr refresh
            reticle_4.setAutoDraw(True)
        if reticle_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > reticle_4.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                reticle_4.tStop = t  # not accounting for scr refresh
                reticle_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(reticle_4, 'tStopRefresh')  # time at next scr refresh
                reticle_4.setAutoDraw(False)
        # *mouse_4* updates
        if mouse_4.status == NOT_STARTED and t >= 95.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_4.frameNStart = frameN  # exact frame index
            mouse_4.tStart = t  # local t and not account for scr refresh
            mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
            mouse_4.status = STARTED
            mouse_4.mouseClock.reset()
            prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
        if mouse_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_4.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                mouse_4.tStop = t  # not accounting for scr refresh
                mouse_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse_4, 'tStopRefresh')  # time at next scr refresh
                mouse_4.status = FINISHED
        if mouse_4.status == STARTED:  # only update if started and not finished!
            if mouse_4_first_frame:
                mouse_4.setPos([0, 0])
                mouse_4_first_frame = False
            x, y = mouse_4.getPos()
            reticle_4.pos = [x, y]
            mouse_4.x.append(x)
            mouse_4.y.append(y)
            buttons = mouse_4.getPressed()
            mouse_4.leftButton.append(buttons[0])
            mouse_4.midButton.append(buttons[1])
            mouse_4.rightButton.append(buttons[2])
            mouse_4.time.append(mouse_4.mouseClock.getTime())
        # start/stop open_eyes_two_2
        if open_eyes_two_2.status == NOT_STARTED and tThisFlip >= 154.0-frameTolerance:
            # keep track of start time/frame for later
            open_eyes_two_2.frameNStart = frameN  # exact frame index
            open_eyes_two_2.tStart = t  # local t and not account for scr refresh
            open_eyes_two_2.tStartRefresh = tThisFlipGlobal  # on global time
            open_eyes_two_2.play(when=win)  # sync with win flip
        if open_eyes_two_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > open_eyes_two_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                open_eyes_two_2.tStop = t  # not accounting for scr refresh
                open_eyes_two_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(open_eyes_two_2, 'tStopRefresh')  # time at next scr refresh
                open_eyes_two_2.stop()
        
        # *song_two_rating_2* updates
        if song_two_rating_2.status == NOT_STARTED and tThisFlip >= 155.0-frameTolerance:
            # keep track of start time/frame for later
            song_two_rating_2.frameNStart = frameN  # exact frame index
            song_two_rating_2.tStart = t  # local t and not account for scr refresh
            song_two_rating_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(song_two_rating_2, 'tStartRefresh')  # time at next scr refresh
            song_two_rating_2.setAutoDraw(True)
        if song_two_rating_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > song_two_rating_2.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                song_two_rating_2.tStop = t  # not accounting for scr refresh
                song_two_rating_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(song_two_rating_2, 'tStopRefresh')  # time at next scr refresh
                song_two_rating_2.setAutoDraw(False)
        # start/stop white_noise_two_2
        if white_noise_two_2.status == NOT_STARTED and tThisFlip >= 175.0-frameTolerance:
            # keep track of start time/frame for later
            white_noise_two_2.frameNStart = frameN  # exact frame index
            white_noise_two_2.tStart = t  # local t and not account for scr refresh
            white_noise_two_2.tStartRefresh = tThisFlipGlobal  # on global time
            white_noise_two_2.play(when=win)  # sync with win flip
        if white_noise_two_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > white_noise_two_2.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                white_noise_two_2.tStop = t  # not accounting for scr refresh
                white_noise_two_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(white_noise_two_2, 'tStopRefresh')  # time at next scr refresh
                white_noise_two_2.stop()
        
        # *instruction_eo_2* updates
        if instruction_eo_2.status == NOT_STARTED and tThisFlip >= 175.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_eo_2.frameNStart = frameN  # exact frame index
            instruction_eo_2.tStart = t  # local t and not account for scr refresh
            instruction_eo_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_eo_2, 'tStartRefresh')  # time at next scr refresh
            instruction_eo_2.setAutoDraw(True)
        if instruction_eo_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_eo_2.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                instruction_eo_2.tStop = t  # not accounting for scr refresh
                instruction_eo_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruction_eo_2, 'tStopRefresh')  # time at next scr refresh
                instruction_eo_2.setAutoDraw(False)
        
        # *eyes_open* updates
        if eyes_open.status == NOT_STARTED and tThisFlip >= 185.0-frameTolerance:
            # keep track of start time/frame for later
            eyes_open.frameNStart = frameN  # exact frame index
            eyes_open.tStart = t  # local t and not account for scr refresh
            eyes_open.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eyes_open, 'tStartRefresh')  # time at next scr refresh
            eyes_open.setAutoDraw(True)
        if eyes_open.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eyes_open.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                eyes_open.tStop = t  # not accounting for scr refresh
                eyes_open.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eyes_open, 'tStopRefresh')  # time at next scr refresh
                eyes_open.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trials_second_partComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trials_second_part"-------
    for thisComponent in trials_second_partComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    phase_2.addData('valence_arousal_space_3.started', valence_arousal_space_3.tStartRefresh)
    phase_2.addData('valence_arousal_space_3.stopped', valence_arousal_space_3.tStopRefresh)
    phase_2.addData('reticle_3.started', reticle_3.tStartRefresh)
    phase_2.addData('reticle_3.stopped', reticle_3.tStopRefresh)
    song_one_2.stop()  # ensure sound has stopped at end of routine
    phase_2.addData('song_one_2.started', song_one_2.tStartRefresh)
    phase_2.addData('song_one_2.stopped', song_one_2.tStopRefresh)
    # store data for phase_2 (TrialHandler)
    phase_2.addData('mouse_3.x', mouse_3.x)
    phase_2.addData('mouse_3.y', mouse_3.y)
    phase_2.addData('mouse_3.leftButton', mouse_3.leftButton)
    phase_2.addData('mouse_3.midButton', mouse_3.midButton)
    phase_2.addData('mouse_3.rightButton', mouse_3.rightButton)
    phase_2.addData('mouse_3.time', mouse_3.time)
    phase_2.addData('mouse_3.started', mouse_3.tStart)
    phase_2.addData('mouse_3.stopped', mouse_3.tStop)
    open_eyes_2.stop()  # ensure sound has stopped at end of routine
    phase_2.addData('open_eyes_2.started', open_eyes_2.tStartRefresh)
    phase_2.addData('open_eyes_2.stopped', open_eyes_2.tStopRefresh)
    song_one_rating_2.addDataToExp(thisExp, 'rows')
    song_one_rating_2.autodraw = False
    white_noise_one_2.stop()  # ensure sound has stopped at end of routine
    phase_2.addData('white_noise_one_2.started', white_noise_one_2.tStartRefresh)
    phase_2.addData('white_noise_one_2.stopped', white_noise_one_2.tStopRefresh)
    phase_2.addData('instruction_ec_2.started', instruction_ec_2.tStartRefresh)
    phase_2.addData('instruction_ec_2.stopped', instruction_ec_2.tStopRefresh)
    phase_2.addData('eyes_closed_2.started', eyes_closed_2.tStartRefresh)
    phase_2.addData('eyes_closed_2.stopped', eyes_closed_2.tStopRefresh)
    phase_2.addData('valence_arousal_space_4.started', valence_arousal_space_4.tStartRefresh)
    phase_2.addData('valence_arousal_space_4.stopped', valence_arousal_space_4.tStopRefresh)
    song_two_2.stop()  # ensure sound has stopped at end of routine
    phase_2.addData('song_two_2.started', song_two_2.tStartRefresh)
    phase_2.addData('song_two_2.stopped', song_two_2.tStopRefresh)
    phase_2.addData('reticle_4.started', reticle_4.tStartRefresh)
    phase_2.addData('reticle_4.stopped', reticle_4.tStopRefresh)
    # store data for phase_2 (TrialHandler)
    phase_2.addData('mouse_4.x', mouse_4.x)
    phase_2.addData('mouse_4.y', mouse_4.y)
    phase_2.addData('mouse_4.leftButton', mouse_4.leftButton)
    phase_2.addData('mouse_4.midButton', mouse_4.midButton)
    phase_2.addData('mouse_4.rightButton', mouse_4.rightButton)
    phase_2.addData('mouse_4.time', mouse_4.time)
    phase_2.addData('mouse_4.started', mouse_4.tStart)
    phase_2.addData('mouse_4.stopped', mouse_4.tStop)
    open_eyes_two_2.stop()  # ensure sound has stopped at end of routine
    phase_2.addData('open_eyes_two_2.started', open_eyes_two_2.tStartRefresh)
    phase_2.addData('open_eyes_two_2.stopped', open_eyes_two_2.tStopRefresh)
    song_two_rating_2.addDataToExp(thisExp, 'rows')
    song_two_rating_2.autodraw = False
    white_noise_two_2.stop()  # ensure sound has stopped at end of routine
    phase_2.addData('white_noise_two_2.started', white_noise_two_2.tStartRefresh)
    phase_2.addData('white_noise_two_2.stopped', white_noise_two_2.tStopRefresh)
    phase_2.addData('instruction_eo_2.started', instruction_eo_2.tStartRefresh)
    phase_2.addData('instruction_eo_2.stopped', instruction_eo_2.tStopRefresh)
    phase_2.addData('eyes_open.started', eyes_open.tStartRefresh)
    phase_2.addData('eyes_open.stopped', eyes_open.tStopRefresh)
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'phase_2'

# get names of stimulus parameters
if phase_2.trialList in ([], [None], None):
    params = []
else:
    params = phase_2.trialList[0].keys()
# save data for this loop
phase_2.saveAsExcel(filename + '.xlsx', sheetName='phase_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
phase_2.saveAsText(filename + 'phase_2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "exit_rest_state"-------
continueRoutine = True
routineTimer.add(290.000000)
# update component parameters for each repeat
sound_2.setSound('A', secs=1.0, hamming=True)
sound_2.setVolume(1.0, log=False)
# keep track of which components have finished
exit_rest_stateComponents = [resting_state_instructions_2, rest_state_eyes_open_2, rest_state_eyes_open_icon_2, rest_eyes_closed_2, rest_eyes_closed_icon_2, sound_2, text]
for thisComponent in exit_rest_stateComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
exit_rest_stateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "exit_rest_state"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = exit_rest_stateClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=exit_rest_stateClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *resting_state_instructions_2* updates
    if resting_state_instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resting_state_instructions_2.frameNStart = frameN  # exact frame index
        resting_state_instructions_2.tStart = t  # local t and not account for scr refresh
        resting_state_instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resting_state_instructions_2, 'tStartRefresh')  # time at next scr refresh
        resting_state_instructions_2.setAutoDraw(True)
    if resting_state_instructions_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > resting_state_instructions_2.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            resting_state_instructions_2.tStop = t  # not accounting for scr refresh
            resting_state_instructions_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(resting_state_instructions_2, 'tStopRefresh')  # time at next scr refresh
            resting_state_instructions_2.setAutoDraw(False)
    
    # *rest_state_eyes_open_2* updates
    if rest_state_eyes_open_2.status == NOT_STARTED and tThisFlip >= 20.0-frameTolerance:
        # keep track of start time/frame for later
        rest_state_eyes_open_2.frameNStart = frameN  # exact frame index
        rest_state_eyes_open_2.tStart = t  # local t and not account for scr refresh
        rest_state_eyes_open_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_state_eyes_open_2, 'tStartRefresh')  # time at next scr refresh
        rest_state_eyes_open_2.setAutoDraw(True)
    if rest_state_eyes_open_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_state_eyes_open_2.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            rest_state_eyes_open_2.tStop = t  # not accounting for scr refresh
            rest_state_eyes_open_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rest_state_eyes_open_2, 'tStopRefresh')  # time at next scr refresh
            rest_state_eyes_open_2.setAutoDraw(False)
    
    # *rest_state_eyes_open_icon_2* updates
    if rest_state_eyes_open_icon_2.status == NOT_STARTED and tThisFlip >= 25.0-frameTolerance:
        # keep track of start time/frame for later
        rest_state_eyes_open_icon_2.frameNStart = frameN  # exact frame index
        rest_state_eyes_open_icon_2.tStart = t  # local t and not account for scr refresh
        rest_state_eyes_open_icon_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_state_eyes_open_icon_2, 'tStartRefresh')  # time at next scr refresh
        rest_state_eyes_open_icon_2.setAutoDraw(True)
    if rest_state_eyes_open_icon_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_state_eyes_open_icon_2.tStartRefresh + 120.0-frameTolerance:
            # keep track of stop time/frame for later
            rest_state_eyes_open_icon_2.tStop = t  # not accounting for scr refresh
            rest_state_eyes_open_icon_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rest_state_eyes_open_icon_2, 'tStopRefresh')  # time at next scr refresh
            rest_state_eyes_open_icon_2.setAutoDraw(False)
    
    # *rest_eyes_closed_2* updates
    if rest_eyes_closed_2.status == NOT_STARTED and tThisFlip >= 145.0-frameTolerance:
        # keep track of start time/frame for later
        rest_eyes_closed_2.frameNStart = frameN  # exact frame index
        rest_eyes_closed_2.tStart = t  # local t and not account for scr refresh
        rest_eyes_closed_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_eyes_closed_2, 'tStartRefresh')  # time at next scr refresh
        rest_eyes_closed_2.setAutoDraw(True)
    if rest_eyes_closed_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_eyes_closed_2.tStartRefresh + 15.0-frameTolerance:
            # keep track of stop time/frame for later
            rest_eyes_closed_2.tStop = t  # not accounting for scr refresh
            rest_eyes_closed_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rest_eyes_closed_2, 'tStopRefresh')  # time at next scr refresh
            rest_eyes_closed_2.setAutoDraw(False)
    
    # *rest_eyes_closed_icon_2* updates
    if rest_eyes_closed_icon_2.status == NOT_STARTED and tThisFlip >= 160.0-frameTolerance:
        # keep track of start time/frame for later
        rest_eyes_closed_icon_2.frameNStart = frameN  # exact frame index
        rest_eyes_closed_icon_2.tStart = t  # local t and not account for scr refresh
        rest_eyes_closed_icon_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_eyes_closed_icon_2, 'tStartRefresh')  # time at next scr refresh
        rest_eyes_closed_icon_2.setAutoDraw(True)
    if rest_eyes_closed_icon_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_eyes_closed_icon_2.tStartRefresh + 120.0-frameTolerance:
            # keep track of stop time/frame for later
            rest_eyes_closed_icon_2.tStop = t  # not accounting for scr refresh
            rest_eyes_closed_icon_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rest_eyes_closed_icon_2, 'tStopRefresh')  # time at next scr refresh
            rest_eyes_closed_icon_2.setAutoDraw(False)
    # start/stop sound_2
    if sound_2.status == NOT_STARTED and tThisFlip >= 279.0-frameTolerance:
        # keep track of start time/frame for later
        sound_2.frameNStart = frameN  # exact frame index
        sound_2.tStart = t  # local t and not account for scr refresh
        sound_2.tStartRefresh = tThisFlipGlobal  # on global time
        sound_2.play(when=win)  # sync with win flip
    if sound_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            sound_2.tStop = t  # not accounting for scr refresh
            sound_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
            sound_2.stop()
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 280.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exit_rest_stateComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "exit_rest_state"-------
for thisComponent in exit_rest_stateComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('resting_state_instructions_2.started', resting_state_instructions_2.tStartRefresh)
thisExp.addData('resting_state_instructions_2.stopped', resting_state_instructions_2.tStopRefresh)
thisExp.addData('rest_state_eyes_open_2.started', rest_state_eyes_open_2.tStartRefresh)
thisExp.addData('rest_state_eyes_open_2.stopped', rest_state_eyes_open_2.tStopRefresh)
thisExp.addData('rest_state_eyes_open_icon_2.started', rest_state_eyes_open_icon_2.tStartRefresh)
thisExp.addData('rest_state_eyes_open_icon_2.stopped', rest_state_eyes_open_icon_2.tStopRefresh)
thisExp.addData('rest_eyes_closed_2.started', rest_eyes_closed_2.tStartRefresh)
thisExp.addData('rest_eyes_closed_2.stopped', rest_eyes_closed_2.tStopRefresh)
thisExp.addData('rest_eyes_closed_icon_2.started', rest_eyes_closed_icon_2.tStartRefresh)
thisExp.addData('rest_eyes_closed_icon_2.stopped', rest_eyes_closed_icon_2.tStopRefresh)
sound_2.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_2.started', sound_2.tStartRefresh)
thisExp.addData('sound_2.stopped', sound_2.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
