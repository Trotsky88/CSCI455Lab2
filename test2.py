import tkinter as tk
from Maestro import Controller

MOTORS = 1
BODY = 2
TURN = 3
HEAD = 4
TILT = 0


class KeyControl():
    def __init__(self, win):
        self.root = win
        self.tango = Controller()
        self.body = 6000
        self.headTurn = 6000
        self.headTilt = 6000
        self.motors = 6000
        self.turn = 6000

    def upArrow(self, key):
        print(key.keycode)
        if key.keycode == 111:
            self.motors -= 200
            self.tango.setTarget(MOTORS, self.motors)
            if (self.motors > 7900):
                self.motors = 7900
            print(self.motors)

    def downArrow(self, key):
        print(key.keycode)
        if key.keycode == 116:
            self.motors += 200
            self.tango.setTarget(MOTORS, self.motors)
            if (self.motors < 5000):
                self.motors = 5000
            print(self.motors)

    def leftArrow(self, key):
        print(key.keycode)
        if key.keycode == 113:
            self.body += 200
            self.tango.setTarget(BODY, self.body)
            if (self.turn > 7900):
                self.turn = 7900
            print(self.turn)

    def rightArrow(self, key):
        print(key.keycode)
        if key.keycode == 114:
            self.body -= 200
            self.tango.setTarget(BODY, self.body)
            if (self.turn < 5000):
                self.turn = 5000
            print(self.turn)

    def qKey(self, key):
        print(key.keycode)
        if key.keycode == 24:
            self.turn += 200
            self.tango.setTarget(TURN, self.turn)
            if (self.motors > 7900):
                self.motors = 7900
            print(self.motors)

    def wKey(self, key):
        print(key.keycode)
        if key.keycode == 25:
            self.turn -= 200
            self.tango.setTarget(TURN, self.turn)
            if (self.motors > 7900):
                self.motors = 7900
            print(self.motors)

    def eKey(self, key):
        print(key.keycode)
        if key.keycode == 26:
            self.headTurn += 200
            self.tango.setTarget(HEAD, self.headTurn)
            if (self.motors > 7900):
                self.motors = 7900
            print(self.motors)

    def rKey(self, key):
        print(key.keycode)
        if key.keycode == 27:
            self.headTurn -= 200
            self.tango.setTarget(HEAD, self.headTurn)
            if (self.motors > 7900):
                self.motors = 7900
            print(self.motors)

    def aKey(self, key):
        print(key.keycode)
        if key.keycode == 38:
            self.headTilt += 200
            self.tango.setTarget(TILT, self.headTilt)
            if (self.motors > 7900):
                self.motors = 7900
            print(self.motors)

    def sKey(self, key):
        print(key.keycode)
        if key.keycode == 39:
            self.headTilt -= 200
            self.tango.setTarget(TILT, self.headTilt)
            if (self.motors > 7900):
                self.motors = 7900
            print(self.motors)

    def spaceKey(self, key):
        print(key.keycode)
        if key.keycode == 65:
            self.body = 6000
            self.headTurn = 6000
            self.headTilt = 6000
            self.motors = 6000
            self.turn = 6000
            self.tango.setTarget(MOTORS, self.motors)
            self.tango.setTarget(BODY, self.body)
            self.tango.setTarget(HEAD, self.headTurn)
            self.tango.setTarget(TILT, self.headTurn)
            self.tango.setTarget(TURN, self.headTurn)
            print(self.motors)

win = tk.Tk()
keys = KeyControl(win)
win.bind('<Up>', keys.upArrow)
win.bind('<Down>', keys.downArrow)
win.bind('<Left>', keys.leftArrow)
win.bind('<Right>', keys.rightArrow)
win.bind('<q>', keys.qKey)
win.bind('<w>', keys.wKey)
win.bind('<e>', keys.eKey)
win.bind('<r>', keys.rKey)
win.bind('<a>', keys.aKey)
win.bind('<s>', keys.sKey)
win.bind('<space>', keys.spaceKey)
win.mainloop()