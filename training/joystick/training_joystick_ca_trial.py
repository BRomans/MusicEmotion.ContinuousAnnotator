﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on June 03, 2021, at 15:52
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



# Ensure that relative paths start from the same directory as this script
from utils.joystick_utilities import clamp_stick, get_clamped_position

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'training_joystick_ca_trial'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='C:\\Users\\miche\\EIT\\INTERNSHIP_MYBRAIN\\experimental_phase\\experiment_continuous_annotation\\training\\joystick\\training_joystick_ca_trial.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joystick import virtualJoystick as virtualjoysticklib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joystick import virtualJoystick as virtualjoysticklib

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

# Initialize components for Routine "example_trial_joystick"
example_trial_joystickClock = core.Clock()
instructions_1 = visual.TextStim(win=win, name='instructions_1',
    text="Now that you know how to move your reticle, let's try to simulate a trial.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions_2 = visual.TextStim(win=win, name='instructions_2',
    text='Before each trial, you will hear this noise. It\'s called White Noise and the purpose is to "wash" away your current emotional state.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructions_3 = visual.TextStim(win=win, name='instructions_3',
    text="Before listening to each song, an instruction will tell you if you need to keep your eyes OPEN or CLOSED. Let's try both!",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
eyes_open = visual.ImageStim(
    win=win,
    name='eyes_open', 
    image='res\\\\img\\\\eye_open.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
instructions_4 = visual.TextStim(win=win, name='instructions_4',
    text='When you see the icon, CLOSE your eyes and open them when you hear this sound.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
alarm_eyes_open_1 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='alarm_eyes_open_1')
alarm_eyes_open_1.setVolume(0.5)
eyes_closed = visual.ImageStim(
    win=win,
    name='eyes_closed', 
    image='res\\\\img\\\\eye_closed.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
eyes_open_alarm_2 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='eyes_open_alarm_2')
eyes_open_alarm_2.setVolume(1.0)
instructions_5 = visual.TextStim(win=win, name='instructions_5',
    text='When you are listening to music with eyes OPEN or CLOSED, you are supposed to continuously annotate your emotions by moving the cursor.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
instructions_6 = visual.TextStim(win=win, name='instructions_6',
    text="To annotate your emotions, simply move the cursor in the corresponding area of the Valence-Arousal space. Get ready, it's your turn now :)\n\nColors have been removed to avoid distractions.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
eyes_open_2 = visual.ImageStim(
    win=win,
    name='eyes_open_2', 
    image='res\\\\img\\\\eye_open.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
white_noise = sound.Sound('res\\1 min wn.wav', secs=-1.0, stereo=True, hamming=True,
    name='white_noise')
white_noise.setVolume(0.5)
white_noise_2 = sound.Sound('res\\1 min wn.wav', secs=-1.0, stereo=True, hamming=True,
    name='white_noise_2')
white_noise_2.setVolume(0.5)
song_trial = sound.Sound('res\\playlist\\Daft Punk - Within (Official Audio).ogg', secs=-1.0, stereo=True, hamming=True,
    name='song_trial')
song_trial.setVolume(1.0)
valence_arousal_space = visual.ImageStim(
    win=win,
    name='valence_arousal_space', 
    image='res\\\\img\\\\valence_arousal_space_basic.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
x, y = [None, None]
joystick = joysticklib.XboxController(0) # Create an object to use as a name space
joystick.device = None
joystick.device_number = 0
joystick.joystickClock = core.Clock()
joystick.xFactor = 1
joystick.yFactor = 1

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        joystick.device = joystickCache[0]
        if win.units == 'height':
            joystick.xFactor = 0.5 * win.size[0]/win.size[1]
            joystick.yFactor = 0.5
    else:
        joystick.device = virtualjoysticklib.VirtualJoystick(0)
        logging.warning("joystick_{}: Using keyboard+mouse emulation 'ctrl' + 'Alt' + digit.".format(joystick.device_number))
except Exception:
    pass
    
if not joystick.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

joystick.status = None
joystick.clock = core.Clock()
joystick.numButtons = joystick.device.getNumButtons()
joystick.getNumButtons = joystick.device.getNumButtons
joystick.getAllButtons = joystick.device.getAllButtons
joystick.getX = lambda: joystick.xFactor * joystick.device.getX()
joystick.getY = lambda: joystick.yFactor * joystick.device.getY()

reticle = visual.ImageStim(
    win=win,
    name='reticle', units='norm', 
    image='res\\\\img\\\\reticle.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
instructions_7 = visual.TextStim(win=win, name='instructions_7',
    text='After each song you have 15 seconds to rate how much you liked/disliked it and how familiar it was to you. Use your mouse to select a value on the scale.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);
win.allowStencil = True
song_rating = visual.Form(win=win, name='song_rating',
    items='res\\\\forms\\\\rating_form.csv',
    textHeight=0.03,
    randomize=False,
    size=(1, 0.7),
    pos=(0, 0),
    style='dark',
    itemPadding=0.05,)
white_noise_3 = sound.Sound('res\\1 min wn.wav', secs=-1.0, stereo=True, hamming=True,
    name='white_noise_3')
white_noise_3.setVolume(0.5)
eyes_closed_2 = visual.ImageStim(
    win=win,
    name='eyes_closed_2', 
    image='res\\\\img\\\\eye_closed.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-20.0)
instructions_8 = visual.TextStim(win=win, name='instructions_8',
    text="Let's give it one more try, with eyes CLOSED this time.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-21.0);
song_trial_2 = sound.Sound('res\\playlist\\Metallica-Fade To Black www.my-free-mp3.net  (1).ogg', secs=-1.0, stereo=True, hamming=True,
    name='song_trial_2')
song_trial_2.setVolume(1.0)
va_2 = visual.ImageStim(
    win=win,
    name='va_2', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-23.0)
x, y = [None, None]
joystick_2 = joysticklib.XboxController(0) # Create an object to use as a name space
joystick_2.device = None
joystick_2.device_number = 0
joystick_2.joystickClock = core.Clock()
joystick_2.xFactor = 1
joystick_2.yFactor = 1

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        joystick_2.device = joystickCache[0]
        if win.units == 'height':
            joystick_2.xFactor = 0.5 * win.size[0]/win.size[1]
            joystick_2.yFactor = 0.5
    else:
        joystick_2.device = virtualjoysticklib.VirtualJoystick(0)
        logging.warning("joystick_{}: Using keyboard+mouse emulation 'ctrl' + 'Alt' + digit.".format(joystick_2.device_number))
except Exception:
    pass
    
if not joystick_2.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

joystick_2.status = None
joystick_2.clock = core.Clock()
joystick_2.numButtons = joystick_2.device.getNumButtons()
joystick_2.getNumButtons = joystick_2.device.getNumButtons
joystick_2.getAllButtons = joystick_2.device.getAllButtons
joystick_2.getX = lambda: joystick_2.xFactor * joystick_2.device.getX()
joystick_2.getY = lambda: joystick_2.yFactor * joystick_2.device.getY()

reticle_2 = visual.ImageStim(
    win=win,
    name='reticle_2', 
    image='res\\\\img\\\\reticle.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-25.0)
eyes_open_alarm = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='eyes_open_alarm')
eyes_open_alarm.setVolume(0.5)
win.allowStencil = True
song_rating_2 = visual.Form(win=win, name='song_rating_2',
    items='res\\\\forms\\\\rating_form.csv',
    textHeight=0.03,
    randomize=False,
    size=(1, 0.7),
    pos=(0, 0),
    style='dark',
    itemPadding=0.05,)
instructions_9 = visual.TextStim(win=win, name='instructions_9',
    text='In every trial, you will be instructed to listen to one song with eyes OPEN (and annotate your emotions) and one song with eyes CLOSED.  After each song you will give your rating, receive new instructions and listen to White Noise to reset your emotional state before the next one. \nWhen you are ready to start the real experiment, press Q. \nFor any doubts, ask the researcher, he is a cool dude. Have fun :)',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-28.0);
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "example_trial_joystick"-------
continueRoutine = True
# update component parameters for each repeat
alarm_eyes_open_1.setSound('A', secs=1.0, hamming=True)
alarm_eyes_open_1.setVolume(0.5, log=False)
eyes_open_alarm_2.setSound('A', secs=1.0, hamming=True)
eyes_open_alarm_2.setVolume(1.0, log=False)
white_noise.setSound('res\\1 min wn.wav', secs=60.0, hamming=True)
white_noise.setVolume(0.5, log=False)
white_noise_2.setSound('res\\1 min wn.wav', secs=15.0, hamming=True)
white_noise_2.setVolume(0.5, log=False)
song_trial.setSound('res\\playlist\\Daft Punk - Within (Official Audio).ogg', secs=45.0, hamming=True)
song_trial.setVolume(1.0, log=False)
joystick.oldButtonState = joystick.device.getAllButtons()[:]
joystick.activeButtons=[i for i in range(joystick.numButtons)]
# setup some python lists for storing info about the joystick
joystick.x = []
joystick.y = []
joystick._x = []
joystick._y = []
joystick.buttonLogs = [[] for i in range(joystick.numButtons)]
joystick.time = []
gotValidClick = False  # until a click is received
white_noise_3.setSound('res\\1 min wn.wav', secs=15.0, hamming=True)
white_noise_3.setVolume(0.5, log=False)
song_trial_2.setSound('res\\playlist\\Metallica-Fade To Black www.my-free-mp3.net  (1).ogg', secs=45.0, hamming=True)
song_trial_2.setVolume(1.0, log=False)
joystick_2.oldButtonState = joystick_2.device.getAllButtons()[:]
joystick_2.activeButtons=[i for i in range(joystick_2.numButtons)]
# setup some python lists for storing info about the joystick_2
joystick_2.x = []
joystick_2.y = []
joystick_2._x = []
joystick_2._y = []
joystick_2.buttonLogs = [[] for i in range(joystick_2.numButtons)]
joystick_2.time = []
gotValidClick = False  # until a click is received
eyes_open_alarm.setSound('A', secs=1.0, hamming=True)
eyes_open_alarm.setVolume(0.5, log=False)
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
example_trial_joystickComponents = [instructions_1, instructions_2, instructions_3, eyes_open, instructions_4, alarm_eyes_open_1, eyes_closed, eyes_open_alarm_2, instructions_5, instructions_6, eyes_open_2, white_noise, white_noise_2, song_trial, valence_arousal_space, joystick, reticle, instructions_7, song_rating, white_noise_3, eyes_closed_2, instructions_8, song_trial_2, va_2, joystick_2, reticle_2, eyes_open_alarm, song_rating_2, instructions_9, key_resp]
for thisComponent in example_trial_joystickComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
example_trial_joystickClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "example_trial_joystick"-------
while continueRoutine:
    # get current time
    t = example_trial_joystickClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=example_trial_joystickClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_1* updates
    if instructions_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_1.frameNStart = frameN  # exact frame index
        instructions_1.tStart = t  # local t and not account for scr refresh
        instructions_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_1, 'tStartRefresh')  # time at next scr refresh
        instructions_1.setAutoDraw(True)
    if instructions_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_1.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            instructions_1.tStop = t  # not accounting for scr refresh
            instructions_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_1, 'tStopRefresh')  # time at next scr refresh
            instructions_1.setAutoDraw(False)
    
    # *instructions_2* updates
    if instructions_2.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_2.frameNStart = frameN  # exact frame index
        instructions_2.tStart = t  # local t and not account for scr refresh
        instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_2, 'tStartRefresh')  # time at next scr refresh
        instructions_2.setAutoDraw(True)
    if instructions_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_2.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            instructions_2.tStop = t  # not accounting for scr refresh
            instructions_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_2, 'tStopRefresh')  # time at next scr refresh
            instructions_2.setAutoDraw(False)
    
    # *instructions_3* updates
    if instructions_3.status == NOT_STARTED and tThisFlip >= 20.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_3.frameNStart = frameN  # exact frame index
        instructions_3.tStart = t  # local t and not account for scr refresh
        instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_3, 'tStartRefresh')  # time at next scr refresh
        instructions_3.setAutoDraw(True)
    if instructions_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_3.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            instructions_3.tStop = t  # not accounting for scr refresh
            instructions_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_3, 'tStopRefresh')  # time at next scr refresh
            instructions_3.setAutoDraw(False)
    
    # *eyes_open* updates
    if eyes_open.status == NOT_STARTED and tThisFlip >= 30.0-frameTolerance:
        # keep track of start time/frame for later
        eyes_open.frameNStart = frameN  # exact frame index
        eyes_open.tStart = t  # local t and not account for scr refresh
        eyes_open.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eyes_open, 'tStartRefresh')  # time at next scr refresh
        eyes_open.setAutoDraw(True)
    if eyes_open.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > eyes_open.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            eyes_open.tStop = t  # not accounting for scr refresh
            eyes_open.frameNStop = frameN  # exact frame index
            win.timeOnFlip(eyes_open, 'tStopRefresh')  # time at next scr refresh
            eyes_open.setAutoDraw(False)
    
    # *instructions_4* updates
    if instructions_4.status == NOT_STARTED and tThisFlip >= 40.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_4.frameNStart = frameN  # exact frame index
        instructions_4.tStart = t  # local t and not account for scr refresh
        instructions_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_4, 'tStartRefresh')  # time at next scr refresh
        instructions_4.setAutoDraw(True)
    if instructions_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_4.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            instructions_4.tStop = t  # not accounting for scr refresh
            instructions_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_4, 'tStopRefresh')  # time at next scr refresh
            instructions_4.setAutoDraw(False)
    # start/stop alarm_eyes_open_1
    if alarm_eyes_open_1.status == NOT_STARTED and tThisFlip >= 45.0-frameTolerance:
        # keep track of start time/frame for later
        alarm_eyes_open_1.frameNStart = frameN  # exact frame index
        alarm_eyes_open_1.tStart = t  # local t and not account for scr refresh
        alarm_eyes_open_1.tStartRefresh = tThisFlipGlobal  # on global time
        alarm_eyes_open_1.play(when=win)  # sync with win flip
    if alarm_eyes_open_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > alarm_eyes_open_1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            alarm_eyes_open_1.tStop = t  # not accounting for scr refresh
            alarm_eyes_open_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(alarm_eyes_open_1, 'tStopRefresh')  # time at next scr refresh
            alarm_eyes_open_1.stop()
    
    # *eyes_closed* updates
    if eyes_closed.status == NOT_STARTED and tThisFlip >= 50.0-frameTolerance:
        # keep track of start time/frame for later
        eyes_closed.frameNStart = frameN  # exact frame index
        eyes_closed.tStart = t  # local t and not account for scr refresh
        eyes_closed.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eyes_closed, 'tStartRefresh')  # time at next scr refresh
        eyes_closed.setAutoDraw(True)
    if eyes_closed.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > eyes_closed.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            eyes_closed.tStop = t  # not accounting for scr refresh
            eyes_closed.frameNStop = frameN  # exact frame index
            win.timeOnFlip(eyes_closed, 'tStopRefresh')  # time at next scr refresh
            eyes_closed.setAutoDraw(False)
    # start/stop eyes_open_alarm_2
    if eyes_open_alarm_2.status == NOT_STARTED and tThisFlip >= 60.0-frameTolerance:
        # keep track of start time/frame for later
        eyes_open_alarm_2.frameNStart = frameN  # exact frame index
        eyes_open_alarm_2.tStart = t  # local t and not account for scr refresh
        eyes_open_alarm_2.tStartRefresh = tThisFlipGlobal  # on global time
        eyes_open_alarm_2.play(when=win)  # sync with win flip
    if eyes_open_alarm_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > eyes_open_alarm_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            eyes_open_alarm_2.tStop = t  # not accounting for scr refresh
            eyes_open_alarm_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(eyes_open_alarm_2, 'tStopRefresh')  # time at next scr refresh
            eyes_open_alarm_2.stop()
    
    # *instructions_5* updates
    if instructions_5.status == NOT_STARTED and tThisFlip >= 60.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_5.frameNStart = frameN  # exact frame index
        instructions_5.tStart = t  # local t and not account for scr refresh
        instructions_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_5, 'tStartRefresh')  # time at next scr refresh
        instructions_5.setAutoDraw(True)
    if instructions_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_5.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            instructions_5.tStop = t  # not accounting for scr refresh
            instructions_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_5, 'tStopRefresh')  # time at next scr refresh
            instructions_5.setAutoDraw(False)
    
    # *instructions_6* updates
    if instructions_6.status == NOT_STARTED and tThisFlip >= 70.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_6.frameNStart = frameN  # exact frame index
        instructions_6.tStart = t  # local t and not account for scr refresh
        instructions_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_6, 'tStartRefresh')  # time at next scr refresh
        instructions_6.setAutoDraw(True)
    if instructions_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_6.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            instructions_6.tStop = t  # not accounting for scr refresh
            instructions_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_6, 'tStopRefresh')  # time at next scr refresh
            instructions_6.setAutoDraw(False)
    
    # *eyes_open_2* updates
    if eyes_open_2.status == NOT_STARTED and tThisFlip >= 80.0-frameTolerance:
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
    # start/stop white_noise
    if white_noise.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        white_noise.frameNStart = frameN  # exact frame index
        white_noise.tStart = t  # local t and not account for scr refresh
        white_noise.tStartRefresh = tThisFlipGlobal  # on global time
        white_noise.play(when=win)  # sync with win flip
    if white_noise.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > white_noise.tStartRefresh + 60.0-frameTolerance:
            # keep track of stop time/frame for later
            white_noise.tStop = t  # not accounting for scr refresh
            white_noise.frameNStop = frameN  # exact frame index
            win.timeOnFlip(white_noise, 'tStopRefresh')  # time at next scr refresh
            white_noise.stop()
    # start/stop white_noise_2
    if white_noise_2.status == NOT_STARTED and t >= 70.0-frameTolerance:
        # keep track of start time/frame for later
        white_noise_2.frameNStart = frameN  # exact frame index
        white_noise_2.tStart = t  # local t and not account for scr refresh
        white_noise_2.tStartRefresh = tThisFlipGlobal  # on global time
        white_noise_2.play()  # start the sound (it finishes automatically)
    if white_noise_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > white_noise_2.tStartRefresh + 15.0-frameTolerance:
            # keep track of stop time/frame for later
            white_noise_2.tStop = t  # not accounting for scr refresh
            white_noise_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(white_noise_2, 'tStopRefresh')  # time at next scr refresh
            white_noise_2.stop()
    # start/stop song_trial
    if song_trial.status == NOT_STARTED and t >= 85.0-frameTolerance:
        # keep track of start time/frame for later
        song_trial.frameNStart = frameN  # exact frame index
        song_trial.tStart = t  # local t and not account for scr refresh
        song_trial.tStartRefresh = tThisFlipGlobal  # on global time
        song_trial.play()  # start the sound (it finishes automatically)
    if song_trial.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > song_trial.tStartRefresh + 45.0-frameTolerance:
            # keep track of stop time/frame for later
            song_trial.tStop = t  # not accounting for scr refresh
            song_trial.frameNStop = frameN  # exact frame index
            win.timeOnFlip(song_trial, 'tStopRefresh')  # time at next scr refresh
            song_trial.stop()
    
    # *valence_arousal_space* updates
    if valence_arousal_space.status == NOT_STARTED and tThisFlip >= 85.0-frameTolerance:
        # keep track of start time/frame for later
        valence_arousal_space.frameNStart = frameN  # exact frame index
        valence_arousal_space.tStart = t  # local t and not account for scr refresh
        valence_arousal_space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(valence_arousal_space, 'tStartRefresh')  # time at next scr refresh
        valence_arousal_space.setAutoDraw(True)
    if valence_arousal_space.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > valence_arousal_space.tStartRefresh + 45.0-frameTolerance:
            # keep track of stop time/frame for later
            valence_arousal_space.tStop = t  # not accounting for scr refresh
            valence_arousal_space.frameNStop = frameN  # exact frame index
            win.timeOnFlip(valence_arousal_space, 'tStopRefresh')  # time at next scr refresh
            valence_arousal_space.setAutoDraw(False)
    # *joystick* updates
    if joystick.status == NOT_STARTED and t >= 85.0-frameTolerance:
        # keep track of start time/frame for later
        joystick.frameNStart = frameN  # exact frame index
        joystick.tStart = t  # local t and not account for scr refresh
        joystick.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(joystick, 'tStartRefresh')  # time at next scr refresh
        joystick.status = STARTED
        joystick.joystickClock.reset()
    if joystick.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > joystick.tStartRefresh + 45.0-frameTolerance:
            # keep track of stop time/frame for later
            joystick.tStop = t  # not accounting for scr refresh
            joystick.frameNStop = frameN  # exact frame index
            win.timeOnFlip(joystick, 'tStopRefresh')  # time at next scr refresh
            joystick.status = FINISHED
    if joystick.status == STARTED:  # only update if started and not finished!
        joystick.newButtonState = joystick.getAllButtons()[:]
        joystick.pressedButtons = [i for i in range(joystick.numButtons) if joystick.newButtonState[i] and not joystick.oldButtonState[i]]
        joystick.releasedButtons = [i for i in range(joystick.numButtons) if not joystick.newButtonState[i] and joystick.oldButtonState[i]]
        joystick.newPressedButtons = [i for i in joystick.activeButtons if i in joystick.pressedButtons]
        joystick.buttons = joystick.newPressedButtons
        [logging.data("joystick_{}_button: {}, pos=({:1.4f},{:1.4f})".format(joystick.device_number, i, joystick.getX(), joystick.getY())) for i in joystick.pressedButtons]
        x, y = clamp_stick(joystick.getX(), joystick.getY())
        joystick._x.append(x)
        joystick._y.append(y)
        reticle.pos = get_clamped_position(joystick)
        [joystick.buttonLogs[i].append(int(joystick.newButtonState[i])) for i in joystick.activeButtons]
        joystick.time.append(joystick.joystickClock.getTime())
    
    # *reticle* updates
    if reticle.status == NOT_STARTED and tThisFlip >= 85.0-frameTolerance:
        # keep track of start time/frame for later
        reticle.frameNStart = frameN  # exact frame index
        reticle.tStart = t  # local t and not account for scr refresh
        reticle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(reticle, 'tStartRefresh')  # time at next scr refresh
        reticle.setAutoDraw(True)
    if reticle.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > reticle.tStartRefresh + 45.0-frameTolerance:
            # keep track of stop time/frame for later
            reticle.tStop = t  # not accounting for scr refresh
            reticle.frameNStop = frameN  # exact frame index
            win.timeOnFlip(reticle, 'tStopRefresh')  # time at next scr refresh
            reticle.setAutoDraw(False)
    
    # *instructions_7* updates
    if instructions_7.status == NOT_STARTED and tThisFlip >= 130.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_7.frameNStart = frameN  # exact frame index
        instructions_7.tStart = t  # local t and not account for scr refresh
        instructions_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_7, 'tStartRefresh')  # time at next scr refresh
        instructions_7.setAutoDraw(True)
    if instructions_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_7.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            instructions_7.tStop = t  # not accounting for scr refresh
            instructions_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_7, 'tStopRefresh')  # time at next scr refresh
            instructions_7.setAutoDraw(False)
    
    # *song_rating* updates
    if song_rating.status == NOT_STARTED and tThisFlip >= 140.0-frameTolerance:
        # keep track of start time/frame for later
        song_rating.frameNStart = frameN  # exact frame index
        song_rating.tStart = t  # local t and not account for scr refresh
        song_rating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(song_rating, 'tStartRefresh')  # time at next scr refresh
        song_rating.setAutoDraw(True)
    if song_rating.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > song_rating.tStartRefresh + 30.0-frameTolerance:
            # keep track of stop time/frame for later
            song_rating.tStop = t  # not accounting for scr refresh
            song_rating.frameNStop = frameN  # exact frame index
            win.timeOnFlip(song_rating, 'tStopRefresh')  # time at next scr refresh
            song_rating.setAutoDraw(False)
    # start/stop white_noise_3
    if white_noise_3.status == NOT_STARTED and t >= 170.0-frameTolerance:
        # keep track of start time/frame for later
        white_noise_3.frameNStart = frameN  # exact frame index
        white_noise_3.tStart = t  # local t and not account for scr refresh
        white_noise_3.tStartRefresh = tThisFlipGlobal  # on global time
        white_noise_3.play()  # start the sound (it finishes automatically)
    if white_noise_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > white_noise_3.tStartRefresh + 15.0-frameTolerance:
            # keep track of stop time/frame for later
            white_noise_3.tStop = t  # not accounting for scr refresh
            white_noise_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(white_noise_3, 'tStopRefresh')  # time at next scr refresh
            white_noise_3.stop()
    
    # *eyes_closed_2* updates
    if eyes_closed_2.status == NOT_STARTED and tThisFlip >= 180.0-frameTolerance:
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
    
    # *instructions_8* updates
    if instructions_8.status == NOT_STARTED and tThisFlip >= 170.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_8.frameNStart = frameN  # exact frame index
        instructions_8.tStart = t  # local t and not account for scr refresh
        instructions_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_8, 'tStartRefresh')  # time at next scr refresh
        instructions_8.setAutoDraw(True)
    if instructions_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_8.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            instructions_8.tStop = t  # not accounting for scr refresh
            instructions_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_8, 'tStopRefresh')  # time at next scr refresh
            instructions_8.setAutoDraw(False)
    # start/stop song_trial_2
    if song_trial_2.status == NOT_STARTED and tThisFlip >= 185.0-frameTolerance:
        # keep track of start time/frame for later
        song_trial_2.frameNStart = frameN  # exact frame index
        song_trial_2.tStart = t  # local t and not account for scr refresh
        song_trial_2.tStartRefresh = tThisFlipGlobal  # on global time
        song_trial_2.play(when=win)  # sync with win flip
    if song_trial_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > song_trial_2.tStartRefresh + 45.0-frameTolerance:
            # keep track of stop time/frame for later
            song_trial_2.tStop = t  # not accounting for scr refresh
            song_trial_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(song_trial_2, 'tStopRefresh')  # time at next scr refresh
            song_trial_2.stop()
    
    # *va_2* updates
    if va_2.status == NOT_STARTED and tThisFlip >= 185.0-frameTolerance:
        # keep track of start time/frame for later
        va_2.frameNStart = frameN  # exact frame index
        va_2.tStart = t  # local t and not account for scr refresh
        va_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(va_2, 'tStartRefresh')  # time at next scr refresh
        va_2.setAutoDraw(True)
    if va_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > va_2.tStartRefresh + 45.0-frameTolerance:
            # keep track of stop time/frame for later
            va_2.tStop = t  # not accounting for scr refresh
            va_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(va_2, 'tStopRefresh')  # time at next scr refresh
            va_2.setAutoDraw(False)
    # *joystick_2* updates
    if joystick_2.status == NOT_STARTED and t >= 185.0-frameTolerance:
        # keep track of start time/frame for later
        joystick_2.frameNStart = frameN  # exact frame index
        joystick_2.tStart = t  # local t and not account for scr refresh
        joystick_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(joystick_2, 'tStartRefresh')  # time at next scr refresh
        joystick_2.status = STARTED
        joystick_2.joystickClock.reset()
    if joystick_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > joystick_2.tStartRefresh + 45.0-frameTolerance:
            # keep track of stop time/frame for later
            joystick_2.tStop = t  # not accounting for scr refresh
            joystick_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(joystick_2, 'tStopRefresh')  # time at next scr refresh
            joystick_2.status = FINISHED
    if joystick_2.status == STARTED:  # only update if started and not finished!
        joystick_2.newButtonState = joystick_2.getAllButtons()[:]
        joystick_2.pressedButtons = [i for i in range(joystick_2.numButtons) if joystick_2.newButtonState[i] and not joystick_2.oldButtonState[i]]
        joystick_2.releasedButtons = [i for i in range(joystick_2.numButtons) if not joystick_2.newButtonState[i] and joystick_2.oldButtonState[i]]
        joystick_2.newPressedButtons = [i for i in joystick_2.activeButtons if i in joystick_2.pressedButtons]
        joystick_2.buttons = joystick_2.newPressedButtons
        [logging.data("joystick_{}_button: {}, pos=({:1.4f},{:1.4f})".format(joystick_2.device_number, i, joystick_2.getX(), joystick_2.getY())) for i in joystick_2.pressedButtons]
        x, y = clamp_stick(joystick_2.getX(), joystick_2.getY())
        joystick_2._x.append(x)
        joystick_2._y.append(y)
        reticle_2.pos = get_clamped_position(joystick_2)
        [joystick_2.buttonLogs[i].append(int(joystick_2.newButtonState[i])) for i in joystick_2.activeButtons]
        joystick_2.time.append(joystick_2.joystickClock.getTime())
    
    # *reticle_2* updates
    if reticle_2.status == NOT_STARTED and tThisFlip >= 185.0-frameTolerance:
        # keep track of start time/frame for later
        reticle_2.frameNStart = frameN  # exact frame index
        reticle_2.tStart = t  # local t and not account for scr refresh
        reticle_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(reticle_2, 'tStartRefresh')  # time at next scr refresh
        reticle_2.setAutoDraw(True)
    if reticle_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > reticle_2.tStartRefresh + 45.0-frameTolerance:
            # keep track of stop time/frame for later
            reticle_2.tStop = t  # not accounting for scr refresh
            reticle_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(reticle_2, 'tStopRefresh')  # time at next scr refresh
            reticle_2.setAutoDraw(False)
    # start/stop eyes_open_alarm
    if eyes_open_alarm.status == NOT_STARTED and tThisFlip >= 230.0-frameTolerance:
        # keep track of start time/frame for later
        eyes_open_alarm.frameNStart = frameN  # exact frame index
        eyes_open_alarm.tStart = t  # local t and not account for scr refresh
        eyes_open_alarm.tStartRefresh = tThisFlipGlobal  # on global time
        eyes_open_alarm.play(when=win)  # sync with win flip
    if eyes_open_alarm.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > eyes_open_alarm.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            eyes_open_alarm.tStop = t  # not accounting for scr refresh
            eyes_open_alarm.frameNStop = frameN  # exact frame index
            win.timeOnFlip(eyes_open_alarm, 'tStopRefresh')  # time at next scr refresh
            eyes_open_alarm.stop()
    
    # *song_rating_2* updates
    if song_rating_2.status == NOT_STARTED and tThisFlip >= 230.0-frameTolerance:
        # keep track of start time/frame for later
        song_rating_2.frameNStart = frameN  # exact frame index
        song_rating_2.tStart = t  # local t and not account for scr refresh
        song_rating_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(song_rating_2, 'tStartRefresh')  # time at next scr refresh
        song_rating_2.setAutoDraw(True)
    if song_rating_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > song_rating_2.tStartRefresh + 30.0-frameTolerance:
            # keep track of stop time/frame for later
            song_rating_2.tStop = t  # not accounting for scr refresh
            song_rating_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(song_rating_2, 'tStopRefresh')  # time at next scr refresh
            song_rating_2.setAutoDraw(False)
    
    # *instructions_9* updates
    if instructions_9.status == NOT_STARTED and tThisFlip >= 260.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_9.frameNStart = frameN  # exact frame index
        instructions_9.tStart = t  # local t and not account for scr refresh
        instructions_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_9, 'tStartRefresh')  # time at next scr refresh
        instructions_9.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 260.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['q'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in example_trial_joystickComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "example_trial_joystick"-------
for thisComponent in example_trial_joystickComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_1.started', instructions_1.tStartRefresh)
thisExp.addData('instructions_1.stopped', instructions_1.tStopRefresh)
thisExp.addData('instructions_2.started', instructions_2.tStartRefresh)
thisExp.addData('instructions_2.stopped', instructions_2.tStopRefresh)
thisExp.addData('instructions_3.started', instructions_3.tStartRefresh)
thisExp.addData('instructions_3.stopped', instructions_3.tStopRefresh)
thisExp.addData('eyes_open.started', eyes_open.tStartRefresh)
thisExp.addData('eyes_open.stopped', eyes_open.tStopRefresh)
thisExp.addData('instructions_4.started', instructions_4.tStartRefresh)
thisExp.addData('instructions_4.stopped', instructions_4.tStopRefresh)
alarm_eyes_open_1.stop()  # ensure sound has stopped at end of routine
thisExp.addData('alarm_eyes_open_1.started', alarm_eyes_open_1.tStartRefresh)
thisExp.addData('alarm_eyes_open_1.stopped', alarm_eyes_open_1.tStopRefresh)
thisExp.addData('eyes_closed.started', eyes_closed.tStartRefresh)
thisExp.addData('eyes_closed.stopped', eyes_closed.tStopRefresh)
eyes_open_alarm_2.stop()  # ensure sound has stopped at end of routine
thisExp.addData('eyes_open_alarm_2.started', eyes_open_alarm_2.tStartRefresh)
thisExp.addData('eyes_open_alarm_2.stopped', eyes_open_alarm_2.tStopRefresh)
thisExp.addData('instructions_5.started', instructions_5.tStartRefresh)
thisExp.addData('instructions_5.stopped', instructions_5.tStopRefresh)
thisExp.addData('instructions_6.started', instructions_6.tStartRefresh)
thisExp.addData('instructions_6.stopped', instructions_6.tStopRefresh)
thisExp.addData('eyes_open_2.started', eyes_open_2.tStartRefresh)
thisExp.addData('eyes_open_2.stopped', eyes_open_2.tStopRefresh)
white_noise.stop()  # ensure sound has stopped at end of routine
thisExp.addData('white_noise.started', white_noise.tStartRefresh)
thisExp.addData('white_noise.stopped', white_noise.tStopRefresh)
white_noise_2.stop()  # ensure sound has stopped at end of routine
thisExp.addData('white_noise_2.started', white_noise_2.tStart)
thisExp.addData('white_noise_2.stopped', white_noise_2.tStop)
song_trial.stop()  # ensure sound has stopped at end of routine
thisExp.addData('song_trial.started', song_trial.tStart)
thisExp.addData('song_trial.stopped', song_trial.tStop)
thisExp.addData('valence_arousal_space.started', valence_arousal_space.tStartRefresh)
thisExp.addData('valence_arousal_space.stopped', valence_arousal_space.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('joystick.x', joystick._x)
thisExp.addData('joystick.y', joystick._y)
thisExp.addData('joystick.time', joystick.time)
[thisExp.addData('joystick.button_{0}'.format(i), joystick.buttonLogs[i]) for i in joystick.activeButtons if len(joystick.buttonLogs[i])]
thisExp.addData('joystick.started', joystick.tStart)
thisExp.addData('joystick.stopped', joystick.tStop)
thisExp.nextEntry()
thisExp.addData('reticle.started', reticle.tStartRefresh)
thisExp.addData('reticle.stopped', reticle.tStopRefresh)
thisExp.addData('instructions_7.started', instructions_7.tStartRefresh)
thisExp.addData('instructions_7.stopped', instructions_7.tStopRefresh)
song_rating.addDataToExp(thisExp, 'rows')
song_rating.autodraw = False
white_noise_3.stop()  # ensure sound has stopped at end of routine
thisExp.addData('white_noise_3.started', white_noise_3.tStart)
thisExp.addData('white_noise_3.stopped', white_noise_3.tStop)
thisExp.addData('eyes_closed_2.started', eyes_closed_2.tStartRefresh)
thisExp.addData('eyes_closed_2.stopped', eyes_closed_2.tStopRefresh)
thisExp.addData('instructions_8.started', instructions_8.tStartRefresh)
thisExp.addData('instructions_8.stopped', instructions_8.tStopRefresh)
song_trial_2.stop()  # ensure sound has stopped at end of routine
thisExp.addData('song_trial_2.started', song_trial_2.tStartRefresh)
thisExp.addData('song_trial_2.stopped', song_trial_2.tStopRefresh)
thisExp.addData('va_2.started', va_2.tStartRefresh)
thisExp.addData('va_2.stopped', va_2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('joystick_2.x', joystick_2._x)
thisExp.addData('joystick_2.y', joystick_2._y)
thisExp.addData('joystick_2.time', joystick_2.time)
[thisExp.addData('joystick_2.button_{0}'.format(i), joystick_2.buttonLogs[i]) for i in joystick_2.activeButtons if len(joystick_2.buttonLogs[i])]
thisExp.addData('joystick_2.started', joystick_2.tStart)
thisExp.addData('joystick_2.stopped', joystick_2.tStop)
thisExp.nextEntry()
thisExp.addData('reticle_2.started', reticle_2.tStartRefresh)
thisExp.addData('reticle_2.stopped', reticle_2.tStopRefresh)
eyes_open_alarm.stop()  # ensure sound has stopped at end of routine
thisExp.addData('eyes_open_alarm.started', eyes_open_alarm.tStartRefresh)
thisExp.addData('eyes_open_alarm.stopped', eyes_open_alarm.tStopRefresh)
song_rating_2.addDataToExp(thisExp, 'rows')
song_rating_2.autodraw = False
thisExp.addData('instructions_9.started', instructions_9.tStartRefresh)
thisExp.addData('instructions_9.stopped', instructions_9.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "example_trial_joystick" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
