import colorama
import time
from Generator.Convert import FConvent,BinConvent
from Generator.Asy import QB_Asy
from Generator.Que_Object import Kind,Que,type,typemapping
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

    #F = FConvent()
    #F.LoadJSONToMem("G:\TEST\TEST.bin")
    #ddd = BinConvent(F.Objects)
    QBASY = QB_Asy(version="V3.2.2.2")
    QBASY.add(Kind())
    QBASY.add(Kind(ID=2))
    QBASY.add(Kind(ID=3))
    QBASY.AddQuestionToQB(Que())
    QBASY.AddQuestionToQB(Que(QuestionCode="QB0002",ID=2))
    FConvent.DictSaveToFile("G:\TEST\TEST2.json",QBASY.Export(),"json")
    #TA = Main()
    #TA.run()
