#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on May 28, 2021, at 17:31
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
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'experiment_eo_ec_controller_annotations'  # from the Builder filename that created this script
expInfo = {'participant': '', 'id': '', 'gender (M/F/N)': '', 'age': '', 'session': '001', 'group': '01'}
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
    originPath='C:\\Users\\miche\\EIT\\INTERNSHIP_MYBRAIN\\experimental_phase\\experiment_continuous_annotation\\experiment_draft.py',
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

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
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

# Initialize components for Routine "opening"
openingClock = core.Clock()
white_noise = sound.Sound('res\\1 min wn.wav', secs=-1.0, stereo=True, hamming=True,
    name='white_noise')
white_noise.setVolume(1.0)
welcome = visual.TextStim(win=win, name='welcome',
    text='Welcome to the Emotion Music experiment',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructions = visual.TextStim(win=win, name='instructions',
    text='The sound you are hearing is called White Noise, it serves to reset your emotions to a neutral condition.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
eo_instructions = visual.TextStim(win=win, name='eo_instructions',
    text='Now keep your eyes OPEN, the experiment is about to start',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
eyes_open_test = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='eyes_open_test')
eyes_open_test.setVolume(0.5)
beep_instructions = visual.TextStim(win=win, name='beep_instructions',
    text="When you hear this BEEP it means it's time to OPEN your eyes.",
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
joystick_target = visual.ImageStim(
    win=win,
    name='joystick_target', 
    image='res\\\\circle.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.075, 0.075),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
song_one = sound.Sound('res\\Daft Punk - Within (Official Audio).ogg', secs=-1.0, stereo=True, hamming=True,
    name='song_one')
song_one.setVolume(1.0)
valence_arousal_space = visual.ImageStim(
    win=win,
    name='valence_arousal_space', 
    image='res\\\\valece_arousal_space.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.2, 1.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
x, y = [None, None]
joystick = joysticklib.XboxController(0)  # Create an object to use as a name space
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

open_eyes = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='open_eyes')
open_eyes.setVolume(0.5)
win.allowStencil = True
song_one_rating = visual.Form(win=win, name='song_one_rating',
    items='res\\\\rating_form.csv',
    textHeight=0.03,
    randomize=False,
    size=(1.5, 0.7),
    pos=(0, 0),
    style='dark',
    itemPadding=0.1,)
white_noise_rating = sound.Sound('res\\1 min wn.wav', secs=-1.0, stereo=True, hamming=True,
    name='white_noise_rating')
white_noise_rating.setVolume(1.0)
instruction_ec = visual.TextStim(win=win, name='instruction_ec',
    text='Now CLOSE your eyes and get ready for the next song.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
song_two = sound.Sound('res\\Metallica-Fade To Black www.my-free-mp3.net  (1).ogg', secs=-1.0, stereo=True, hamming=True,
    name='song_two')
song_two.setVolume(1.0)
valence_arousal_space_two = visual.ImageStim(
    win=win,
    name='valence_arousal_space_two', 
    image='res\\\\valece_arousal_space.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
eyes_open = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='eyes_open')
eyes_open.setVolume(0.5)
win.allowStencil = True
song_two_rating = visual.Form(win=win, name='song_two_rating',
    items='res\\\\rating_form.csv',
    textHeight=0.03,
    randomize=False,
    size=(1.5, 0.7),
    pos=(0, 0),
    style='dark',
    itemPadding=0.05,)
white_noise_rating_two = sound.Sound('res\\1 min wn.wav', secs=-1.0, stereo=True, hamming=True,
    name='white_noise_rating_two')
white_noise_rating_two.setVolume(1.0)
instruction_eo = visual.TextStim(win=win, name='instruction_eo',
    text='Now OPEN your eyes and get ready for the next song.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "opening"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
white_noise.setSound('res\\1 min wn.wav', secs=15.0, hamming=True)
white_noise.setVolume(1.0, log=False)
eyes_open_test.setSound('A', secs=1.0, hamming=True)
eyes_open_test.setVolume(0.5, log=False)
# keep track of which components have finished
openingComponents = [white_noise, welcome, instructions, eo_instructions, eyes_open_test, beep_instructions]
for thisComponent in openingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
openingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "opening"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = openingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=openingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop white_noise
    if white_noise.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        white_noise.frameNStart = frameN  # exact frame index
        white_noise.tStart = t  # local t and not account for scr refresh
        white_noise.tStartRefresh = tThisFlipGlobal  # on global time
        white_noise.play(when=win)  # sync with win flip
    if white_noise.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > white_noise.tStartRefresh + 15.0-frameTolerance:
            # keep track of stop time/frame for later
            white_noise.tStop = t  # not accounting for scr refresh
            white_noise.frameNStop = frameN  # exact frame index
            win.timeOnFlip(white_noise, 'tStopRefresh')  # time at next scr refresh
            white_noise.stop()
    
    # *welcome* updates
    if welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome.frameNStart = frameN  # exact frame index
        welcome.tStart = t  # local t and not account for scr refresh
        welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome, 'tStartRefresh')  # time at next scr refresh
        welcome.setAutoDraw(True)
    if welcome.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > welcome.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            welcome.tStop = t  # not accounting for scr refresh
            welcome.frameNStop = frameN  # exact frame index
            win.timeOnFlip(welcome, 'tStopRefresh')  # time at next scr refresh
            welcome.setAutoDraw(False)
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    if instructions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            instructions.tStop = t  # not accounting for scr refresh
            instructions.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions, 'tStopRefresh')  # time at next scr refresh
            instructions.setAutoDraw(False)
    
    # *eo_instructions* updates
    if eo_instructions.status == NOT_STARTED and tThisFlip >= 11.0-frameTolerance:
        # keep track of start time/frame for later
        eo_instructions.frameNStart = frameN  # exact frame index
        eo_instructions.tStart = t  # local t and not account for scr refresh
        eo_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eo_instructions, 'tStartRefresh')  # time at next scr refresh
        eo_instructions.setAutoDraw(True)
    if eo_instructions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > eo_instructions.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            eo_instructions.tStop = t  # not accounting for scr refresh
            eo_instructions.frameNStop = frameN  # exact frame index
            win.timeOnFlip(eo_instructions, 'tStopRefresh')  # time at next scr refresh
            eo_instructions.setAutoDraw(False)
    # start/stop eyes_open_test
    if eyes_open_test.status == NOT_STARTED and tThisFlip >= 9.0-frameTolerance:
        # keep track of start time/frame for later
        eyes_open_test.frameNStart = frameN  # exact frame index
        eyes_open_test.tStart = t  # local t and not account for scr refresh
        eyes_open_test.tStartRefresh = tThisFlipGlobal  # on global time
        eyes_open_test.play(when=win)  # sync with win flip
    if eyes_open_test.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > eyes_open_test.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            eyes_open_test.tStop = t  # not accounting for scr refresh
            eyes_open_test.frameNStop = frameN  # exact frame index
            win.timeOnFlip(eyes_open_test, 'tStopRefresh')  # time at next scr refresh
            eyes_open_test.stop()
    
    # *beep_instructions* updates
    if beep_instructions.status == NOT_STARTED and tThisFlip >= 7.0-frameTolerance:
        # keep track of start time/frame for later
        beep_instructions.frameNStart = frameN  # exact frame index
        beep_instructions.tStart = t  # local t and not account for scr refresh
        beep_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(beep_instructions, 'tStartRefresh')  # time at next scr refresh
        beep_instructions.setAutoDraw(True)
    if beep_instructions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > beep_instructions.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            beep_instructions.tStop = t  # not accounting for scr refresh
            beep_instructions.frameNStop = frameN  # exact frame index
            win.timeOnFlip(beep_instructions, 'tStopRefresh')  # time at next scr refresh
            beep_instructions.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in openingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "opening"-------
for thisComponent in openingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
white_noise.stop()  # ensure sound has stopped at end of routine
thisExp.addData('white_noise.started', white_noise.tStartRefresh)
thisExp.addData('white_noise.stopped', white_noise.tStopRefresh)
thisExp.addData('welcome.started', welcome.tStartRefresh)
thisExp.addData('welcome.stopped', welcome.tStopRefresh)
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
thisExp.addData('eo_instructions.started', eo_instructions.tStartRefresh)
thisExp.addData('eo_instructions.stopped', eo_instructions.tStopRefresh)
eyes_open_test.stop()  # ensure sound has stopped at end of routine
thisExp.addData('eyes_open_test.started', eyes_open_test.tStartRefresh)
thisExp.addData('eyes_open_test.stopped', eyes_open_test.tStopRefresh)
thisExp.addData('beep_instructions.started', beep_instructions.tStartRefresh)
thisExp.addData('beep_instructions.stopped', beep_instructions.tStopRefresh)

# set up handler to look after randomisation of conditions etc
music_emotion_trial_eo_ec = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='music_emotion_trial_eo_ec')
thisExp.addLoop(music_emotion_trial_eo_ec)  # add the loop to the experiment
thisMusic_emotion_trial_eo_ec = music_emotion_trial_eo_ec.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMusic_emotion_trial_eo_ec.rgb)
if thisMusic_emotion_trial_eo_ec != None:
    for paramName in thisMusic_emotion_trial_eo_ec:
        exec('{} = thisMusic_emotion_trial_eo_ec[paramName]'.format(paramName))

for thisMusic_emotion_trial_eo_ec in music_emotion_trial_eo_ec:
    currentLoop = music_emotion_trial_eo_ec
    # abbreviate parameter names if possible (e.g. rgb = thisMusic_emotion_trial_eo_ec.rgb)
    if thisMusic_emotion_trial_eo_ec != None:
        for paramName in thisMusic_emotion_trial_eo_ec:
            exec('{} = thisMusic_emotion_trial_eo_ec[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(150.000000)
    # update component parameters for each repeat
    song_one.setSound('res\\Daft Punk - Within (Official Audio).ogg', secs=45.0, hamming=True)
    song_one.setVolume(1.0, log=False)
    joystick.oldButtonState = joystick.device.getAllButtons()[:]
    joystick.activeButtons=[i for i in range(joystick.numButtons)]
    # setup some python lists for storing info about the joystick
    joystick.x = []
    joystick.y = []
    joystick.buttonLogs = [[] for i in range(joystick.numButtons)]
    joystick.time = []
    gotValidClick = False  # until a click is received
    joystick.joystickClock.reset()
    open_eyes.setSound('A', secs=1.0, hamming=True)
    open_eyes.setVolume(0.5, log=False)
    white_noise_rating.setSound('res\\1 min wn.wav', secs=15.0, hamming=True)
    white_noise_rating.setVolume(1.0, log=False)
    song_two.setSound('res\\Metallica-Fade To Black www.my-free-mp3.net  (1).ogg', secs=45.0, hamming=True)
    song_two.setVolume(1.0, log=False)
    eyes_open.setSound('A', secs=1.0, hamming=True)
    eyes_open.setVolume(0.5, log=False)
    white_noise_rating_two.setSound('res\\1 min wn.wav', secs=15.0, hamming=True)
    white_noise_rating_two.setVolume(1.0, log=False)
    # keep track of which components have finished
    trialComponents = [joystick_target, song_one, valence_arousal_space, joystick, open_eyes, song_one_rating, white_noise_rating, instruction_ec, song_two, valence_arousal_space_two, eyes_open, song_two_rating, white_noise_rating_two, instruction_eo]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *joystick_target* updates
        if joystick_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            joystick_target.frameNStart = frameN  # exact frame index
            joystick_target.tStart = t  # local t and not account for scr refresh
            joystick_target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(joystick_target, 'tStartRefresh')  # time at next scr refresh
            joystick_target.setAutoDraw(True)
        if joystick_target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > joystick_target.tStartRefresh + 45.0-frameTolerance:
                # keep track of stop time/frame for later
                joystick_target.tStop = t  # not accounting for scr refresh
                joystick_target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(joystick_target, 'tStopRefresh')  # time at next scr refresh
                joystick_target.setAutoDraw(False)
        # start/stop song_one
        if song_one.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            song_one.frameNStart = frameN  # exact frame index
            song_one.tStart = t  # local t and not account for scr refresh
            song_one.tStartRefresh = tThisFlipGlobal  # on global time
            song_one.play(when=win)  # sync with win flip
        if song_one.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > song_one.tStartRefresh + 45.0-frameTolerance:
                # keep track of stop time/frame for later
                song_one.tStop = t  # not accounting for scr refresh
                song_one.frameNStop = frameN  # exact frame index
                win.timeOnFlip(song_one, 'tStopRefresh')  # time at next scr refresh
                song_one.stop()
        
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
            if tThisFlipGlobal > valence_arousal_space.tStartRefresh + 45.0-frameTolerance:
                # keep track of stop time/frame for later
                valence_arousal_space.tStop = t  # not accounting for scr refresh
                valence_arousal_space.frameNStop = frameN  # exact frame index
                win.timeOnFlip(valence_arousal_space, 'tStopRefresh')  # time at next scr refresh
                valence_arousal_space.setAutoDraw(False)
        # *joystick* updates
        if joystick.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            joystick.frameNStart = frameN  # exact frame index
            joystick.tStart = t  # local t and not account for scr refresh
            joystick.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(joystick, 'tStartRefresh')  # time at next scr refresh
            joystick.status = STARTED
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
            [logging.data("joystick_{}_button: {}, pos=({:1.4f},{:1.4f})".format(joystick.device_number, i, joystick.getX(), joystick.getY()) for i in joystick.pressedButtons)]
            x, y = joystick.getX(), joystick.getY()
            joystick._x = x
            joystick._y = y
            new_target_position = [joystick.get_left_thumbstick_axis()[0], -joystick.get_left_thumbstick_axis()[1]]
            joystick_target.pos = new_target_position
            [joystick.buttonLogs[i].append(int(joystick.newButtonState[i])) for i in joystick.activeButtons]
            joystick.time.append(joystick.joystickClock.getTime())
        # start/stop open_eyes
        if open_eyes.status == NOT_STARTED and tThisFlip >= 45.0-frameTolerance:
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
        if song_one_rating.status == NOT_STARTED and tThisFlip >= 45.0-frameTolerance:
            # keep track of start time/frame for later
            song_one_rating.frameNStart = frameN  # exact frame index
            song_one_rating.tStart = t  # local t and not account for scr refresh
            song_one_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(song_one_rating, 'tStartRefresh')  # time at next scr refresh
            song_one_rating.setAutoDraw(True)
        if song_one_rating.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > song_one_rating.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                song_one_rating.tStop = t  # not accounting for scr refresh
                song_one_rating.frameNStop = frameN  # exact frame index
                win.timeOnFlip(song_one_rating, 'tStopRefresh')  # time at next scr refresh
                song_one_rating.setAutoDraw(False)
        # start/stop white_noise_rating
        if white_noise_rating.status == NOT_STARTED and tThisFlip >= 60.0-frameTolerance:
            # keep track of start time/frame for later
            white_noise_rating.frameNStart = frameN  # exact frame index
            white_noise_rating.tStart = t  # local t and not account for scr refresh
            white_noise_rating.tStartRefresh = tThisFlipGlobal  # on global time
            white_noise_rating.play(when=win)  # sync with win flip
        if white_noise_rating.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > white_noise_rating.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                white_noise_rating.tStop = t  # not accounting for scr refresh
                white_noise_rating.frameNStop = frameN  # exact frame index
                win.timeOnFlip(white_noise_rating, 'tStopRefresh')  # time at next scr refresh
                white_noise_rating.stop()
        
        # *instruction_ec* updates
        if instruction_ec.status == NOT_STARTED and tThisFlip >= 60.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_ec.frameNStart = frameN  # exact frame index
            instruction_ec.tStart = t  # local t and not account for scr refresh
            instruction_ec.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_ec, 'tStartRefresh')  # time at next scr refresh
            instruction_ec.setAutoDraw(True)
        if instruction_ec.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_ec.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                instruction_ec.tStop = t  # not accounting for scr refresh
                instruction_ec.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruction_ec, 'tStopRefresh')  # time at next scr refresh
                instruction_ec.setAutoDraw(False)
        # start/stop song_two
        if song_two.status == NOT_STARTED and tThisFlip >= 75.0-frameTolerance:
            # keep track of start time/frame for later
            song_two.frameNStart = frameN  # exact frame index
            song_two.tStart = t  # local t and not account for scr refresh
            song_two.tStartRefresh = tThisFlipGlobal  # on global time
            song_two.play(when=win)  # sync with win flip
        if song_two.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > song_two.tStartRefresh + 45.0-frameTolerance:
                # keep track of stop time/frame for later
                song_two.tStop = t  # not accounting for scr refresh
                song_two.frameNStop = frameN  # exact frame index
                win.timeOnFlip(song_two, 'tStopRefresh')  # time at next scr refresh
                song_two.stop()
        
        # *valence_arousal_space_two* updates
        if valence_arousal_space_two.status == NOT_STARTED and tThisFlip >= 75.0-frameTolerance:
            # keep track of start time/frame for later
            valence_arousal_space_two.frameNStart = frameN  # exact frame index
            valence_arousal_space_two.tStart = t  # local t and not account for scr refresh
            valence_arousal_space_two.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(valence_arousal_space_two, 'tStartRefresh')  # time at next scr refresh
            valence_arousal_space_two.setAutoDraw(True)
        if valence_arousal_space_two.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > valence_arousal_space_two.tStartRefresh + 45.0-frameTolerance:
                # keep track of stop time/frame for later
                valence_arousal_space_two.tStop = t  # not accounting for scr refresh
                valence_arousal_space_two.frameNStop = frameN  # exact frame index
                win.timeOnFlip(valence_arousal_space_two, 'tStopRefresh')  # time at next scr refresh
                valence_arousal_space_two.setAutoDraw(False)
        # start/stop eyes_open
        if eyes_open.status == NOT_STARTED and tThisFlip >= 120.0-frameTolerance:
            # keep track of start time/frame for later
            eyes_open.frameNStart = frameN  # exact frame index
            eyes_open.tStart = t  # local t and not account for scr refresh
            eyes_open.tStartRefresh = tThisFlipGlobal  # on global time
            eyes_open.play(when=win)  # sync with win flip
        if eyes_open.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eyes_open.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                eyes_open.tStop = t  # not accounting for scr refresh
                eyes_open.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eyes_open, 'tStopRefresh')  # time at next scr refresh
                eyes_open.stop()
        
        # *song_two_rating* updates
        if song_two_rating.status == NOT_STARTED and tThisFlip >= 120.0-frameTolerance:
            # keep track of start time/frame for later
            song_two_rating.frameNStart = frameN  # exact frame index
            song_two_rating.tStart = t  # local t and not account for scr refresh
            song_two_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(song_two_rating, 'tStartRefresh')  # time at next scr refresh
            song_two_rating.setAutoDraw(True)
        if song_two_rating.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > song_two_rating.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                song_two_rating.tStop = t  # not accounting for scr refresh
                song_two_rating.frameNStop = frameN  # exact frame index
                win.timeOnFlip(song_two_rating, 'tStopRefresh')  # time at next scr refresh
                song_two_rating.setAutoDraw(False)
        # start/stop white_noise_rating_two
        if white_noise_rating_two.status == NOT_STARTED and tThisFlip >= 135.0-frameTolerance:
            # keep track of start time/frame for later
            white_noise_rating_two.frameNStart = frameN  # exact frame index
            white_noise_rating_two.tStart = t  # local t and not account for scr refresh
            white_noise_rating_two.tStartRefresh = tThisFlipGlobal  # on global time
            white_noise_rating_two.play(when=win)  # sync with win flip
        if white_noise_rating_two.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > white_noise_rating_two.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                white_noise_rating_two.tStop = t  # not accounting for scr refresh
                white_noise_rating_two.frameNStop = frameN  # exact frame index
                win.timeOnFlip(white_noise_rating_two, 'tStopRefresh')  # time at next scr refresh
                white_noise_rating_two.stop()
        
        # *instruction_eo* updates
        if instruction_eo.status == NOT_STARTED and tThisFlip >= 135.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_eo.frameNStart = frameN  # exact frame index
            instruction_eo.tStart = t  # local t and not account for scr refresh
            instruction_eo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_eo, 'tStartRefresh')  # time at next scr refresh
            instruction_eo.setAutoDraw(True)
        if instruction_eo.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_eo.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                instruction_eo.tStop = t  # not accounting for scr refresh
                instruction_eo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruction_eo, 'tStopRefresh')  # time at next scr refresh
                instruction_eo.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    music_emotion_trial_eo_ec.addData('joystick_target.started', joystick_target.tStartRefresh)
    music_emotion_trial_eo_ec.addData('joystick_target.stopped', joystick_target.tStopRefresh)
    song_one.stop()  # ensure sound has stopped at end of routine
    music_emotion_trial_eo_ec.addData('song_one.started', song_one.tStartRefresh)
    music_emotion_trial_eo_ec.addData('song_one.stopped', song_one.tStopRefresh)
    music_emotion_trial_eo_ec.addData('valence_arousal_space.started', valence_arousal_space.tStartRefresh)
    music_emotion_trial_eo_ec.addData('valence_arousal_space.stopped', valence_arousal_space.tStopRefresh)
    # store data for music_emotion_trial_eo_ec (TrialHandler)
    music_emotion_trial_eo_ec.addData('joystick.x', joystick.x)
    music_emotion_trial_eo_ec.addData('joystick.y', joystick.y)
    music_emotion_trial_eo_ec.addData('joystick.time', joystick.time)
    [music_emotion_trial_eo_ec.addData('joystick.button_{0}'.format(i), joystick.buttonLogs[i]) for i in joystick.activeButtons if len(joystick.buttonLogs[i])]
    music_emotion_trial_eo_ec.addData('joystick.started', joystick.tStart)
    music_emotion_trial_eo_ec.addData('joystick.stopped', joystick.tStop)
    open_eyes.stop()  # ensure sound has stopped at end of routine
    music_emotion_trial_eo_ec.addData('open_eyes.started', open_eyes.tStartRefresh)
    music_emotion_trial_eo_ec.addData('open_eyes.stopped', open_eyes.tStopRefresh)
    song_one_rating.addDataToExp(thisExp, 'rows')
    song_one_rating.autodraw = False
    white_noise_rating.stop()  # ensure sound has stopped at end of routine
    music_emotion_trial_eo_ec.addData('white_noise_rating.started', white_noise_rating.tStartRefresh)
    music_emotion_trial_eo_ec.addData('white_noise_rating.stopped', white_noise_rating.tStopRefresh)
    music_emotion_trial_eo_ec.addData('instruction_ec.started', instruction_ec.tStartRefresh)
    music_emotion_trial_eo_ec.addData('instruction_ec.stopped', instruction_ec.tStopRefresh)
    song_two.stop()  # ensure sound has stopped at end of routine
    music_emotion_trial_eo_ec.addData('song_two.started', song_two.tStartRefresh)
    music_emotion_trial_eo_ec.addData('song_two.stopped', song_two.tStopRefresh)
    music_emotion_trial_eo_ec.addData('valence_arousal_space_two.started', valence_arousal_space_two.tStartRefresh)
    music_emotion_trial_eo_ec.addData('valence_arousal_space_two.stopped', valence_arousal_space_two.tStopRefresh)
    eyes_open.stop()  # ensure sound has stopped at end of routine
    music_emotion_trial_eo_ec.addData('eyes_open.started', eyes_open.tStartRefresh)
    music_emotion_trial_eo_ec.addData('eyes_open.stopped', eyes_open.tStopRefresh)
    song_two_rating.addDataToExp(thisExp, 'rows')
    song_two_rating.autodraw = False
    white_noise_rating_two.stop()  # ensure sound has stopped at end of routine
    music_emotion_trial_eo_ec.addData('white_noise_rating_two.started', white_noise_rating_two.tStartRefresh)
    music_emotion_trial_eo_ec.addData('white_noise_rating_two.stopped', white_noise_rating_two.tStopRefresh)
    music_emotion_trial_eo_ec.addData('instruction_eo.started', instruction_eo.tStartRefresh)
    music_emotion_trial_eo_ec.addData('instruction_eo.stopped', instruction_eo.tStopRefresh)
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'music_emotion_trial_eo_ec'

# get names of stimulus parameters
if music_emotion_trial_eo_ec.trialList in ([], [None], None):
    params = []
else:
    params = music_emotion_trial_eo_ec.trialList[0].keys()
# save data for this loop
music_emotion_trial_eo_ec.saveAsExcel(filename + '.xlsx', sheetName='music_emotion_trial_eo_ec',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
music_emotion_trial_eo_ec.saveAsText(filename + 'music_emotion_trial_eo_ec.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

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
