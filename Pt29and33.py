from socket import *

class Pt2933():
    def __init__(self,ip) :
        self.HOST = ip   # Dobot ip
        self.PORT29999 = 29999       
        self.PORT30003 = 30003      
        # self.s = socket(AF_INET, SOCK_STREAM)

    def Dashboard(self,Commands):
        print(Commands)
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((self.HOST,self.PORT29999)) 
        send_data=Commands
        s.send(send_data.encode('utf8'))  
        MsgRecv = s.recv(1024).decode()
        print(MsgRecv)
        s.close()
        return MsgRecv

    def ScriptPort(self,Commands):
        print(Commands)
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((self.HOST,self.PORT30003)) 
        send_data=Commands
        s.send(send_data.encode('utf8'))  
        MsgRecv = s.recv(1024).decode()
        print(MsgRecv)
        s.close()
        return MsgRecv