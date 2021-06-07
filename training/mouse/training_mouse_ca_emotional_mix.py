#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on June 07, 2021, at 17:23
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
expName = 'training_mouse_ca_emotional_mix'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\miche\\EIT\\INTERNSHIP_MYBRAIN\\experimental_phase\\experiment_continuous_annotation\\training\\mouse\\training_mouse_ca_emotional_mix.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
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

# Initialize components for Routine "trial"
trialClock = core.Clock()
welcome = visual.TextStim(win=win, name='welcome',
    text='Welcome to the annotation training',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
description = visual.TextStim(win=win, name='description',
    text='The purpose of this training is to get you acquainted with the annotation task.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructions = visual.TextStim(win=win, name='instructions',
    text='For the next 3 minutes, you will hear a mix of different songs with no breaks in between.\nYour task is:\n- Move the reticle along the Valence-Arousal space in the area corresponding to the emotion you are feeling\n- Adjust the reticle position if the arousal intensity or the emotional valence changes over time\n- Return to the Neutral Zone when a new song starts',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
warning = visual.TextStim(win=win, name='warning',
    text="Be careful to the following:\n- You need to annotate the emotion you are feeling, not the emotion you think the artist wants to communicate (sometimes they are the same emotion, sometimes they are not)\n- You don't need to click anywhere, the position of the reticle is saved every second in background\n- You should stay on the Valence-Arousal space and avoid the grey area, annotations there are not saved.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
raedy = visual.TextStim(win=win, name='raedy',
    text='Alright, get ready! :)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
valence_arousal_space = visual.ImageStim(
    win=win,
    name='valence_arousal_space', 
    image='res\\\\img\\\\valence_arousal_space.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
song_mix = sound.Sound('res\\playlist\\emotional_mashup.ogg', secs=-1.0, stereo=True, hamming=True,
    name='song_mix')
song_mix.setVolume(1.0)
reticle = visual.ImageStim(
    win=win,
    name='reticle', 
    image='res\\\\img\\\\reticle.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.075, 0.075),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
done = visual.TextStim(win=win, name='done',
    text='Bravo!\n\nPress Q to save and exit :)',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
song_mix.setSound('res\\playlist\\emotional_mashup.ogg', secs=180.0, hamming=True)
song_mix.setVolume(1.0, log=False)
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
gotValidClick = False  # until a click is received
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
trialComponents = [welcome, description, instructions, warning, raedy, valence_arousal_space, song_mix, reticle, mouse, done, key_resp]
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
first_mouse_frame = True

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
        if tThisFlipGlobal > welcome.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            welcome.tStop = t  # not accounting for scr refresh
            welcome.frameNStop = frameN  # exact frame index
            win.timeOnFlip(welcome, 'tStopRefresh')  # time at next scr refresh
            welcome.setAutoDraw(False)
    
    # *description* updates
    if description.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        description.frameNStart = frameN  # exact frame index
        description.tStart = t  # local t and not account for scr refresh
        description.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(description, 'tStartRefresh')  # time at next scr refresh
        description.setAutoDraw(True)
    if description.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > description.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            description.tStop = t  # not accounting for scr refresh
            description.frameNStop = frameN  # exact frame index
            win.timeOnFlip(description, 'tStopRefresh')  # time at next scr refresh
            description.setAutoDraw(False)
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 20.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    if instructions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions.tStartRefresh + 25.0-frameTolerance:
            # keep track of stop time/frame for later
            instructions.tStop = t  # not accounting for scr refresh
            instructions.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions, 'tStopRefresh')  # time at next scr refresh
            instructions.setAutoDraw(False)
    
    # *warning* updates
    if warning.status == NOT_STARTED and tThisFlip >= 45.0-frameTolerance:
        # keep track of start time/frame for later
        warning.frameNStart = frameN  # exact frame index
        warning.tStart = t  # local t and not account for scr refresh
        warning.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(warning, 'tStartRefresh')  # time at next scr refresh
        warning.setAutoDraw(True)
    if warning.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > warning.tStartRefresh + 25.0-frameTolerance:
            # keep track of stop time/frame for later
            warning.tStop = t  # not accounting for scr refresh
            warning.frameNStop = frameN  # exact frame index
            win.timeOnFlip(warning, 'tStopRefresh')  # time at next scr refresh
            warning.setAutoDraw(False)
    
    # *raedy* updates
    if raedy.status == NOT_STARTED and tThisFlip >= 70.0-frameTolerance:
        # keep track of start time/frame for later
        raedy.frameNStart = frameN  # exact frame index
        raedy.tStart = t  # local t and not account for scr refresh
        raedy.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(raedy, 'tStartRefresh')  # time at next scr refresh
        raedy.setAutoDraw(True)
    if raedy.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > raedy.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            raedy.tStop = t  # not accounting for scr refresh
            raedy.frameNStop = frameN  # exact frame index
            win.timeOnFlip(raedy, 'tStopRefresh')  # time at next scr refresh
            raedy.setAutoDraw(False)
    
    # *valence_arousal_space* updates
    if valence_arousal_space.status == NOT_STARTED and tThisFlip >= 80.0-frameTolerance:
        # keep track of start time/frame for later
        valence_arousal_space.frameNStart = frameN  # exact frame index
        valence_arousal_space.tStart = t  # local t and not account for scr refresh
        valence_arousal_space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(valence_arousal_space, 'tStartRefresh')  # time at next scr refresh
        valence_arousal_space.setAutoDraw(True)
    if valence_arousal_space.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > valence_arousal_space.tStartRefresh + 180.0-frameTolerance:
            # keep track of stop time/frame for later
            valence_arousal_space.tStop = t  # not accounting for scr refresh
            valence_arousal_space.frameNStop = frameN  # exact frame index
            win.timeOnFlip(valence_arousal_space, 'tStopRefresh')  # time at next scr refresh
            valence_arousal_space.setAutoDraw(False)
    # start/stop song_mix
    if song_mix.status == NOT_STARTED and t >= 80.0-frameTolerance:
        # keep track of start time/frame for later
        song_mix.frameNStart = frameN  # exact frame index
        song_mix.tStart = t  # local t and not account for scr refresh
        song_mix.tStartRefresh = tThisFlipGlobal  # on global time
        song_mix.play()  # start the sound (it finishes automatically)
    if song_mix.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > song_mix.tStartRefresh + 180.0-frameTolerance:
            # keep track of stop time/frame for later
            song_mix.tStop = t  # not accounting for scr refresh
            song_mix.frameNStop = frameN  # exact frame index
            win.timeOnFlip(song_mix, 'tStopRefresh')  # time at next scr refresh
            song_mix.stop()
    
    # *reticle* updates
    if reticle.status == NOT_STARTED and tThisFlip >= 80.0-frameTolerance:
        # keep track of start time/frame for later
        reticle.frameNStart = frameN  # exact frame index
        reticle.tStart = t  # local t and not account for scr refresh
        reticle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(reticle, 'tStartRefresh')  # time at next scr refresh
        reticle.setAutoDraw(True)
    if reticle.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > reticle.tStartRefresh + 180.0-frameTolerance:
            # keep track of stop time/frame for later
            reticle.tStop = t  # not accounting for scr refresh
            reticle.frameNStop = frameN  # exact frame index
            win.timeOnFlip(reticle, 'tStopRefresh')  # time at next scr refresh
            reticle.setAutoDraw(False)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 80.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        if first_mouse_frame:
            mouse.setPos([0, 0])
            first_mouse_frame = False
        x, y = mouse.getPos()
        mouse.x.append(x)
        mouse.y.append(y)
        buttons = mouse.getPressed()
        mouse.leftButton.append(buttons[0])
        mouse.midButton.append(buttons[1])
        mouse.rightButton.append(buttons[2])
        mouse.time.append(mouse.mouseClock.getTime())
    
    # *done* updates
    if done.status == NOT_STARTED and tThisFlip >= 260.0-frameTolerance:
        # keep track of start time/frame for later
        done.frameNStart = frameN  # exact frame index
        done.tStart = t  # local t and not account for scr refresh
        done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(done, 'tStartRefresh')  # time at next scr refresh
        done.setAutoDraw(True)
    
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
thisExp.addData('welcome.started', welcome.tStartRefresh)
thisExp.addData('welcome.stopped', welcome.tStopRefresh)
thisExp.addData('description.started', description.tStartRefresh)
thisExp.addData('description.stopped', description.tStopRefresh)
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
thisExp.addData('warning.started', warning.tStartRefresh)
thisExp.addData('warning.stopped', warning.tStopRefresh)
thisExp.addData('raedy.started', raedy.tStartRefresh)
thisExp.addData('raedy.stopped', raedy.tStopRefresh)
thisExp.addData('valence_arousal_space.started', valence_arousal_space.tStartRefresh)
thisExp.addData('valence_arousal_space.stopped', valence_arousal_space.tStopRefresh)
song_mix.stop()  # ensure sound has stopped at end of routine
thisExp.addData('song_mix.started', song_mix.tStart)
thisExp.addData('song_mix.stopped', song_mix.tStop)
thisExp.addData('reticle.started', reticle.tStartRefresh)
thisExp.addData('reticle.stopped', reticle.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.x', mouse.x)
thisExp.addData('mouse.y', mouse.y)
thisExp.addData('mouse.leftButton', mouse.leftButton)
thisExp.addData('mouse.midButton', mouse.midButton)
thisExp.addData('mouse.rightButton', mouse.rightButton)
thisExp.addData('mouse.time', mouse.time)
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
thisExp.addData('done.started', done.tStartRefresh)
thisExp.addData('done.stopped', done.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
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
