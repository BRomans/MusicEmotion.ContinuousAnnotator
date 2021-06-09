#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on May 31, 2021, at 22:41
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
    originPath='C:\\Users\\miche\\EIT\\INTERNSHIP_MYBRAIN\\experimental_phase\\experiment_continuous_annotation\\training\\training_mouse_ca.py',
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
va_exp_1_cont = visual.TextStim(win=win, name='va_exp_1_cont',
    text='The goal of the Valence-Arousal space is to represent emotions over two dimensions: the valence of an emotion is represented from left (negative) to right (positive). The arousal of an emotions is represented from bottom (low) to top (high). The center represents neutral emotions.',
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
    text='Now you are in control. Try to move the red reticle using the mouse. The position will be saved automatically. Press ESC when you are done.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
reticle_introduction = visual.ImageStim(
    win=win,
    name='reticle_introduction', 
    image='res\\\\img\\\\reticle.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.075, 0.075),
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
mouse_introduction = event.Mouse(win=win)
x, y = [None, None]
mouse_introduction.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "introduction"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_introduction
mouse_introduction.x = []
mouse_introduction.y = []
mouse_introduction.leftButton = []
mouse_introduction.midButton = []
mouse_introduction.rightButton = []
mouse_introduction.time = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
introductionComponents = [welcome, task_introduction, va_1, va_exp_1, va_exp_1_cont, va_2, va_exp_2, va_exp_3, reticle_introduction, va_3, mouse_introduction]
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
    
    # *va_exp_1_cont* updates
    if va_exp_1_cont.status == NOT_STARTED and tThisFlip >= 35.0-frameTolerance:
        # keep track of start time/frame for later
        va_exp_1_cont.frameNStart = frameN  # exact frame index
        va_exp_1_cont.tStart = t  # local t and not account for scr refresh
        va_exp_1_cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(va_exp_1_cont, 'tStartRefresh')  # time at next scr refresh
        va_exp_1_cont.setAutoDraw(True)
    if va_exp_1_cont.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > va_exp_1_cont.tStartRefresh + 15.0-frameTolerance:
            # keep track of stop time/frame for later
            va_exp_1_cont.tStop = t  # not accounting for scr refresh
            va_exp_1_cont.frameNStop = frameN  # exact frame index
            win.timeOnFlip(va_exp_1_cont, 'tStopRefresh')  # time at next scr refresh
            va_exp_1_cont.setAutoDraw(False)
    
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
    # *mouse_introduction* updates
    if mouse_introduction.status == NOT_STARTED and t >= 75.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_introduction.frameNStart = frameN  # exact frame index
        mouse_introduction.tStart = t  # local t and not account for scr refresh
        mouse_introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_introduction, 'tStartRefresh')  # time at next scr refresh
        mouse_introduction.status = STARTED
        mouse_introduction.mouseClock.reset()
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if mouse_introduction.status == STARTED:  # only update if started and not finished!
        x, y = mouse_introduction.getPos()
        reticle_introduction.pos = [x, y]
        mouse_introduction.x.append(x)
        mouse_introduction.y.append(y)
        buttons = mouse_introduction.getPressed()
        mouse_introduction.leftButton.append(buttons[0])
        mouse_introduction.midButton.append(buttons[1])
        mouse_introduction.rightButton.append(buttons[2])
        mouse_introduction.time.append(mouse_introduction.mouseClock.getTime())
    
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
thisExp.addData('va_exp_1_cont.started', va_exp_1_cont.tStartRefresh)
thisExp.addData('va_exp_1_cont.stopped', va_exp_1_cont.tStopRefresh)
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
thisExp.addData('mouse_introduction.x', mouse_introduction.x)
thisExp.addData('mouse_introduction.y', mouse_introduction.y)
thisExp.addData('mouse_introduction.leftButton', mouse_introduction.leftButton)
thisExp.addData('mouse_introduction.midButton', mouse_introduction.midButton)
thisExp.addData('mouse_introduction.rightButton', mouse_introduction.rightButton)
thisExp.addData('mouse_introduction.time', mouse_introduction.time)
thisExp.addData('mouse_introduction.started', mouse_introduction.tStart)
thisExp.addData('mouse_introduction.stopped', mouse_introduction.tStop)
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
