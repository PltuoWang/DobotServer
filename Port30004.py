import socket
import struct

# 解析地址:https://github.com/Dobot-Arm/TCP-IP-Protocol
#          author：王海峰 plutohfw@gmail.com
#          创建时间:   2023/4/21    
#          最后维护时间:2023/4/21
#          注意：30004的realtime服务需要注意接收字长，字典里"MessageSize""的值

class Dobot30004():
    def __init__(self,ip) :
        self.HOST = ip   # Dobot ip
        self.PORT = 30004       # 30004 Ser Port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def realtime(self,Meaning):
        self.s.connect((self.HOST, self.PORT))
        dic= {'MessageSize': 'h','reserved':'3h','DigitalInputs':'q','DigitalOutputs':'q','RobotMode':'q','TimeStamp':'q','reserved2':'q',
            'TestValue':'q','reserved3':'q','SpeedScaling':'d','LinearMomentumNorm':'d','VMain':'d','VRobot':'d','IRobot':'d','reserved4':'d',
            'reserved5':'d','ToolAcceleroMeter':'3d','ElbowPosition':'3d','ElbowVelocity':'3d','QTarget':'6d','QDTarget':'6d','QDDTarget':'6d','ITarget':'6d',
            'MTarget':'6d','QActual':'6d','QDActual':'6d','IActual':'6d','ActualTCPForce':'6d','ToolVectorActual':'6d','TCPSpeedActual':'6d',
            'TCPForce':'6d','ToolVectorTarget':'6d','TCPSpeedTarget':'6d','MotorTemperatures':'6d','JointModes':'6d','VActual':'6d','HandType':'4c',
            'User':'c','Tool':'c','RunQueuedCmd':'c','PauseCmdFlag':'c','VelocityRatio':'c','AccelerationRatio':'c','JerkRatio':'c','XYZVelocityRatio':'c',
            'RVelocityRatio':'c','XYZAccelerationRatio':'c','RAccelerationRatio':'c','XYZJerkRatio':'c','RJerkRatio':'c','BrakeStatus':'c','EnableStatus':'c','DragStatus':'c',
            'RunningStatus':'c','ErrorStatus':'c','JogStatusCR':'c','CRRobotType':'c','DragButtonSignal':'c','EnableButtonSignal':'c','RecordButtonSignal':'c',
            'ReappearButtonSignal':'c','JawButtonSignal':'c','SixForceOnline':'c','Reserve2[82]	':'82c','MActual[6]':'6d','Load':'d','CenterX':'d','CenterY':'d','CenterZ':'d',
            'User[6]':'6d','Tool[6]':'6d','TraceIndex':'d','SixForceValue[6]':'6d','TargetQuaternion[4]':'4d','ActualQuaternion[4]':'4d','Reserve3[24]':'24c'}
        data = self.s.recv(1440) #接收字长
        names=[]
        ii=range(len(dic))
        for key,i in zip(dic,ii):
            fmtsize=struct.calcsize(dic[key])   
            data1,data=data[0:fmtsize],data[fmtsize:]
            fmt=dic[key]    #"!"反转字节高低位 
            names.append(struct.unpack(fmt, data1))
            dic[key]=dic[key],struct.unpack(fmt, data1)
            self.s.close()
        return dic[Meaning]
        # print(dic['MessageSize'])
        # print(dic['DigitalOutputs'])
        # print(dic['RobotMode'])
        # print(dic['TimeStamp'])
        # print(dic['TestValue'])
        # print(dic['SpeedScaling'])
        # print(dic['QActual'])
        # print(dic['ToolVectorActual'])
        # print(dic['CenterX'])
        # print(dic['CenterY'])
        # print("I actual:",dic['I actual'])
        # print('I control:',dic['I control'])
        # print("\n")
