from utils.joystick_utilities import get_clamped_position

joysticklib.backend = 'glfw'
joystick = joysticklib.XboxController(0)
joystick._x = []
joystick._y = []

x, y = clamp_stick(joystick.getX(), joystick.getY())
joystick._x.append(x)
joystick._y.append(y)
reticle.pos = get_clamped_position(joystick)


thisExp.addData('joystick.x', joystick._x)
thisExp.addData('joystick.y', joystick._y)

# mouse
x, y = mouse.getPos()
reticle.pos = [x, y]