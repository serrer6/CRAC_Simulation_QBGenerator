class Kind:
    def __init__(self,Version="v1.0.0.0",ID=1,CutOffScores=25,ExamDuration=40,QuestionAmount=30,KindName='A'):
        self.Version=Version
        self.ID=ID
        if(ID==1):
            self.KindName='A'
        elif(ID==2):
            self.KindName='B'
        elif(ID==3):
            self.KindName='C'
        else:
            raise Exception("Invalid level!", kd)
        self.CutOffScores=CutOffScores
        self.QuestionAmount=QuestionAmount
        self.ExamDuration=ExamDuration

class Que:
    def __init__(self,ID=0,InsertDt="1999-01-01 00:00:00",IsDelete=0,Option1="NULL",Option2="NULL",Option3="NULL",Option4="NULL",isMuit=0,Question="NULL",Answer=['A'],QuestionCode="QB0001",QuestionPic="",Remark="",UpdateDt=""):
        self.ID=ID
        self.InsertDt=InsertDt
        self.IsDelete=IsDelete
        self.Option1=Option1
        self.Option2=Option2
        self.Option3=Option3
        self.Option4=Option4
        self.Question=Question
        self.QuestionCode=QuestionCode
        self.QuestionPic=QuestionPic
        self.Remark=Remark
        self.UpdateDt=UpdateDt
        self.isMuit = isMuit
        self.Answer = Answer

    def LoadFromDict(self,dict):
        if "Portable" in dict:
            pass
        self = self.__init__(**dict)


class type:
    def __init__(self,ID=0,InsertDt="1999-01-01 00:00:00",IsDelete=0,KindID=1,TypeName="NULL",UpdateDt=""):
        self.ID=ID
        self.InsertDt=InsertDt
        self.IsDelete=IsDelete
        self.KindID=KindID
        self.TypeName=TypeName
        self.UpdateDt=UpdateDt

class typemapping:
    def __init__(self,ID=0,InsertDt="1999-01-01 00:00:00",IsDelete=0,TypeID=0,QuestionID=0,UpdateDt=""):
        self.ID=ID
        self.InsertDt=InsertDt
        self.IsDelete=IsDelete
        self.TypeID=TypeID
        self.QuestionID=QuestionID
        self.UpdateDt=UpdateDt
