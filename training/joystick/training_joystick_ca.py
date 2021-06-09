#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on June 03, 2021, at 16:39
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
from utils.joystick_utilities import clamp_stick

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'training_joystick_ca'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\miche\\EIT\\INTERNSHIP_MYBRAIN\\experimental_phase\\experiment_continuous_annotation\\training\\joystick\\training_joystick_ca.py',
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
welcome = visual.TextStim(win=win, name='welcome',
    text='Welcome to the Emotion Music experiment',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
task_introduction = visual.TextStim(win=win, name='task_introduction',
    text='In this experiment your task is to listen to a playlist of song excerpts and rate your emotions in real time.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
va_1 = visual.ImageStim(
    win=win,
    name='va_1', 
    image='res\\\\img\\\\russel_va.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
va_exp_1 = visual.TextStim(win=win, name='va_exp_1',
    text="The quadrant that will be shortly displayed is called Valence-Arousal space.\nIt's an emotion assessment tool developed by James Russel.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text = visual.TextStim(win=win, name='text',
    text='The goal of the Valence-Arousal space is to represent emotions over two dimensions: the valence of an emotion is represented from left (negative) to right (positive). The arousal of an emotion is represented from bottom (low) to top (high). The center represents neutral emotions.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
va_2 = visual.ImageStim(
    win=win,
    name='va_2', 
    image='res\\\\img\\\\valence_arousal_space.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
va_exp_2 = visual.TextStim(win=win, name='va_exp_2',
    text='Here is a simplified version that we are going to use in this experiment.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
va_exp_3 = visual.TextStim(win=win, name='va_exp_3',
    text='Now you are in control. Try to move the red reticle using the LEFT thumbstick of your joystick. The software will record the position automatically. Press ESC when you are done.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
reticle_introduction = visual.ImageStim(
    win=win,
    name='reticle_introduction', units='norm', 
    image='res\\\\img\\\\reticle.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
va_3 = visual.ImageStim(
    win=win,
    name='va_3', 
    image='res\\\\img\\\\valence_arousal_space.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
x, y = [None, None]
joystick_introduction = joysticklib.XboxController(0) # Create an object to use as a name space
joystick_introduction.device = None
joystick_introduction.device_number = 0
joystick_introduction.joystickClock = core.Clock()
joystick_introduction.xFactor = 1
joystick_introduction.yFactor = 1

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        joystick_introduction.device = joystickCache[0]
        if win.units == 'height':
            joystick_introduction.xFactor = 0.5 * win.size[0]/win.size[1]
            joystick_introduction.yFactor = 0.5
    else:
        joystick_introduction.device = virtualjoysticklib.VirtualJoystick(0)
        logging.warning("joystick_{}: Using keyboard+mouse emulation 'ctrl' + 'Alt' + digit.".format(joystick_introduction.device_number))
except Exception:
    pass
    
if not joystick_introduction.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

joystick_introduction.status = None
joystick_introduction.clock = core.Clock()
joystick_introduction.numButtons = joystick_introduction.device.getNumButtons()
joystick_introduction.getNumButtons = joystick_introduction.device.getNumButtons
joystick_introduction.getAllButtons = joystick_introduction.device.getAllButtons
joystick_introduction.getX = lambda: joystick_introduction.xFactor * joystick_introduction.device.getX()
joystick_introduction.getY = lambda: joystick_introduction.yFactor * joystick_introduction.device.getY()


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "introduction"-------
continueRoutine = True
# update component parameters for each repeat
joystick_introduction.oldButtonState = joystick_introduction.device.getAllButtons()[:]
joystick_introduction.activeButtons=[i for i in range(joystick_introduction.numButtons)]
# setup some python lists for storing info about the joystick_introduction
joystick_introduction.x = []
joystick_introduction.y = []
joystick_introduction.buttonLogs = [[] for i in range(joystick_introduction.numButtons)]
joystick_introduction.time = []
gotValidClick = False  # until a click is received
joystick_introduction.joystickClock.reset()
# keep track of which components have finished
introductionComponents = [welcome, task_introduction, va_1, va_exp_1, text, va_2, va_exp_2, va_exp_3, reticle_introduction, va_3, joystick_introduction]
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
        if tThisFlipGlobal > welcome.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            welcome.tStop = t  # not accounting for scr refresh
            welcome.frameNStop = frameN  # exact frame index
            win.timeOnFlip(welcome, 'tStopRefresh')  # time at next scr refresh
            welcome.setAutoDraw(False)
    
    # *task_introduction* updates
    if task_introduction.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
        # keep track of start time/frame for later
        task_introduction.frameNStart = frameN  # exact frame index
        task_introduction.tStart = t  # local t and not account for scr refresh
        task_introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(task_introduction, 'tStartRefresh')  # time at next scr refresh
        task_introduction.setAutoDraw(True)
    if task_introduction.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > task_introduction.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            task_introduction.tStop = t  # not accounting for scr refresh
            task_introduction.frameNStop = frameN  # exact frame index
            win.timeOnFlip(task_introduction, 'tStopRefresh')  # time at next scr refresh
            task_introduction.setAutoDraw(False)
    
    # *va_1* updates
    if va_1.status == NOT_STARTED and tThisFlip >= 20.0-frameTolerance:
        # keep track of start time/frame for later
        va_1.frameNStart = frameN  # exact frame index
        va_1.tStart = t  # local t and not account for scr refresh
        va_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(va_1, 'tStartRefresh')  # time at next scr refresh
        va_1.setAutoDraw(True)
    if va_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > va_1.tStartRefresh + 15.0-frameTolerance:
            # keep track of stop time/frame for later
            va_1.tStop = t  # not accounting for scr refresh
            va_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(va_1, 'tStopRefresh')  # time at next scr refresh
            va_1.setAutoDraw(False)
    
    # *va_exp_1* updates
    if va_exp_1.status == NOT_STARTED and tThisFlip >= 14.0-frameTolerance:
        # keep track of start time/frame for later
        va_exp_1.frameNStart = frameN  # exact frame index
        va_exp_1.tStart = t  # local t and not account for scr refresh
        va_exp_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(va_exp_1, 'tStartRefresh')  # time at next scr refresh
        va_exp_1.setAutoDraw(True)
    if va_exp_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > va_exp_1.tStartRefresh + 6.0-frameTolerance:
            # keep track of stop time/frame for later
            va_exp_1.tStop = t  # not accounting for scr refresh
            va_exp_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(va_exp_1, 'tStopRefresh')  # time at next scr refresh
            va_exp_1.setAutoDraw(False)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 35.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 15.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # *va_2* updates
    if va_2.status == NOT_STARTED and tThisFlip >= 55.0-frameTolerance:
        # keep track of start time/frame for later
        va_2.frameNStart = frameN  # exact frame index
        va_2.tStart = t  # local t and not account for scr refresh
        va_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(va_2, 'tStartRefresh')  # time at next scr refresh
        va_2.setAutoDraw(True)
    if va_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > va_2.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            va_2.tStop = t  # not accounting for scr refresh
            va_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(va_2, 'tStopRefresh')  # time at next scr refresh
            va_2.setAutoDraw(False)
    
    # *va_exp_2* updates
    if va_exp_2.status == NOT_STARTED and tThisFlip >= 50.0-frameTolerance:
        # keep track of start time/frame for later
        va_exp_2.frameNStart = frameN  # exact frame index
        va_exp_2.tStart = t  # local t and not account for scr refresh
        va_exp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(va_exp_2, 'tStartRefresh')  # time at next scr refresh
        va_exp_2.setAutoDraw(True)
    if va_exp_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > va_exp_2.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            va_exp_2.tStop = t  # not accounting for scr refresh
            va_exp_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(va_exp_2, 'tStopRefresh')  # time at next scr refresh
            va_exp_2.setAutoDraw(False)
    
    # *va_exp_3* updates
    if va_exp_3.status == NOT_STARTED and tThisFlip >= 65.0-frameTolerance:
        # keep track of start time/frame for later
        va_exp_3.frameNStart = frameN  # exact frame index
        va_exp_3.tStart = t  # local t and not account for scr refresh
        va_exp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(va_exp_3, 'tStartRefresh')  # time at next scr refresh
        va_exp_3.setAutoDraw(True)
    if va_exp_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > va_exp_3.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            va_exp_3.tStop = t  # not accounting for scr refresh
            va_exp_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(va_exp_3, 'tStopRefresh')  # time at next scr refresh
            va_exp_3.setAutoDraw(False)
    
    # *reticle_introduction* updates
    if reticle_introduction.status == NOT_STARTED and tThisFlip >= 75.0-frameTolerance:
        # keep track of start time/frame for later
        reticle_introduction.frameNStart = frameN  # exact frame index
        reticle_introduction.tStart = t  # local t and not account for scr refresh
        reticle_introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(reticle_introduction, 'tStartRefresh')  # time at next scr refresh
        reticle_introduction.setAutoDraw(True)
    
    # *va_3* updates
    if va_3.status == NOT_STARTED and tThisFlip >= 75.0-frameTolerance:
        # keep track of start time/frame for later
        va_3.frameNStart = frameN  # exact frame index
        va_3.tStart = t  # local t and not account for scr refresh
        va_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(va_3, 'tStartRefresh')  # time at next scr refresh
        va_3.setAutoDraw(True)
    # *joystick_introduction* updates
    if joystick_introduction.status == NOT_STARTED and t >= 75.0-frameTolerance:
        # keep track of start time/frame for later
        joystick_introduction.frameNStart = frameN  # exact frame index
        joystick_introduction.tStart = t  # local t and not account for scr refresh
        joystick_introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(joystick_introduction, 'tStartRefresh')  # time at next scr refresh
        joystick_introduction.status = STARTED
    if joystick_introduction.status == STARTED:  # only update if started and not finished!
        joystick_introduction.newButtonState = joystick_introduction.getAllButtons()[:]
        joystick_introduction.pressedButtons = [i for i in range(joystick_introduction.numButtons) if joystick_introduction.newButtonState[i] and not joystick_introduction.oldButtonState[i]]
        joystick_introduction.releasedButtons = [i for i in range(joystick_introduction.numButtons) if not joystick_introduction.newButtonState[i] and joystick_introduction.oldButtonState[i]]
        joystick_introduction.newPressedButtons = [i for i in joystick_introduction.activeButtons if i in joystick_introduction.pressedButtons]
        joystick_introduction.buttons = joystick_introduction.newPressedButtons
        [logging.data("joystick_{}_button: {}, pos=({:1.4f},{:1.4f})".format(joystick_introduction.device_number, i, joystick_introduction.getX(), joystick_introduction.getY())) for i in joystick_introduction.pressedButtons]
        x, y = clamp_stick(joystick_introduction.getX(), joystick_introduction.getY())
        joystick_introduction.x = x
        joystick_introduction.y = y
        new_target_position = [
            clamp_stick(joystick_introduction.get_left_thumbstick_axis()[0],
                        -joystick_introduction.get_left_thumbstick_axis()[1])]
        reticle_introduction.pos = new_target_position
        [joystick_introduction.buttonLogs[i].append(int(joystick_introduction.newButtonState[i])) for i in joystick_introduction.activeButtons]
        joystick_introduction.time.append(joystick_introduction.joystickClock.getTime())
    
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
thisExp.addData('welcome.started', welcome.tStartRefresh)
thisExp.addData('welcome.stopped', welcome.tStopRefresh)
thisExp.addData('task_introduction.started', task_introduction.tStartRefresh)
thisExp.addData('task_introduction.stopped', task_introduction.tStopRefresh)
thisExp.addData('va_1.started', va_1.tStartRefresh)
thisExp.addData('va_1.stopped', va_1.tStopRefresh)
thisExp.addData('va_exp_1.started', va_exp_1.tStartRefresh)
thisExp.addData('va_exp_1.stopped', va_exp_1.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('va_2.started', va_2.tStartRefresh)
thisExp.addData('va_2.stopped', va_2.tStopRefresh)
thisExp.addData('va_exp_2.started', va_exp_2.tStartRefresh)
thisExp.addData('va_exp_2.stopped', va_exp_2.tStopRefresh)
thisExp.addData('va_exp_3.started', va_exp_3.tStartRefresh)
thisExp.addData('va_exp_3.stopped', va_exp_3.tStopRefresh)
thisExp.addData('reticle_introduction.started', reticle_introduction.tStartRefresh)
thisExp.addData('reticle_introduction.stopped', reticle_introduction.tStopRefresh)
thisExp.addData('va_3.started', va_3.tStartRefresh)
thisExp.addData('va_3.stopped', va_3.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('joystick_introduction.x', joystick_introduction.x)
thisExp.addData('joystick_introduction.y', joystick_introduction.y)
thisExp.addData('joystick_introduction.time', joystick_introduction.time)
[thisExp.addData('joystick_introduction.button_{0}'.format(i), joystick_introduction.buttonLogs[i]) for i in joystick_introduction.activeButtons if len(joystick_introduction.buttonLogs[i])]
thisExp.addData('joystick_introduction.started', joystick_introduction.tStart)
thisExp.addData('joystick_introduction.stopped', joystick_introduction.tStop)
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
