import tkinter as tk
from tkinter import filedialog, Text, Entry
import os
import subprocess
import commands as cmd

window = tk.Tk()
#canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
#canvas.pack()

importedPowerPlanPath = ""

#Declared Commands
def installPowerPlanCommand():
    global importedPowerPlanPath
    cmd.installPowerPlan(importedPowerPlanPath)
    importedPowerPlanPath = ""          # clears variable for next use


def importPowerPlanCommand():
    global importedPowerPlanPath
    importedPowerPlanPath = cmd.importPowerPlan()               # function returns the file path of the imported power plan
    if isinstance(importedPowerPlanPath, str):
        cmd.setImportFlag(True)
        print("PATH = " + importedPowerPlanPath)


def setPowerPlan75Command():
    cmd.setPowerPlan75()


def setPowerPlan100Command():
    cmd.setPowerPlan100()

#Widgets

display = Entry()

installPowerPlanButton = tk.Button(window, text="Install power plan", padx=10, pady=5, fg="white", bg="gray", command=installPowerPlanCommand)
installPowerPlanButton.place(x=80, y=10)

importPowerPlanButton = tk.Button(window, text="Import power plan", padx=10, pady=5, fg="white", bg="gray", command=importPowerPlanCommand)
importPowerPlanButton.place(x=80, y=50)

exportPowerPlanButton = tk.Button(window, text="Export power plan", padx=10, pady=5, fg="white", bg="gray")
exportPowerPlanButton.place(x=80, y=90)

set75PlanButton = tk.Button(window, text="Set power plan = 75", padx=10, pady=5, fg="white", bg="gray", command=setPowerPlan75Command)
set75PlanButton.place(x=80, y=130)

set100PlanButton = tk.Button(window, text="Set power plan = 100", padx=10, pady=5, fg="white", bg="gray", command=setPowerPlan100Command)
set100PlanButton.place(x=80, y=170)

#Functions

"""def installPowerPlan():
    global importedPowerPlanPath

    if importedPowerPlanPath == "":
        errorMessage = "Please import a power plan and try again"
        print(errorMessage)
    
    elif os.path.isfile(importedPowerPlanPath):
        errorMessage = "Please insert a valid file path"
        print(errorMessage)
    
    elif not importedPowerPlanPath.endswith(".pow"):
        errorMessage = "Please insert a .pow file"
        print(errorMessage)

    else:
        subprocess.call([importedPowerPlanPath])
        importedPowerPlanPath = ""
"""

window.geometry("300x300")
window.mainloop()