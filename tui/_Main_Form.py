import npyscreen
from tui.ExitButton import ExitButton

class _MainFrom(npyscreen.Form):
    def create(self):
        self.min_c=40
        self.min_l=80
        self.name = "CRAC QBG"
        self.text_FileSelected = self.add(npyscreen.FixedText,name="Wait...")
        self.btn_FileButton = self.add(npyscreen.ButtonPress,name="File...", when_pressed_function=self.File_Menu)
        self.btn_ExitButton = self.add(ExitButton,name="Exit")

    def File_Menu(self):
        self.parentApp.switchForm("FileSelecter")

    def on_cancel(self):
        self.parentApp.switchForm(None)
