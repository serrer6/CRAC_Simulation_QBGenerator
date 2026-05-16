import npyscreen
import sys
class _FileSelecterFrom(npyscreen.ActionForm):
    def create(self):
        self.name="File..."
        self.btn_Menu = self.add(npyscreen.TitleSelectOne,name="Please Select...",
                                        values=["Open CRAC QB  (*.bin)","Open Portable file (*.zip)"])
    def on_ok(self):
        
        print(self.btn_Menu.get_selected_objects())
    def on_cancel(self):
        self.parentApp.switchFormPrevious()
