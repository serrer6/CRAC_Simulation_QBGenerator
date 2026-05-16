import colorama
import time
from Generator.Convert import FConvent,BinConvent
from colorama import Fore,Back
import tui.FilePicker as FilePicker
import npyscreen
from tui._Main_Form import _MainFrom
from tui.FileMenu import _FileSelecterFrom
#from Generator.Asy import BinFile_Asy

print("""
   ______    ____     ___    ______          ____     ____    ______
  / ____/   / __ \   /   |  / ____/         / __ \   / __ )  / ____/
 / /       / /_/ /  / /| | / /             / / / /  / __  | / / __  
/ /___    / _, _/  / ___ |/ /___          / /_/ /  / /_/ / / /_/ /  
\____/   /_/ |_|  /_/  |_|\____/          \___\_\ /_____/  \____/   
                                                                    """)

def OutPutHeader(s):
    print(Fore.GREEN+"[INFO]"+Fore.WHITE+s)

import npyscreen

# 这里应用充当了 curses 初始化封装器的角色
# 同时也管理着应用的实际形态.

class Main(npyscreen.NPSAppManaged):
    def onStart(self):
        self.File1=""
        self.File2="."

        self.addForm("MAIN", _MainFrom)
        self.addForm("FileSelecter", _FileSelecterFrom)

if __name__ == '__main__':
    OutPutHeader("CopyRight BG4LGX-SourCheese GPL3")
    time.sleep(1.5)

    F = FConvent()
    F.LoadJSONToMem("G:\TEST\TEST.bin")
    ddd = BinConvent(F.Objects)
    FConvent.DictSaveToFile("G:\TEST\TEST2.bin",ddd.QB_Object.Export(),"bin")
    #TA = Main()
    #TA.run()
