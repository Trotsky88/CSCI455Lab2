import tkinter as tk
from Maestro import Controller

MOTORS = 1


class KeyControl():
    def __init__(self,win):
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
            self.motors += 200
            self.tango.setTarget(MOTORS, self.motors)
            if(self.motors > 7900):
                self.motors = 7900
            print(self.motors)

    def downArrow(self, key):
        print(key.keycode)
        if key.keycode == 40:
            self.motors -= 200
            if(self.motors < 5000):
                self.motors = 5000
            print(self.motors)

    def leftArrow(self, key):
        print(key.keycode)
        if key.keycode == 37:
            self.turn += 200
            if(self.turn > 7900):
                self.turn = 7900
            print(self.turn)

    def rightArrow(self, key):
        print(key.keycode)
        if key.keycode == 39:
            self.turn -= 200
            if(self.turn < 5000):
                self.turn = 5000
            print(self.turn)

    def qKey(self, key):
        print(key.keycode)
        if key.keycode == 81:
            self.motors += 200
            if(self.motors > 7900):
                self.motors = 7900
            print(self.motors)

    def wKey(self, key):
        print(key.keycode)
        if key.keycode == 87:
            self.motors += 200
            if(self.motors > 7900):
                self.motors = 7900
            print(self.motors)

    def eKey(self, key):
        print(key.keycode)
        if key.keycode == 69:
            self.motors += 200
            if(self.motors > 7900):
                self.motors = 7900
            print(self.motors)

    def rKey(self, key):
        print(key.keycode)
        if key.keycode == 82:
            self.motors += 200
            if(self.motors > 7900):
                self.motors = 7900
            print(self.motors)

    def aKey(self, key):
        print(key.keycode)
        if key.keycode == 65:
            self.motors += 200
            if(self.motors > 7900):
                self.motors = 7900
            print(self.motors)

    def sKey(self, key):
        print(key.keycode)
        if key.keycode == 83:
            self.motors += 200
            if(self.motors > 7900):
                self.motors = 7900
            print(self.motors)

win = tk.Tk()
keys = KeyControl(win)
win.bind('<Up>', keys.upArrow)
win.bind('<Down>', keys.downArrow)
win.bind('<Left>', keys.leftArrow)
win.bind('<Right>', keys.rightArrow)
win.bind('<Q>', keys.qKey)
win.bind('<W>', keys.wKey)
win.bind('<E>', keys.eKey)
win.bind('<R>', keys.rKey)
win.bind('<A>', keys.aKey)
win.bind('<S>', keys.sKey)
win.mainloop()
