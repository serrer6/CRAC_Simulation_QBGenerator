import json
import time
#from Generator.Convert import FConvent
from Generator.Que_Object import Kind,Que,type,typemapping

class QB_Asy:
    def __init__(self,check_pass=0,version:str | None=None):
        self.Kind = []
        self.Question = []
        self.Type = []
        self.TypeMapping = []
        self.checkpass = check_pass
        self.version = "v1.0.0.0"
        if version:
            self.version = version
        #metadata
        self.meta_LastKindID = 0
        self.meta_LastQuestionID = 0
        self.meta_LastTypeID = 0
        self.meta_LastTypeMappinID = 0

    def add(self,value:object):
        #将题目对象载入题库
        if value.__type__ == "kind":
            if self.meta_LastKindID < value.ID: self.meta_LastKindID = value.ID
            self.Kind.append(value)
        elif value.__type__ == "question":
            if self.meta_LastQuestionID < value.ID: self.meta_LastQuestionID = value.ID
            self.Question.append(value)
            if self.meta_LastTypeID < value.ID: self.meta_LastTypeID = value.ID
        elif value.__type__ == "type":
            self.Type.append(value)
            if self.meta_LastTypeMappinID < value.ID: self.meta_LastTypeMappinID = value.ID
        elif value.__type__ == "typemapping":
            self.TypeMapping.append(value)
        else:
            #返回错误
            raise Exception("Invalid level!", name)
    def Check(self,value):
        if(self.checkpass == 1):return value
        if value.__type__ == "kind":
            if value["ExamDuration"] > 0 and  value["QuestionAmount"] > value["CutOffScores"]:
                # and value["QuestionAmount"]<=len(self.Question)
                return 1
        elif value.__type__ == "question":
            pass
        elif value.__type__ == "type":
            pass
        elif value.__type__ == "typemapping":
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
        self2dict = self.__dict__
        for i in self2dict["Kind"]:
            i=i.__dict__
            del i["__type__"]
            Export_dict["Kind"].append(i)
        for i in self2dict["Question"]:
            ExpQuestion = i.__dict__
            if len(ExpQuestion["Answer"]) <= 1 and ExpQuestion["isMuit"] == 0:
                del ExpQuestion["Answer"]
                del ExpQuestion["isMuit"]
            del ExpQuestion["__type__"]
            Export_dict["Question"].append(ExpQuestion)
        for i in self2dict["Type"]:
            i=i.__dict__
            del i["__type__"]
            Export_dict["Type"].append(i)
        for i in self2dict["TypeMapping"]:
            i=i.__dict__
            del i["__type__"]
            Export_dict["TypeMapping"].append(i)
        return Export_dict
    
    def AddQuestionToQB(self,que:Que,kind:Kind | None=None,Type:type | None=None) -> None:
        if not kind: _kind = Kind(self.version)
        else:_kind = kind
        timestamp = time.time()
        local_time = time.localtime(timestamp)
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        if not Type:
            _type = type(ID=self.meta_LastTypeID+1,InsertDt=time_str,KindID=_kind.ID,TypeName="CRACQBG_AUTO")
            self.meta_LastTypeID += 1
        else: _type = Type

        _typemapping = typemapping(self.meta_LastTypeMappinID+1,InsertDt=time_str,TypeID=_type.ID,QuestionID=que.ID,UpdateDt=time_str)
        self.meta_LastTypeMappinID+=1
        self.add(que)
        self.add(_type)
        self.add(_typemapping)

        


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
