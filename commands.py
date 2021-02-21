"""Commands to be used by the buttons in power_plans_app.py"""

import tkinter as tk
from tkinter import filedialog, Text, Entry
import os
import subprocess
import re


def installPowerPlan(path):
    if path == "":
        errorMessage = "Please import a power plan and try again"
        print(errorMessage)
    
    elif not os.path.isfile(path):
        errorMessage = "Please insert a valid file path"
        print(errorMessage)
    
    elif not path.endswith(".pow"):
        errorMessage = "Please insert a .pow file"
        print(errorMessage)

    else:
        os.system(r".\\install.bat")


def importPowerPlan():
    file = open("data.txt", "r+")
    importFlag = file.readline()

    if isDataCorrupted(importFlag):
        return

    file.close()

    return filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=((".pow", "*.pow"),))      # returns file path


def setPowerPlan75():
    fileName = open("data.txt", "r+")
    importFlag = fileName.readline()
    
    if isDataCorrupted(importFlag):
        return

    elif not isPowerPlanImported(importFlag):
        return
    
    else:
        os.system(r".\\setPowerPlan75.bat")
        print("Power Scheme set successfully")

    fileName.close()


def setPowerPlan100():
    fileName = open("data.txt", "r+")
    importFlag = fileName.readline()
    
    if isDataCorrupted(importFlag):
        return

    elif not isPowerPlanImported(importFlag):
        return

    else:
        os.system(r".\\setPowerPlan100.bat")
        print("Power Scheme set successfully")

    fileName.close()


def isDataCorrupted(importFlag):
    matched = re.match("IMPORTED=[True, False]", importFlag)    # verifies importFlag's string format    
  
    if not bool(matched):
        errorMessage = "Error: data corrupted. Check file integrity"
        print(errorMessage)
        return True

    else:
        return False


def isPowerPlanImported(importFlag):
    if "False" in importFlag:
        errorMessage = "Error: custom power plan was not imported"
        print(errorMessage)
        return False
    else:
        return True


def setImportFlag(boolean):

    # Read in the file
    with open('data.txt', 'r') as file :
        importFlag = file.readline()

    value = boolean
    
    # Replace the target string
    importFlag = importFlag.split("=")
    importFlag[-1] = str(value)
    importFlag = "=".join(importFlag)
    print("string: " + importFlag)

    # Write the file out again
    with open('data.txt', 'w') as file:
        file.write(importFlag)
