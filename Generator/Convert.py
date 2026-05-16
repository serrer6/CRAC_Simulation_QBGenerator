import base64
import json
from Generator.Asy import QB_Asy
from Generator.Que_Object import Kind,Que,type,typemapping

class FConvent:
    def __init__(self):
        self.Objects={}

    def ToBase64(infile, outfile):
        with open(infile,"r") as InputFile:
            ori_file = InputFile.read()
            b64_data = base64.b64encode(ori_file)
            b64_file = open(outfile,"w")
            b64_file.write(b64_data.decode())
            b64_file.close()
        InputFile.close()

    def ToJSON(infile, outfile):
        with open(infile,"r") as InputFile:
            b64_data = InputFile.read()
            ori_data = base64.b64decode(b64_data)
            ori_file  = open(outfile,"w")
            ori_file.write(ori_data.decode())
            ori_file.close
        InputFile.close()
    #将文件加载后载入内存
    def LoadJSONToMem(self,infile,):
        with open(infile,"r") as InputFile:
            b64_data = InputFile.read()
            ori_data = base64.b64decode(b64_data)
            self.Objects=ori_data.decode()
        InputFile.close()
    
    def DictSaveToFile(outfile,dict,type):
        with open(outfile,"w",encoding="utf-8") as OutputFile:
            if type == "json":
                OutputFile.write(json.dumps(dict,ensure_ascii=False))
            elif type == "bin":
                jsonstr = json.dumps(dict,ensure_ascii=False)
                OutputFile.write(base64.b64encode(jsonstr.encode()).decode())

    #垃圾回收
    def GC(self):
        self.Objects=None

class BinConvent:
    def __init__(self,obj={}):
        self.QB_Object = QB_Asy(check_pass=1)
        BinDict = json.loads(obj)
        for que in BinDict["Question"]:
            self.QB_Object.add("question",Que(**que))
        for kd in BinDict["Kind"]:
            self.QB_Object.add("kind",Kind(**kd))
        for tp in BinDict["Type"]:
            self.QB_Object.add("type",type(**tp))
        for tm in BinDict["TypeMapping"]:
            self.QB_Object.add("mapping",typemapping(**tm))
