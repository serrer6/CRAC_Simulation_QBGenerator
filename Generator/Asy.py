import json
#from Generator.Convert import FConvent
from Generator.Que_Object import Kind,Que,type,typemapping

class QB_Asy:
    def __init__(self,check_pass=0):
        self.Kind = []
        self.Question = []
        self.Type = []
        self.TypeMapping = []
        self.checkpass = check_pass

    def add(self,name,value):
        #将题目对象载入题库
        if name == "kind":
            self.Kind.append(value)
        elif name == "question":
            self.Question.append(value)
        elif name == "type":
            self.Type.append(value)
        elif name == "mapping":
            self.TypeMapping.append(value)
        else:
            #返回错误
            raise Exception("Invalid level!", name)
    def Check(self,name,value):
        if(self.checkpass == 1):return value
        if name == "kind":
            if value["ExamDuration"] > 0 and  value["QuestionAmount"] > value["CutOffScores"] and value["QuestionAmount"]<=len(self.Question):
                return value
            else:
                raise Exception("Invalid level!", value)
        elif name == "question":
            pass
        elif name == "type":
            pass
        elif name == "mapping":
            pass
        else:
            #返回错误
            raise Exception("Invalid level!", name)

    def Export(self,isPortable=0):
        Export_dict = {}
        Export_dict["Kind"]=[]
        Export_dict["Question"]=[]
        Export_dict["Type"]=[]
        Export_dict["TypeMapping"]=[]
        for i in self.__dict__["Kind"]:
            Export_dict["Kind"].append(i.__dict__)
        for i in self.__dict__["Question"]:
            ExpQuestion = i.__dict__
            if len(ExpQuestion["Answer"]) <= 1 and ExpQuestion["isMuit"] == 0:
                del ExpQuestion["Answer"]
                del ExpQuestion["isMuit"]
                Export_dict["Question"].append(ExpQuestion)
        for i in self.__dict__["Type"]:
            Export_dict["Type"].append(i.__dict__)
        for i in self.__dict__["TypeMapping"]:
            Export_dict["TypeMapping"].append(i.__dict__)
        return Export_dict

'''class BinFile_Asy:
    def __init__(self,Obj:FConvent):
        self.QBASY = QB_Asy()
        self.Obj = Obj
    def load(self):
        #题库转换成字典
        BinDict = json.loads(self.Obj.Objects)
        #载入题库对象
        for kind in BinDict["Kind"]:

            self.QBASY.add("kind",kind)
        #返回题库对象
        return self.QBASY

class PortableFile_Asy:
    pass'''
