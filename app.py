import colorama
import time
from Generator.Convert import FConvent,BinConvent,ConventImgtoBase64
from Generator.Asy import QB_Asy
from Generator.Que_Object import Kind,Que,type,typemapping
from Generator.Question import *
from colorama import Fore,Back
import tui.FilePicker as FilePicker
import npyscreen
from tui._Main_Form import _MainFrom
from tui.FileMenu import _FileSelecterFrom
import copy

import os
current_path = os.path.dirname(os.path.abspath(__file__))
timestamp = time.time()
local_time = time.localtime(timestamp)
app_local_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
#from Generator.Asy import BinFile_Asy

NEW_STEP = 0

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
    #File1="."
    #File2="."
    #mode=None

    def onStart(self):
        self.File1="."
        self.File2="."
        self.mode=None
        self.addForm("MAIN", _MainFrom)
        self.addForm("FileSelecter", _FileSelecterFrom)

if __name__ == '__main__':
    QB=QB_Asy(version="V4.0.0.1")

     #定义Kind
    AL=Kind(Version="V4.0.0.1",CutOffScores=30,QuestionAmount=40,ExamDuration=40)
    BL=Kind(Version="V4.0.0.1",ID=2,CutOffScores=45,QuestionAmount=60,ExamDuration=60)
    CL=Kind(Version="V4.0.0.1",ID=3,CutOffScores=70,QuestionAmount=90,ExamDuration=90)

    QB.add(AL)
    QB.add(BL)
    QB.add(CL)


    with open("tk2.txt","r",encoding="utf-8") as f:
        txt=f.read()
        data_list=txt.split("\n\n")
        que_dist=[]
        type_list=[]
        for ln in data_list:
            rquestion,rtype=parse_single_question(ln)
            OutputQustion = MuitAnswerGen(Que(**rquestion))
            que_dist.append(OutputQustion)
            type_list.append(type(**rtype))
        for ln in range(len(que_dist)):
            if que_dist[ln].QuestionCode=="LX":
                NEW_STEP+=1
                que_dist[ln].QuestionCode=f"LX{NEW_STEP:04d}"

            if os.path.isfile(que_dist[ln].QuestionPic):
                que_dist[ln].QuestionPic  = ConventImgtoBase64(que_dist[ln].QuestionPic)
                #que_dist[ln].QuestionPic=""
            que_dist[ln].ID=ln+1
            QB.AddQuestionToQB(copy.deepcopy(que_dist[ln]),Type=copy.deepcopy(type_list[ln]))

    #FConvent.DictSaveToFile("G:\TEST\TEST.json",QB.Export(),"json")
    FConvent.DictSaveToFile("G:\TEST\TEST.bin",QB.Export(),"bin")
       

    print("clear TEMP")
    remove_all_files_with_suffix("temp", suffixes=('.jpg',))


    #OutPutHeader("CopyRight BG4LGX-SourCheese GPL3")
    #time.sleep(1.5)
    #FConvent.DictSaveToFile("G:\TEST\TEST2.json",ddd.QB_Object.Export(),"json")
    #TA = Main()
    #TA.run()
