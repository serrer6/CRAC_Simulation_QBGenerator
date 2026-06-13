from Generator.Que_Object import Que
from PIL import Image, ImageDraw, ImageFont
import platform
import os
import random
import itertools
from app import current_path

def get_chinese_font(size=32):
    """自动获取系统中文字体"""
    system = platform.system()
    
    font_paths = {
        'Windows': [
            "C:/Windows/Fonts/simhei.ttf",    # 黑体
            "C:/Windows/Fonts/msyh.ttc",      # 微软雅黑
            "C:/Windows/Fonts/simkai.ttf",    # 楷体
        ],
        'Darwin': [  # macOS
            "/System/Library/Fonts/PingFang.ttc",
            "/System/Library/Fonts/STHeiti Light.ttc",
            "/Library/Fonts/Arial Unicode.ttf",
        ],
        'Linux': [
            "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
            "/usr/share/fonts/opentype/wqy/WenQuanYiZenHei.otf",
            "/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc",
        ]
    }
    
    for font_path in font_paths.get(system, []):
        if os.path.exists(font_path):
            return ImageFont.truetype(font_path, size)
    
    # 默认字体（无中文）
    return ImageFont.load_default()

def GetKindId(code: str):
    part = code.split("MC")[-1]
    num_str = part.split("-")[0]
    return int(num_str)

def clean_tag(j_text: str) -> str:
    split_chars = ["、", ","]
    for c in split_chars:
        if c in j_text:
            return j_text.split(c)[0].strip()
    return j_text.strip()

def CreateQueImage(Question : Que) -> Image:
    img = Image.new("RGB",(1920,180),color=(255,255,255))
    draw = ImageDraw.Draw(img)

    font = get_chinese_font(27)
    strs = "问："+Question.Question+"\nA："+Question.Option1+"\nB："+Question.Option2+"\nC："+Question.Option3+"\nD："+Question.Option4
    draw.text((20,20),strs,fill="black",font=font)
    path = current_path + '\\temp\\'+Question.QuestionCode+'_Que.jpg'
    img = img.convert("RGB")
    img.save(path,quality=100, subsampling=0)
    return path


def parse_single_question(q_str: str) -> dict:
    """
    传入单题完整字符串（自行分割好的单题文本），解析为题目字典
    :param q_str: 单个题目的完整文本字符串
    :return: 题目字典
    """
    # 分行并过滤空行
    lines = [line.strip() for line in q_str.splitlines()]
    content_lines = [ln for ln in lines if ln]

    q_data = {
        "ID": None,
        #"P": "",
        #"I": "",
        "Option1":"NULL",
        "Option2":"NULL",
        "Option3":"NULL",
        "Option4":"NULL",
        "Question": "NULL",
        "QuestionCode":"",
        "Answer": []
    }
    t_data = {
        "KindID":1,
        "TypeName":"",
        "IsDelete":0,
    }

    for line in content_lines:
        if line.startswith('[J]'):
            q_data["QuestionCode"] = clean_tag(line.replace("[J]", ""))
        elif line.startswith('[P]'):
            t_data["TypeName"] = line.replace("[P]", "")
        elif line.startswith('[I]'):
            t_data["KindID"] = GetKindId(line.replace("[I]", ""))
        elif line.startswith('[Q]'):
            q_data["Question"] = line.replace("[Q]", "")
        elif line.startswith('[T]'):
            temp = line.replace("[T]", "")
            for char in temp:
                q_data["Answer"].append(char)
        elif line.startswith(('[A]', '[B]', '[C]', '[D]')):
            if line[1]=='A':
                q_data["Option1"] = line[3:]
            elif line[1]=='B':
                q_data["Option2"] = line[3:]
            elif line[1]=='C':
                q_data["Option3"] = line[3:]
            else:
                q_data["Option4"] = line[3:]
    if len(q_data["Answer"]) > 1:
        q_data["isMuit"]=1

    return q_data,t_data


def generate_three_unique_wrong(correct):
    base = ['A','B','C','D']
    pool = []
    for length in range(2, 5):
        for combo in itertools.combinations(base, length):
            txt = ''.join(combo)
            if txt != correct:
                pool.append(txt)
    random.shuffle(pool)
    # 取前3个，数量足够就不重复
    res = pool[:3]
    # 不够长度时重复最后一个补齐3位
    while len(res) < 3:
        res.append(res[-1])
    return res
#os.path.isfile(path)
def MuitAnswerGen(Question : Que):
    

    Ans_len = len(Question.Answer)
    if Ans_len > 1:
        Question.QuestionPic = CreateQueImage(Question=Question)
        Question.Option1=""
        Question.Option2=""
        Question.Option3=""
        Question.Option4=""
        for char in Question.Answer:
            Question.Option1+=char
        AnsList = generate_three_unique_wrong(Question.Option1)
        Question.Option2=AnsList[0]
        Question.Option3=AnsList[1]
        Question.Option4=AnsList[2]
        #Question.Answer=
    
    return Question

def remove_all_files_with_suffix(filepath, suffixes=('.jpg',)):
    """
    删除指定目录下所有以特定后缀名结尾的文件。
    参数:
        filepath (str): 目标目录路径。
        suffixes (tuple): 要删除的文件后缀名列表，默认为 ('.x', '.X', '.X1')。
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            for suffix in suffixes:
                if file_path.endswith(suffix):
                    try:
                        os.remove(file_path)
                        print(f"已删除文件: {file_path}")
                    except PermissionError:
                        print(f"没有权限删除文件: {file_path}")
                    except Exception as e:
                        print(f"删除文件时出错: {e}")
                    break  # 匹配到一个后缀名即可，无需继续检查
