# -*- coding: utf-8 -*-
import SimpleDialog
import sys
import tkFileDialog

import os

import shutil
from lantools.tkinter import messagebox

import lantools

reload(sys)
sys.setdefaultencoding('utf-8')

mainwindow = SimpleDialog.Tk()
mainwindow.title("导出")
mainwindow.geometry('300x200')


def find_match_dir_list(path="", name=""):
    pathList = []
    for fpathe, dirs, files in os.walk(path):
        if not fpathe.endswith(name):
            continue
        inList = False
        for item in pathList:
            inList = fpathe.startswith(item)
            if inList:
                break
        if not inList:
            pathList.append(fpathe)
    return pathList


def hasSingleDir(path="", name=""):
    dir = str()
    for fpathe, dirs, files in os.walk(path):
        if not fpathe.endswith(name):
            continue
        if dir.__len__() == 0:
            dir = fpathe
        elif fpathe.startswith(dir):
            continue
        else:
            return "e"
    return dir


def android_out(pathList={}):
    toplevel = SimpleDialog.Toplevel()
    toplevel.title("Android导出")
    toplevel.geometry('250x100')
    SimpleDialog.Label(toplevel, text="请输入Android工程地址\n(DingtoneAndroid所在路径)").grid(row=0, column=0)
    key = SimpleDialog.StringVar()
    key.set("./DingtoneAndroid")
    entry = SimpleDialog.Entry(toplevel, textvariable=key)
    entry.grid(row=1, column=0)

    def checkDir(directory=str()):
        if directory.endswith("DingtoneAndroid"):
            return directory
        # list = find_match_dir_list(directory, "DingtoneAndroid")
        # if list.__len__() == 0:
        #     messagebox.showwarning("异常", "你选择的目录下不存在Android工程")
        #     return ""
        # elif list.__len__() > 1:
        #     messagebox.showwarning("异常", "你选择的目录下存在多个Android工程")
        #     return ""
        directory = hasSingleDir(directory, "DingtoneAndroid")
        if directory.__len__() == 0:
            messagebox.showwarning("异常", "你选择的目录下不存在Android工程")
            return ""
        elif directory.__len__() == 1:
            messagebox.showwarning("异常", "你选择的目录下存在多个Android工程")
            return ""
        return directory

    def choosePath():
        directory = checkDir(tkFileDialog.askdirectory())
        if directory.__len__() > 0:
            entry.delete(0, SimpleDialog.END)
            entry.insert(0, directory)

    SimpleDialog.Button(toplevel, text="选择路径", command=choosePath).grid(row=0, column=1)

    def copyfile():
        directory = checkDir(entry.get())
        if directory.__len__() == 0:
            return
        directory = directory + "/dingtone_lib/src/"
        for itemPath in pathList:
            cpPath = directory + itemPath.replace("Android/", "")
            if os.path.exists(cpPath):
                shutil.copyfile(itemPath, cpPath)
        toplevel.destroy()

    SimpleDialog.Button(toplevel, text="确定", command=copyfile).grid(row=2, column=0)
    pass


def ios_out(pathList={}):
    toplevel = SimpleDialog.Toplevel()
    toplevel.title("IOS导出")
    toplevel.geometry('250x100')
    SimpleDialog.Label(toplevel, text="请输入IOS工程地址\n(.git所在路径)").grid(row=0, column=0)
    key = SimpleDialog.StringVar()
    key.set("./.git")
    entry = SimpleDialog.Entry(toplevel, textvariable=key)
    entry.grid(row=1, column=0)

    def checkDir(directory=str()):
        if directory.endswith(".git"):
            return directory
        # list = find_match_dir_list(directory, ".git")
        # if list.__len__() == 0:
        #     messagebox.showwarning("异常", "你选择的目录下不存在.git")
        #     return ""
        # elif list.__len__() > 1:
        #     messagebox.showwarning("异常", "你选择的目录下存在多个.git")
        #     return ""
        directory = hasSingleDir(directory, ".git")
        if directory.__len__() == 0:
            messagebox.showwarning("异常", "你选择的目录下不存在.git")
            return ""
        elif directory.__len__() == 1:
            messagebox.showwarning("异常", "你选择的目录下存在多个.git")
            return ""
        return directory

    def choosePath():
        directory = checkDir(tkFileDialog.askdirectory())
        if directory.__len__() > 0:
            entry.delete(0, SimpleDialog.END)
            entry.insert(0, directory)

    SimpleDialog.Button(toplevel, text="选择路径", command=choosePath).grid(row=0, column=1)

    def copyfile():
        directory = checkDir(entry.get())
        if directory.__len__() == 0:
            return
        directory = directory.replace(".git", "Dingtone/IOS_Client/")
        for itemPath in pathList:
            dir = itemPath
            dir = dir.replace("IOS/Dingtone/", "PFIMCLient/resources/lang/")
            dir = dir.replace("IOS/TalkU/", "TalkURes/Localization/")
            dir = dir.replace("IOS/Telos/", "TelOSRes/Localization/")
            dir = dir.replace("IOS/WeFone/", "WeFoneRes/Localization/")
            cpPath = directory + dir
            if os.path.exists(cpPath):
                shutil.copyfile(itemPath, cpPath)
        toplevel.destroy()
        SimpleDialog.SimpleDialog(mainwindow, text="Success", buttons=["OK"], default=0).go()

    SimpleDialog.Button(toplevel, text="确定", command=copyfile).grid(row=2, column=0)
    pass


def androidOut():
    toplevel = SimpleDialog.Toplevel()
    toplevel.title("Android导出")
    toplevel.geometry('250x100')
    pathList = lantools.find_match_path_list("Android/", "strings.xml")
    transle = []
    local = []
    for itemPath in pathList:
        if itemPath.find("/values/") > -1 or itemPath.find("/values-zh/") > -1 or itemPath.find("/values-zh-rCN/") > -1:
            transle.append(itemPath)
        else:
            local.append(itemPath)

    def androidTransle():
        toplevel.destroy()
        android_out(transle)
        pass

    def androidLocal():
        toplevel.destroy()
        android_out(local)
        pass

    SimpleDialog.Button(toplevel, text="中英文翻译", command=androidTransle).pack()
    SimpleDialog.Button(toplevel, text="本地化翻译", command=androidLocal).pack()


def iosOut():
    toplevel = SimpleDialog.Toplevel()
    toplevel.title("IOS导出")
    toplevel.geometry('250x100')
    pathList = lantools.find_match_path_list("IOS", "Localizable.strings")
    transle = []
    local = []
    for itemPath in pathList:
        if itemPath.find("en.lproj") > -1 or itemPath.find("zh-Hans.lproj") > -1 or itemPath.find("zh-Hant.lproj") > -1:
            transle.append(itemPath)
        else:
            local.append(itemPath)

    def iosTransle():
        toplevel.destroy()
        ios_out(transle)
        pass

    def iosLocal():
        toplevel.destroy()
        ios_out(local)
        pass

    SimpleDialog.Button(toplevel, text="中英文翻译", command=iosTransle).pack()
    SimpleDialog.Button(toplevel, text="本地化翻译", command=iosLocal).pack()
    pass


SimpleDialog.Button(mainwindow, text="Android导出", command=androidOut).pack()
SimpleDialog.Button(mainwindow, text="IOS导出", command=iosOut).pack()

mainwindow.mainloop()
