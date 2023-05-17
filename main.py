from socket import *
import struct,math,numpy as np
from PySide2.QtWidgets import QApplication,QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from threading import*
from PySide2.QtGui import  QIcon
import ctypes
import Pt29and33 as _Pt2933


class MG400_Control():
    def __init__(self):
        URC_ui = QFile("mg400_ctrl.ui")#打开ui文件
        URC_ui.open(QFile.ReadOnly)
        URC_ui.close()
        self.ui = QUiLoader().load(URC_ui)

# '29999端口功能'         
        self.ui.EnableRobot.clicked.connect(self.EnableRobot)
        self.ui.DisableRobot.clicked.connect(self.DisableRobot)
        self.ui.EmergencyStop.clicked.connect(self.EmergencyStop)
        self.ui.PowerOn.clicked.connect(self.PowerOn)
        self.ui.StartDrag.clicked.connect(self.StartDrag)
        self.ui.StopDrag.clicked.connect(self.StopDrag)
        self.ui.speedSet.clicked.connect(self.speed)
        self.ui.SpeedFactor.clicked.connect(self.SpeedFactor)
        self.ui.RunScript.clicked.connect(self.RunScript)
        self.ui.PauseScript.clicked.connect(self.PauseScript)
        self.ui.ContinueScript.clicked.connect(self.ContinueScript)
        self.ui.StopScript.clicked.connect(self.StopScript)
        self.ui.ClearError.clicked.connect(self.ClearError)
        self.ui.RobotMode.clicked.connect(self.RobotMode)
        self.ui.GetErrorID.clicked.connect(self.GetErrorID)

# '30003端口功能' 
        self.ui.Xforward.pressed.connect(self.Xforward)
        self.ui.Yforward.pressed.connect(self.Yforward)
        self.ui.Zforward.pressed.connect(self.Zforward)
        self.ui.Xnegative.pressed.connect(self.Xnegative)
        self.ui.Ynegative.pressed.connect(self.Ynegative)
        self.ui.Znegative.pressed.connect(self.Znegative)
        self.ui.Xforward.released.connect(self.StopJog)
        self.ui.Xnegative.released.connect(self.StopJog)
        self.ui.Yforward.released.connect(self.StopJog)
        self.ui.Ynegative.released.connect(self.StopJog)
        self.ui.Zforward.released.connect(self.StopJog)
        self.ui.Znegative.released.connect(self.StopJog)
        self.ui.PutIntoBox.pressed.connect(self.PutIntoBox)
        self.ui.PutIntoBox.released.connect(self.ResetRobot)

    def Roboip(self):
        Dobot=_Pt2933.Pt2933(f"{self.ui.ip.text()}")
        return Dobot
    
# '29999端口功能'     
    def EnableRobot(self,Dobot):
        Dobot=MG400_Control.Roboip(self)
        Dobot.Dashboard('EnableRobot()')

    def DisableRobot(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.Dashboard('DisableRobot()')
        
    def PowerOn(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.Dashboard('PowerOn()')

    def EmergencyStop(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.Dashboard('EmergencyStop()')

    def ClearError(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.Dashboard('ClearError()')

    def StartDrag(self):
        self.Dobot.Dashboard('StartDrag()')

    def StopDrag(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.Dashboard('StopDrag()')

    def speed(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.Dashboard(f'SpeedL({self.ui.Speed.text()})')
        Dobot.Dashboard(f'SpeedJ({self.ui.Speed.text()})')

    def SpeedFactor(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.Dashboard(f'SpeedJ({self.ui.TxSpeedFactor.text()})')
        
    def RunScript(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.Dashboard(f'RunScript({self.ui.ScriptName.text()})')
        
    def PauseScript(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.Dashboard('PauseScript()')

    def ContinueScript(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.Dashboard('ContinueScript()')

    def StopScript(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.Dashboard('StopScript()')

    def Stop(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.Dashboard('Stop()')

    def ResetRobot(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.Dashboard('ResetRobot()')

    def RobotMode(self):
        Dobot=MG400_Control.Roboip(self)
        info=Dobot.Dashboard('RobotMode()')
        if info[0] != '0':
            self.ui.RoboMode.setText('fail to get')
        else: 
            start=info.find('{')
            end=info.find('}')
            if (end-start) ==2:
                Modecode=info[3]
            elif (end-start)==3:
                Modecode=info[3]+info[4]
            dic={'1':'初始化','2':'抱闸松开','3':'保留位',
                 '4':'未使能','5':'使能','6':'拖拽','7':'程序运行',
                 '8':'拖拽录制','9':'报警','10':'暂停状态','11':'点动'}
            self.ui.RoboMode.setText(dic[Modecode])

    def GetErrorID(self):
        Dobot=MG400_Control.Roboip(self)
        info=Dobot.Dashboard('GetErrorID()')
        print(info)
        self.ui.ErrorID.setText(info[0])


# '30003端口功能' 
    def Xforward(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.ScriptPort('MoveJog(X+)')

    def Yforward(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.ScriptPort('MoveJog(Y+)')

    def Zforward(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.ScriptPort('MoveJog(Z+)')


    def Xnegative(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.ScriptPort('MoveJog(X-)')

    def Ynegative(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.ScriptPort('MoveJog(Y-)')

    def Znegative(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.ScriptPort('MoveJog(Z-)')

    def StopJog(self):
        Dobot=MG400_Control.Roboip(self)
        Dobot.ScriptPort('MoveJog(stop)')

    def PutIntoBox(self):
        QMessageBox.information(self.ui,"信息","debug中")
        # self.Dobot.ScriptPort('MovJ(-172.490692,-623.993286,447.865204,173.569107,8.778808,72.281548,AccJ=20)')
    # def PutIntoBox(self):
    #     self.Dobot.ScriptPort('JointMovJ(265,10,120,27,90,114,SpeedJ=10,AccJ=200)')


app =QApplication([])
URCgui = MG400_Control()
URCgui.ui.show()
app.exec_()