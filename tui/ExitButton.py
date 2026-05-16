import npyscreen
import sys

class ExitButton(npyscreen.ButtonPress):
    def whenPressed(self):
        sys.exit(0)
