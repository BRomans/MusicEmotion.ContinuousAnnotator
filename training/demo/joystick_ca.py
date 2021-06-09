#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on June 03, 2021, at 13:49
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
expName = 'Joystick Demo'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\miche\\EIT\\INTERNSHIP_MYBRAIN\\experimental_phase\\experiment_continuous_annotation\\training\\demo\\joystick_ca.py',
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

# Initialize components for Routine "introduction"
introductionClock = core.Clock()
va_3 = visual.ImageStim(
    win=win,
    name='va_3', 
    image='res\\\\img\\\\valence_arousal_space.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
reticle = visual.ImageStim(
    win=win,
    name='reticle', units='norm', 
    image='res\\\\img\\\\reticle.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
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

key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "introduction"-------
continueRoutine = True
# update component parameters for each repeat
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
joystick.joystickClock.reset()
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
introductionComponents = [va_3, reticle, joystick, key_resp]
for thisComponent in introductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction"-------
while continueRoutine:
    # get current time
    t = introductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introductionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *va_3* updates
    if va_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        va_3.frameNStart = frameN  # exact frame index
        va_3.tStart = t  # local t and not account for scr refresh
        va_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(va_3, 'tStartRefresh')  # time at next scr refresh
        va_3.setAutoDraw(True)
    
    # *reticle* updates
    if reticle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        reticle.frameNStart = frameN  # exact frame index
        reticle.tStart = t  # local t and not account for scr refresh
        reticle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(reticle, 'tStartRefresh')  # time at next scr refresh
        reticle.setAutoDraw(True)
    # *joystick* updates
    if joystick.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        joystick.frameNStart = frameN  # exact frame index
        joystick.tStart = t  # local t and not account for scr refresh
        joystick.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(joystick, 'tStartRefresh')  # time at next scr refresh
        joystick.status = STARTED
    if joystick.status == STARTED:  # only update if started and not finished!
        joystick.newButtonState = joystick.getAllButtons()[:]
        joystick.pressedButtons = [i for i in range(joystick.numButtons) if joystick.newButtonState[i] and not joystick.oldButtonState[i]]
        joystick.releasedButtons = [i for i in range(joystick.numButtons) if not joystick.newButtonState[i] and joystick.oldButtonState[i]]
        joystick.newPressedButtons = [i for i in joystick.activeButtons if i in joystick.pressedButtons]
        joystick.buttons = joystick.newPressedButtons
        [logging.data("joystick_{}_button: {}, pos=({:1.4f},{:1.4f})".format(joystick.device_number, i, joystick.getX(), joystick.getY()) for i in joystick.pressedButtons)]
        x, y = clamp_stick(joystick.getX(), joystick.getY())
        joystick._x.append(x)
        joystick._y.append(y)
        reticle.pos = get_clamped_position(joystick)
        [joystick.buttonLogs[i].append(int(joystick.newButtonState[i])) for i in joystick.activeButtons]
        joystick.time.append(joystick.joystickClock.getTime())
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    for thisComponent in introductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction"-------
for thisComponent in introductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('va_3.started', va_3.tStartRefresh)
thisExp.addData('va_3.stopped', va_3.tStopRefresh)
thisExp.addData('reticle.started', reticle.tStartRefresh)
thisExp.addData('reticle.stopped', reticle.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('joystick.x', joystick._x)
thisExp.addData('joystick.y', joystick._y)
thisExp.addData('joystick.time', joystick.time)
[thisExp.addData('joystick.button_{0}'.format(i), joystick.buttonLogs[i]) for i in joystick.activeButtons if len(joystick.buttonLogs[i])]
thisExp.addData('joystick.started', joystick.tStart)
thisExp.addData('joystick.stopped', joystick.tStop)
thisExp.nextEntry()
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "introduction" was not non-slip safe, so reset the non-slip timer
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
