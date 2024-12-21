#***************************************************************************
#*    Copyright (C) 2023 
#*    This library is free software
#***************************************************************************
import inspect
import os
import sys
import FreeCAD
import FreeCADGui

class cutGateHopperShowCommand:
    def GetResources(self):
        file_path = inspect.getfile(inspect.currentframe())
        module_path=os.path.dirname(file_path)
        return { 
          'Pixmap': os.path.join(module_path, "icons", "cutGateHopper.svg"),
          'MenuText': "cutGateHopper",
          'ToolTip': "Show/Hide cutGateHopper"}

    def IsActive(self):
        import cutGateAssy
        cutGateAssy
        return True

    def Activated(self):
        try:
          import cutGateAssy
          cutGateAssy.main.d.show()
        except Exception as e:
          FreeCAD.Console.PrintError(str(e) + "\n")

    def IsActive(self):
        import cutGateAssy
        return not FreeCAD.ActiveDocument is None

class cutGateAssy(FreeCADGui.Workbench):
    def __init__(self):
        file_path = inspect.getfile(inspect.currentframe())
        module_path=os.path.dirname(file_path)
        self.__class__.Icon = os.path.join(module_path, "icons", "cutGateHopper.svg")
        self.__class__.MenuText = "cutGateHopper"
        self.__class__.ToolTip = "cutGateHopper by Pascal"

    def Initialize(self):
        self.commandList = ["cutGateHopper_Show"]
        self.appendToolbar("&cutGateHopper", self.commandList)
        self.appendMenu("&cutGateHopper", self.commandList)

    def Activated(self):
        import cutGateAssy
        cutGateAssy
        return

    def Deactivated(self):
        return

    def ContextMenu(self, recipient):
        return

    def GetClassName(self): 
        return "Gui::PythonWorkbench"
FreeCADGui.addWorkbench(cutGateAssy())
FreeCADGui.addCommand("cutGateHopper_Show", cutGateHopperShowCommand())

