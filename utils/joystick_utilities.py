import math
import numpy as np


# This function is used to clamp the joystick movement in a 1x1 area
def clamp_stick(x, y):
    magnitude = math.sqrt(x * x + y * y)  # Compute magnitude (length) of vector

    if magnitude > 1:
        x /= magnitude
        y /= magnitude

    return x, y


# Normalize the axis value to deal with the joystick dead zone
def dead_zone(axis):
    deadzone = 0.2
    if abs(axis) < deadzone:
        axis = 0
    else:
        # smoothing
        axis = axis - np.sign(axis) * deadzone
        axis /= (1.0 - deadzone)
    return axis
