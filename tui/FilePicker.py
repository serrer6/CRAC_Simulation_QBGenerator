import tkinter as tk
from tkinter import filedialog

def Get_FolderPath():
    root = tk.Tk()
    root.withdraw()
    FolderPath=filedialog.askdirectory()
    root.destroy()
    return FolderPath

def Get_FilePath():
    root = tk.Tk()
    root.withdraw()
    FilePath=filedialog.askopenfilename()
    root.destroy()
    return FilePath
