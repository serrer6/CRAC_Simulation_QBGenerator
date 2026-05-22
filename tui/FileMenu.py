import npyscreen
import sys
class _FileSelecterFrom(npyscreen.ActionForm):
    def create(self):
        self.add(npyscreen.FixedText,name="Open")
        self.add(npyscreen.Button,name="Open Simulation QB File(*.bin)")
        self.add(npyscreen.Button,name="Open Simulation QB File(*.bin)")
    def on_ok(self):
        self.parentApp.switchFormPrevious()
    def on_cancel(self):
        self.parentApp.switchFormPrevious()
